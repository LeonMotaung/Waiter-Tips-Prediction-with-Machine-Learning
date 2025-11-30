import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("tips.csv")



# Aggregate total tips by day
tips_by_day = data.groupby("day")["tip"].sum()

# Plot donut chart
plt.figure(figsize=(8, 6))
plt.pie(tips_by_day, labels=tips_by_day.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.5))
plt.title("Total Tips by Day")
plt.show()


#According to the visualization above, on Saturdays, most tips are given to the waiters. 
#Now let’s look at the number of tips given to waiters 
#by gender of the person paying the bill to see who tips waiters the most:
