import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("tips.csv")

# Prepare features and target
X = data[["total_bill"]]  # independent variable
y = data["tip"]           # target

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Predict values for regression line
y_pred = model.predict(X)

# Plot scatter and regression line
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data["total_bill"], data["tip"], 
                      s=data["size"]*20,       # bubble size
                      c=pd.Categorical(data["day"]).codes, # color by day
                      cmap="viridis", alpha=0.6)

plt.plot(data["total_bill"], y_pred, color="red", linewidth=2, label="OLS Regression")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Tips vs Total Bill with Regression Line")
plt.legend()
plt.colorbar(scatter, label="Day code (0=Thur, 1=Fri, etc.)")
plt.show()
