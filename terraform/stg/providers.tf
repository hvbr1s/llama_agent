provider "aws" {
  region = var.region
  assume_role {
    role_arn = var.atlantis_role
  }
  default_tags {
    tags = var.tags
  }
}
