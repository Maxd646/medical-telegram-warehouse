{{ config(materialized='table', schema='analytics') }}

select distinct
    channel_name as channel_key,
    channel_name
from {{ source('telegram', 'telegram_messages') }}
