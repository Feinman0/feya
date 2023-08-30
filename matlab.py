import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
data = pd.read_csv('dataset.csv')

# Data cleaning: Remove missing values
data = data.dropna()

# Calculate basic statistics
mean_age = data['age'].mean()
median_salary = data['salary'].median()
total_records = len(data)

# Plotting
plt.figure(figsize=(10, 6))

# Histogram of ages
plt.subplot(2, 2, 1)
plt.hist(data['age'], bins=20, color='blue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Scatter plot of age vs. salary
plt.subplot(2, 2, 2)
plt.scatter(data['age'], data['salary'], color='green', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary')

# Bar plot of job categories
plt.subplot(2, 1, 2)
job_counts = data['job'].value_counts()
plt.bar(job_counts.index, job_counts.values, color='purple')
plt.xticks(rotation=45)
plt.xlabel('Job Category')
plt.ylabel('Count')
plt.title('Job Category Distribution')

plt.tight_layout()

# Print out the calculated statistics
print(f"Mean Age: {mean_age:.2f}")
print(f"Median Salary: ${median_salary:.2f}")
print(f"Total Records: {total_records}")

# Save the plots as image files
plt.savefig('analysis_plots.png')

# Show the plots
plt.show()
