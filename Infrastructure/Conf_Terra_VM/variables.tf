locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  default = "dtc-dezoomcamp-2023"
  type = string
}

variable "region" {
  description = "Region for GCP resources"
  default = "us-central1"
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

variable "instance" {
  type = string
  default = "de-zoomcamp"
}

variable "machine_type" {
  type = string
  default = "n1-standard-1"
}

variable "zone" {
  description = "Region for VM"
  type = string
  default = "us-central1"
}