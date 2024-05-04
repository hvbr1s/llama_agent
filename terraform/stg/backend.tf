terraform {
  backend "s3" {
    bucket         = "ledger-staging-tfstates"
    key            = "knowledge-bot-2081/stg.tfstate"
    region         = "eu-west-1"
    role_arn       = "arn:aws:iam::454902641012:role/Atlantis-non-prd"
    encrypt        = true
    dynamodb_table = "ledger-staging-terraform-state-lock"
  }
}
