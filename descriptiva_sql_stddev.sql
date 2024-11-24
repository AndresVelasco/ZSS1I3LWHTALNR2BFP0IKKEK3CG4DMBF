SELECT
  item.item_category,
  COUNT(1) AS total,
  ROUND(AVG(item.price),2) AS mean_revenue,
  ROUND(STDDEV(item.price),2) AS stddev_revenue,
  ROUND((100*STDDEV(item.price))/AVG(item.price),2) AS cv_revenue,
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_2021*` t, UNNEST (items) item
WHERE
  COALESCE(ecommerce.purchase_revenue,0) > 0
GROUP BY
  1
ORDER BY
  total DESC
