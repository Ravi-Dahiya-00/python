import pandas as pd

# Sample data to be written to Excel
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 34, 29, 45],
    'Department': ['HR', 'Engineering', 'Marketing', 'Finance'],
    'Salary': [50000, 70000, 55000, 60000]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Specify the filename
filename = 'employee_data.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(filename, index=False)

print(f"Data written to {filename} successfully.")
