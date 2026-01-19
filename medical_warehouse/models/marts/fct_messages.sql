{{ config(materialized='table', schema='analytics') }}

select
    m.message_id,
    d.date_key,
    c.channel_key,
    m.message_text,
    m.views,
    m.forwards,
    m.has_media,
    m.image_path
from {{ source('telegram', 'telegram_messages') }} m
join {{ ref('dim_dates') }} d
  on date(m.message_date) = d.full_date
join {{ ref('dim_channels') }} c
  on m.channel_name = c.channel_name
