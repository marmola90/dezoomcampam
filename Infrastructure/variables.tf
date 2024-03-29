locals {
  data_lake_bucket = "dtc_data_lake" #
}

variable "project" {
  default = "de-zoomcampam" #the name of your project
  type = string
}

variable "region" {
  description = "Region for GCP resources"
  default = "us-central1" #your preference region 
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket"
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "videogames"
}