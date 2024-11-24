SELECT
  geo.sub_continent,
  COUNT(1) AS total,
  ROUND(AVG(ecommerce.purchase_revenue),2) AS mean_revenue,
  ROUND(STDDEV(ecommerce.purchase_revenue),2) AS stddev_revenue,
  ROUND((100*STDDEV(ecommerce.purchase_revenue))/AVG(ecommerce.purchase_revenue),2) AS cv_revenue,
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_2021*` t
WHERE
  COALESCE(ecommerce.purchase_revenue,0) > 0
GROUP BY
  1
ORDER BY
  total DESC
