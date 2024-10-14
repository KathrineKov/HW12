import numpy as np
import pandas as pd

income = np.array([10000, 12000, 9000, 11000, 15000, 13000, 16000, 14000, 17000, 13500])
income_without_tax = income * 0.7
expenses = np.array([8000, 8500, 7000, 9000, 12000, 11000, 10000, 9500, 11500, 10500])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
data = {
    'Income (after tax)': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data, index=months)

print("Full DataFrame:")
print(df)
print("\n1st Quarter Data (Jan, Feb, Mar):")
print(df.loc[['Jan', 'Feb', 'Mar']])