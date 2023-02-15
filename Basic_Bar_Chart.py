import pandas as pd
import matplotlib.pyplot as plt

# Data should be numpy array or pandas dataframe:
data = pd.read_csv("Data.csv")

# Gets the unique values in the data:
unique_values = entries.Entries.unique()
list_unique_vals = []
for i in unique_values:
        list_unique_vals.append(i)

# Counts the iterations of every unique data point:
list_repeats = []
for i in list_unique_vals:
        list_repeats.append(data["Column"].value_counts()[i])

# Assigns the list of unique items and their number of repeats as "keys" and "values"
keys = list_unique
values = list_repeats

# Sets the figure specifications:
fig = plt.figure(figsize = (10, 5), dpi=400)

# creating the bar plot
plt.bar(keys, values, color ='yellow',
        width = 0.4)

# Sets the scale of the graph:
plt.yticks(np.arange(0,10,1))
plt.xticks(np.arange(0,10,1))

plt.xlabel("X Label")
plt.ylabel("Y label")
plt.title("Graph Title")
plt.show()
