select
    message_id,
    channel_name,
    cast(message_date as date) as message_date,
    message_text,
    length(message_text) as message_length,
    views as view_count,
    forwards as forward_count,
    has_media as has_image,
    image_path
from {{ source('telegram', 'telegram_messages') }}
where message_text is not null
