import os

from prefect import flow
from prefect_dbt.cli.commands import DbtCliProfile, DbtCoreOperation

@flow(log_prints=True)
def dbt_run(dir:str)->DbtCoreOperation:
    """Run dbt commandas with CLI commands"""
    dir=f'{dir}dbt/'
    #dbt_path = os.path.realpath("../../dbt")
    #dbt_cli_profile = DbtCliProfile.load("profile-block")
    dbt_path=os.path.dirname(dir)
    #print(dbt_path)
    #print(dbt_p)
    dbt_op = DbtCoreOperation(
        commands=["dbt debug", "dbt build --var 'is_test_run: false'"],
        working_dir=dbt_path,
        project_dir=dbt_path,
        profiles_dir=dbt_path,
    ).run()
    
    return dbt_op
    
if __name__=='__main__':
    dir='/home/amarmol/dezoomcampam/'
    dbt_run(dir)