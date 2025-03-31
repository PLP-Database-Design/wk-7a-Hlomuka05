import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target variable to the DataFrame
df['species'] = iris.target

# Mapping the numeric target to species names for better clarity
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
df.head()
# Check data types and missing values
df.info()

# Check for any missing values
df.isnull().sum()
# Dropping any rows with missing values (if there are any)
df = df.dropna()

# Alternatively, you could fill missing values using df.fillna(value) if necessary
# Get basic statistics
df.describe()
import matplotlib.pyplot as plt

# Line chart showing trends for petal length for each species
plt.figure(figsize=(10,6))
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data['petal length (cm)'], label=species)

plt.title("Petal Length Trends by Species")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
# Bar chart comparing the average petal length by species
plt.figure(figsize=(8,5))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()
# Bar chart comparing the average petal length by species
plt.figure(figsize=(8,5))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()
# Histogram of petal length
plt.figure(figsize=(8,5))
df['petal length (cm)'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()
# Scatter plot to visualize the relationship between sepal length and petal length
plt.figure(figsize=(8,5))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['species'].map({'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}))
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

