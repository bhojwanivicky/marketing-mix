import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Marketing_data.csv")

# Data Cleaning
df.columns = df.columns.str.strip()
df['Income'] = df['Income'].str.replace('[$,]', '', regex=True).astype(float)
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
df['Age'] = 2024 - df['Year_Birth']
df['Total_Spending'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

df['Income'].fillna(df.groupby(['Education', 'Marital_Status'])['Income'].transform('mean'), inplace=True)

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Total_Spending"])
plt.title("Box Plot of Total Spending")
plt.xlabel("Total Spending")
plt.show()

# Heatmap
corr_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Correlation Between Variables")
plt.show()