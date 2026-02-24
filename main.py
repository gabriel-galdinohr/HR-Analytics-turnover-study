import pandas as pd

data = {
    'Employee': ['Ana', 'Carlos', 'Beatriz', 'David', 'Elena'],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'Status': ['Active', 'Left', 'Active', 'Left', 'Active'],
    'Salary_USD': [5000, 7000, 4800, 5500, 7200]
}

df = pd.DataFrame(data)

total_employees = len(df)
total_exits = len(df[df['Status'] == 'Left'])
turnover_rate = (total_exits / total_employees) * 100

print(f"Global Turnover Rate: {turnover_rate}%")

exits_by_dept = df[df['Status'] == 'Left'].groupby('Department').size()
print("\nExits by Department:")
print(exits_by_dept)
