import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("tips.csv")
print(data.head())

#   the total bill paid
# number of people at a table
# and the day of the week:

print(data["total_bill"].describe())
print(data["size"].describe())
print(data["day"].describe())
