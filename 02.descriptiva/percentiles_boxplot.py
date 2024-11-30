from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

# Configura el cliente de BigQuery
client = bigquery.Client()

# Consulta para obtener los datos de BigQuery
query = """
SELECT
  COALESCE(item.item_category,'?') AS category_column,
  item.price AS numeric_column,
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_2021*` t,
  UNNEST (items) item
WHERE
  COALESCE(ecommerce.purchase_revenue,0) > 0
  AND item.price IS NOT NULL 

"""

# Ejecuta la consulta y carga los datos en un DataFrame de Pandas
df = client.query(query).to_dataframe()

# Filtra las 5 categorías predominantes
top_categories = df['category_column'].value_counts().head(5).index
filtered_df = df[df['category_column'].isin(top_categories)]

# Ordena las categorías por frecuencia
category_order = filtered_df['category_column'].value_counts().index
filtered_df['category_column'] = pd.Categorical(filtered_df['category_column'], categories=category_order, ordered=True)

# Crear un box-plot personalizado sin outliers (máximo y mínimo reales)
plt.figure(figsize=(10, 6))
filtered_df.boxplot(
    column='numeric_column',
    by='category_column',
    showfliers=False,  # Elimina visualización de outliers
    grid=False
)

# Configura el gráfico
plt.title('Box-Plot sin Valores Atípicos')
plt.suptitle("")  # Elimina el título adicional generado por defecto
plt.xlabel('Categoría (ordenadas por predominancia)')
plt.ylabel('Valor')
plt.xticks(rotation=45)  # Gira las etiquetas para mayor legibilidad

# Muestra el gráfico
plt.show()
