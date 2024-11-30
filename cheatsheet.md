# Cheat Sheet de Estadística

| Concepto               | Fórmula Matemática                       | Implementación en Python (scipy.stats)  | Ejemplo con DataFrame |
|------------------------|------------------------------------------|-----------------------------------------|-----------------------|
| **Media**              | \( \mu = \frac{1}{n} \sum_{i=1}^{n} x_i \) | `scipy.stats.tmean(data)`               | `df['columna'].mean()` |
| **Varianza**           | \( \sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2 \) | `scipy.stats.tvar(data)`                | `df['columna'].var()` |
| **Desviación Estándar**| \( \sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2} \) | `scipy.stats.tstd(data)`                | `df['columna'].std()` |
| **Covarianza**         | \( \text{Cov}(X,Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_X)(y_i - \mu_Y) \) | `scipy.stats.todds(data1, data2)`      | `df['col1'].cov(df['col2'])` |
| **Estandarización**    | \( z = \frac{x - \mu}{\sigma} \)        | `scipy.stats.zscore(data)`              | `df['columna'] = (df['columna'] - df['columna'].mean()) / df['columna'].std()` |
| **Cálculo de p-value (z-test)** | Para z-test: \( p = P(Z > |z|) \) | `scipy.stats.norm.cdf(z_score)`         | `scipy.stats.norm.cdf(z_score)` |
| **Cálculo de p-value (t-test)** | Para t-test: \( p = P(T > |t|) \) | `scipy.stats.ttest_1samp(data, popmean)` | `scipy.stats.ttest_1samp(df['columna'], popmean=0)` |

