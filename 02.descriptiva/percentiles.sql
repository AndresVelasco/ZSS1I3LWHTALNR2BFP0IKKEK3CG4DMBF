SELECT
  item.item_category,
  ROUND(AVG(item.price),2) AS mean_revenue,
  ROUND(APPROX_QUANTILES(item.price,4)[OFFSET(1)],2) AS percent_25,
  ROUND(APPROX_QUANTILES(item.price,4)[OFFSET(2)],2) AS percent_50,
  ROUND(APPROX_QUANTILES(item.price,4)[OFFSET(3)],2) AS percent_75,
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_2021*` t, UNNEST (items) item
WHERE
  COALESCE(ecommerce.purchase_revenue,0) > 0
GROUP BY
  1
ORDER BY
  2 DESC
