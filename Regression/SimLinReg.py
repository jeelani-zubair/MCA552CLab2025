# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# 1. Simulate dataset
# --------------------
# Let's simulate a linear relationship: y = 3x + 4 + noise
np.random.seed(42)  # for reproducibility
X = 2 * np.random.rand(100, 1)  # 100 random values between 0 and 2
y = 3 * X + 4 + np.random.randn(100, 1)  # Adding some Gaussian noise

# Visualize the raw data
plt.scatter(X, y, color='blue', alpha=0.5)
plt.title('Simulated Data')
plt.xlabel('X')
plt.ylabel('y')
plt.grid(True)
plt.show()

# 2. Preprocessing
# -----------------
# Check shape
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# No missing values, and only one feature — perfect for simple linear regression
# If needed, we could scale features or impute missing values here.

# Split into training and testing sets for evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Apply Simple Linear Regression
# ----------------------------------
# Create model
lin_reg = LinearRegression()

# Train the model
lin_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = lin_reg.predict(X_test)

# Model coefficients
print(f"Intercept (b0): {lin_reg.intercept_[0]:.2f}")
print(f"Slope (b1): {lin_reg.coef_[0][0]:.2f}")

# 4. Evaluate using R-squared
# ----------------------------
r2 = r2_score(y_test, y_pred)
print(f"R-squared score on test data: {r2:.4f}")

# 5. Visualize the fitted line
# -----------------------------
plt.scatter(X_test, y_test, color='green', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Regression Line')
plt.title('Simple Linear Regression Fit')
plt.xlabel('X_test')
plt.ylabel('y_test')
plt.legend()
plt.grid(True)
plt.show()
