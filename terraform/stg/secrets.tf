resource "aws_secretsmanager_secret" "secrets" {
  name        = local.project_id
  description = "Secrets for knowledge bot. You must use terraform to add a secret"
}

########################################################################
# Decode Secrets from KMS
# echo -n "text" | base64 > text_encoded
# aws kms encrypt --key-id alias/ledger-global-prod --plaintext "text_encoded"
########################################################################
data "aws_kms_secrets" "kms_secrets" {
  for_each = var.secrets
  secret {
    name    = each.key
    payload = each.value
  }
}

########################
# SecretsManager entries
# key:value
########################
resource "aws_secretsmanager_secret_version" "secretsmanager_secret_version" {
  secret_id = aws_secretsmanager_secret.secrets.id
  secret_string = jsonencode(
    merge(
      {
        PINECONE_ENVIRONMENT               = "northamerica-northeast1-gcp",
        API_KEY_NAME                       = "Authorization",
        LANGCHAIN_ENDPOINT                 = "https://api.smith.langchain.com",
        LANGCHAIN_PROJECT                  = "SamanthaBot Internal",
        LANGCHAIN_TRACING_V2               = "true",
      },
      {
        for key, val in var.secrets : key => data.aws_kms_secrets.kms_secrets[key].plaintext[key]
      }
    )
  )
}
