from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

@task(retries=3,log_prints=True)
def extract_from_gcs(datafile:str)->Path:
    """Extract from GCS

    Args:
        datafile (str): _description_

    Returns:
        Path: _description_
    """
    gcs_path=f"data/videogames/{datafile}"
    gcs_block = GcsBucket.load("zomm-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../../")
    return Path(f"../../{gcs_path}")

@task(retries=3,log_prints=True)
def fetchData(path:Path)->pd.DataFrame:
    df=pd.read_parquet(path)
    print(f"Shape of the dataframe: {df.shape}")
    print(df.isnull().sum())
    return df

@task(retries=3,log_prints=True)
def write_bq(df:pd.DataFrame)->None:
    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")
    print('Creating table..............')
    df.to_gbq(
        destination_table="videogames.videogames_data",
        project_id="de-zoomcampam",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="replace"
    )
    print('Table created............')

@flow(name='Principal',log_prints=True)
def gcs_to_bq()->None:
    """Main Function
    """
    datafile='Video_Games.parquet'
    path=extract_from_gcs(datafile)
    df = fetchData(path)
    write_bq(df)
  
if __name__== '__main__':
    gcs_to_bq()