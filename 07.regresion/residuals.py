import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Function to plot residuals
def plot_residuals(X, y, y_pred, title):
    residuals = y - y_pred
    plt.scatter(y_pred, residuals, alpha=0.7)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title(title)
    plt.xlabel('Predicted values (ŷ)')
    plt.ylabel('Residuals')
    plt.show()

# 1. Satisfactory Fit (Random residuals)
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2.5 * X.flatten() + np.random.randn(100) * 2  # Linear relationship with noise

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plot_residuals(X, y, y_pred, "1. Satisfactory Fit (Random residuals)")

# 2. Non-linear relationship (Model can't capture non-linearity)
X_nonlinear = np.random.rand(100, 1) * 10
y_nonlinear = 0.5 * (X_nonlinear**2).flatten() + np.random.randn(100) * 2  # Quadratic relationship with noise

# Fit linear model (incorrect)
model.fit(X_nonlinear, y_nonlinear)
y_pred_nonlinear = model.predict(X_nonlinear)

plot_residuals(X_nonlinear, y_nonlinear, y_pred_nonlinear, "2. Non-linear Relationship (Linear model residuals)")

# 3. Heteroscedasticity (Increasing variance with X)
X_hetero = np.random.rand(100, 1) * 10
y_hetero = 2.5 * X_hetero.flatten() + np.random.randn(100) * (X_hetero.flatten())  # Increasing variance

model.fit(X_hetero, y_hetero)
y_pred_hetero = model.predict(X_hetero)

plot_residuals(X_hetero, y_hetero, y_pred_hetero, "3. Heteroscedasticity (Increasing residuals)")

# Optional: Polynomial regression to show improved fit for non-linear case
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_nonlinear)

model_poly = LinearRegression()
model_poly.fit(X_poly, y_nonlinear)
y_pred_poly = model_poly.predict(X_poly)

plot_residuals(X_nonlinear, y_nonlinear, y_pred_poly, "Polynomial Fit (Improved for non-linearity)")
