import os

from prefect import flow
from prefect_dbt.cli.credentials import DbtCliProfile
from prefect_dbt.cli.commands import trigger_dbt_cli_command

@flow(log_prints=True)
def dbt_transform():
    dbt_path = os.path.realpath("../../dbt")
    dbt_cli_profile = DbtCliProfile.load("profile-block")

    dbt_op = trigger_dbt_cli_command(
        "dbt build",
        project_dir=dbt_path,
        overwrite_profiles=True,
        dbt_cli_profile=dbt_cli_profile
    )
    
    return dbt_op
    
if __name__=='__main__':
    dbt_transform()