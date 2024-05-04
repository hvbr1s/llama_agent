variable "env" {
  type        = string
  description = "The environment used to create resources"
}

variable "region" {
  default     = "eu-west-1"
  type        = string
  description = "The region to use for aws provider setup"
}

variable "atlantis_role" {
  type        = string
  description = "Atlantis role to use for aws provider setup"
}

variable "tags" {
  type        = map(string)
  description = "The tags to use to aws resources."
}

variable "secrets" {
  default     = {}
  type        = map(string)
  description = "secrets in AWS Secrets Manager"
}

variable "openai_api_key" {
  type        = string
}

variable "alchemy_api_key" {
  type        = string
}
variable "pinecone_api_key" {
  type        = string
}
