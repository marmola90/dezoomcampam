{{ config(
    materialized='table',
    partition_by={
        "field":"year_release",
        "data_type":"int64",
        "range":{
            "start":0,
            "end":2017,
            "interval":20
        }
    },
    cluser_by=["platform","genre"],
)}}

with vgdata as (
    select * 
    from {{ref('stg_videogames')}}
)

SELECT 
    vgdata.code_id,
    vgdata.name,
    vgdata.platform,
    vgdata.year_release,
    vgdata.genre,
    vgdata.publisher,
    vgdata.na_sales,
    vgdata.eu_sales,
    vgdata.jp_sales,
    vgdata.other_sales,
    vgdata.global_sales
FROM vgdata