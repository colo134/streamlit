# Import necessary libraries
import seaborn as sns  # Importing Seaborn library for data visualization
import plotly.express as px
import pandas as pd


# Load the tips dataset from Seaborn
tips = sns.load_dataset('tips')  # Loading the dataset

# Display the first few rows of the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset
# Visualizations using Plotly
fig1 = px.bar(tips, x="day", y="tip")
fig1.show()
