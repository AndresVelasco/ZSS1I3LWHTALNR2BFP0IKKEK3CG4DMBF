SELECT  
    ROUND(AVG(ecommerce.purchase_revenue),2) AS mean_revenue,
    ROUND(APPROX_QUANTILES(ecommerce.purchase_revenue,10)[OFFSET(5)],2) AS median_revenue,
    ROUND(AVG(ecommerce.total_item_quantity),2) AS mean_items,
    ROUND(APPROX_QUANTILES(ecommerce.total_item_quantity,10)[OFFSET(5)],2) AS median_items,
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_202101*`
WHERE COALESCE(ecommerce.purchase_revenue,0) > 0
