SELECT
  item.item_category1,
  COUNT(1) AS total,
  SUM(quantity) AS total_quantity,
  SUM(item.price) AS total_price,
  ROUND(AVG(item.price),2) AS mean_revenue,
  ROUND(APPROX_QUANTILES(item.price,10)[OFFSET(5)],2) AS median_revenue,
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_2021*` t, UNNEST (items) item
WHERE
  COALESCE(ecommerce.purchase_revenue,0) > 0
GROUP BY
  1
ORDER BY
  total DESC
