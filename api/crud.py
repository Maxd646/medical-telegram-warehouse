from sqlalchemy import text

TOP_PRODUCTS_QUERY = """
SELECT word AS term, count(*) AS freq
FROM (
    SELECT regexp_split_to_table(lower(message_text), '\s+') AS word
    FROM analytics.fct_messages
) t
WHERE length(word) > 3
GROUP BY word
ORDER BY freq DESC
LIMIT :limit;
"""
