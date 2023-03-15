from pathlib import Path
import pandas as pd
from prefect import flow, task
import kaggle
from prefect_gcp.cloud_storage import GcsBucket

@task(retries=3,log_prints=True)
def downloadData(dataset_kaggle:str)-> None:
    """Download Data from Kaggle

    Args:
        dataset_kaggle (str): Direcction of Kaggle Data Source
    """
    print('Downloading file from Kaggle..........')
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_kaggle, path=f'../data/', unzip=True)
    print('File download to destination Dir..........')

#internal function call
def localPath(dataset_file:str)->Path:
    """Local Path of the file

    Args:
        dataset_file (str): file description

    Returns:
        Path: return path of the file
    """
    return Path(f'../data/{dataset_file}').as_posix() 

# internal funcion call
def remotePath(dataset_file)->Path:
    """Remote Path of the file

    Args:
        dataset_file (_type_): file description

    Returns:
        Path: return remote path of the file
    """
    return Path(f'data/videogames/{dataset_file}').as_posix() 

@flow(name='Subflow fetchData',retries=3, log_prints=True)
def fetchData(dataset_kaggle:str, dataset_file:str)-> pd.DataFrame:
    """Fetching data from Kaggle

    Args:
        dataset_kaggle (str): dataset from kaggle
        dataset_file (str): name of the file

    Returns:
        pd.DataFrame: return dataframe value
    """
    downloadData(dataset_kaggle)
    path = localPath(dataset_file)
    df=pd.read_csv(path)
    return df

@task(retries=3,log_prints=True)
def write_local(df:pd.DataFrame, dataset_file:str)->None:
    """Write local

    Args:
        df (pd.DataFrame): _description_
        dataset_file (str): _description_

    Returns:
        Path: _description_
    """
    df.to_parquet(localPath(dataset_file))
    print('Writing to local Dir in parquet extension.......')

@task(retries=3,log_prints=True)
def write_gcs(localPath:Path, remotePath:Path)->None:
    print("Uploading file to GCS")
    gcs_Block= GcsBucket.load("zomm-gcs")
    gcs_Block.upload_from_path(from_path=f"{localPath}",to_path=remotePath)
    print("Uploaded file to GCS")
    return

@flow(name='EL Principal')
def el_web_to_gcs()->None:
    """The Main EL function
    """
    dataset_file=f'Video_Games.csv'
    dataset_file_parquet=f'Video_Games.parquet'
    dataset_kaggle=f'ibriiee/video-games-sales-dataset-2022-updated-extra-feat'

    df= fetchData(dataset_kaggle,dataset_file)
    write_local(df,dataset_file_parquet)
    write_gcs(localPath(dataset_file_parquet),remotePath(dataset_file_parquet))

if __name__ == '__main__':
    """Principal MAIN"""
    el_web_to_gcs()