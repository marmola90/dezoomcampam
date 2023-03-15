# **Data pipeline for Video Game Sales monitoring**

### **Data pipeline for uploading, preprocessing, and visualising Video Games Sales data using Google Cloud Platform**

This repo includes implementation of a pipeline for visualization of Video Games Sales data: list of video games with sales greater than 100,000 copies.

The pipeline has scheduled jobs with monthly scheduled tables.

## Project Contents

- [Problem description](#problem-description)
- [Contents](#contents)
- [Data source](#data-source)
- [Description of architecture](#description-of-architecture)
- Steps

# Problem Description
For the following project, the data set to use will be video game sales.

When looking for which data set to use, I found this one, which caught my attention a lot. Who doesn't like video games? Who has not thought about knowing which console is the most popular? I think that for most it is the favorite hobby.

Based on this, we will try to answer questions like:

>1. Which region has had the best performance in terms of sales?
>2. What are the top 10 games currently generating the most sales globally?
>3. What are the best games for different regions?
>4. What are the main game genres that are generating big sales?
>5. Does the publisher have any impact on regional sales?

# Technologies
The technologies that were chosen to use are the following:
- Cloud: GCP  
    - Data Lake (DL): GCS
    - Data Warehouse (DWH): BigQuery
- Infrastructure as code (IaC): Terraform
- Workflow Orchestation: Prefect
- Transforming Data: DBT
- Data Visualization: Looker Studio

# Contents 
`/Workflow orchestration/Data` :  Data Source  
`/Dbt` : dbt files and folders  
`/Images` : printscreens for Readme files  
`/Infrastructure` : Terraform files  
`/Workflow orchestration` : Flows and deployments files for Prefect orchestations  

# Data Source
Data has been provided by [Kaggle](https://www.kaggle.com/datasets/ibriiee/video-games-sales-dataset-2022-updated-extra-feat).

# Description of architecture
![Architecture Pipeline](Images/Pipeline%20Archictecture%20dark.png "Pipeline Architecture")  

The data source (*at raw level*) is on csv format and located in [Kaggle](https://www.kaggle.com/datasets/ibriiee/video-games-sales-dataset-2022-updated-extra-feat). 

The pipeline includes the next steps:
- Terraform was used as IaC for the creation of the Bucket and BigQuery, as well as for the creation of a VM.
- The initial data will be download from Kaggle Datasets.
- The data will be stored in Google Cloud Storage as Data Lake.
- The data will be moved from the data lake to a DWH.
- The DWH data will be transformed and prepared for display on a dashboard.
- The dashboard will be created to visualize the data.

