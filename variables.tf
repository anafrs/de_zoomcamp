variable "project" {
  description = "Project"
  default     = "de-zoomcap-411511"
}


variable "region" {
  description = "Region"
  default     = "europe-west2"
}


variable "location" {
  description = "Project Location"
  default     = "EU"
}


variable "bq_dataset_name" {
  description = "BigQuery Dataset Name"
  default     = "zoomcamp_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "de-zoomcap-411511-bucket"
}