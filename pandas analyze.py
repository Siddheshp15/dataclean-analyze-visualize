import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 15]}
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Plot Data
plt.bar(df['Category'], df['Values'])
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Sample Bar Chart")
plt.show()