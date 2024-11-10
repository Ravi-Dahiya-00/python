# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn's built-in datasets
data = sns.load_dataset('titanic')

# Display the first few rows of the dataset
print("First 5 rows of the Titanic dataset:")
print(data.head())

# Step 1: Data Cleaning
# Drop unnecessary columns
data = data.drop(columns=['deck', 'embark_town', 'alive', 'adult_male', 'who'])

# Fill missing values in 'age' and 'embarked' columns
data['age'].fillna(data['age'].median(), inplace=True)
data['embarked'].fillna(data['embarked'].mode()[0], inplace=True)

# Display cleaned data info
print("\nCleaned Data Information:")
print(data.info())

# Step 2: Exploratory Data Analysis (EDA)

# Analysis 1: Survival Rate by Passenger Class
plt.figure(figsize=(8, 6))
sns.barplot(x='class', y='survived', data=data, ci=None)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Analysis 2: Age Distribution of Passengers
plt.figure(figsize=(8, 6))
sns.histplot(data['age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Analysis 3: Survival Rate by Gender
plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='survived', data=data, ci=None)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.show()

# Analysis 4: Correlation Heatmap for Numerical Variables
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix of Titanic Dataset')
plt.show()

# Step 3: Summary Statistics
# Calculate and display survival rate
survival_rate = data['survived'].mean() * 100
print(f"\nOverall Survival Rate: {survival_rate:.2f}%")

# Calculate survival rate by gender
survival_rate_by_gender = data.groupby('sex')['survived'].mean() * 100
print("\nSurvival Rate by Gender:")
print(survival_rate_by_gender)

# Calculate survival rate by passenger class
survival_rate_by_class = data.groupby('class')['survived'].mean() * 100
print("\nSurvival Rate by Passenger Class:")
print(survival_rate_by_class)
