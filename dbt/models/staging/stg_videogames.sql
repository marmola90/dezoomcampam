{{ config(
    materialized='view',
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

with vgdata as 
(
    select *
    from {{source('staging','videogames_data')}}
    where Name is not null
)

select
    ROW_NUMBER() OVER() AS code_id,
    CAST(Name as STRING) as name,
    CAST(Platform as STRING) as platform,
    COALESCE(CAST(Year_of_Release as INTEGER), 0) as year_release,
    CAST(Genre as STRING) as genre,
    COALESCE(Publisher,'Not provided')as publisher,
    CAST(NA_Sales as NUMERIC) as na_sales,
    CAST(EU_Sales as NUMERIC) as eu_sales,
    CAST(JP_Sales as NUMERIC) as jp_sales,
    CAST(Other_Sales as NUMERIC) as other_sales,
    CAST(Global_Sales as NUMERIC) as global_sales
FROM vgdata

{% if var('is_test_run', default=false) %}

  limit 100

{% endif %}