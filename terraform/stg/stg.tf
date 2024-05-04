#module "knowledge-bot" {
#  source = "git::ssh://git@github.com/LedgerHQ/tf-aws-ledger-apps.git//knowledge-bot"
#  # Application variables
#
#}

/*
data "aws_kms_secrets" "openai_api_key" {
  secret {
    name    = "api_key"
    payload = var.openai_api_key
  }
}

data "aws_kms_secrets" "alchemy_api_key" {
  secret {
    name    = "api_key"
    payload = var.alchemy_api_key
  }
}

data "aws_kms_secrets" "pinecone_api_key" {
  secret {
    name    = "api_key"
    payload = var.pinecone_api_key
  }
}

resource "aws_secretsmanager_secret" "openai" {
  name = format("%s/tf-openai", local.project_id)
  tags = var.tags
}

resource "aws_secretsmanager_secret_version" "openai" {
  secret_id = aws_secretsmanager_secret.openai.id
  secret_string = jsonencode({
    OPENAI_API_KEY = data.aws_kms_secrets.openai_api_key.plaintext["api_key"]
  })
}

resource "aws_secretsmanager_secret" "alchemy" {
  name = format("%s/tf-alchemy", local.project_id)
  tags = var.tags
}

resource "aws_secretsmanager_secret_version" "alchemy" {
  secret_id = aws_secretsmanager_secret.alchemy.id
  secret_string = jsonencode({
    ALCHEMY_API_KEY = data.aws_kms_secrets.alchemy_api_key.plaintext["api_key"]
  })
}

resource "aws_secretsmanager_secret" "pinecone" {
  name = format("%s/tf-pinecone", local.project_id)
  tags = var.tags
}

resource "aws_secretsmanager_secret_version" "pinecone" {
  secret_id = aws_secretsmanager_secret.pinecone.id
  secret_string = jsonencode({
    PINECONE_API_KEY = data.aws_kms_secrets.pinecone_api_key.plaintext["api_key"]
  })
}
*/
