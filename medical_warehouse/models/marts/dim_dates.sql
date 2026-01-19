with dates as (
    select generate_series(
        '2024-01-01'::date,
        '2026-12-31'::date,
        '1 day'
    )::date as full_date
)
select
    to_char(full_date, 'YYYYMMDD')::int as date_key,
    full_date,
    extract(year from full_date) as year,
    extract(month from full_date) as month,
    to_char(full_date, 'Month') as month_name,
    extract(dow from full_date) in (0,6) as is_weekend
from dates
