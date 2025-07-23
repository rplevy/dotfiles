import matplotlib.pyplot as plt

def calculate_equivalent_salary(initial_salary, monthly_expense_reduction):
    approximate_tax_factor = 0.74
    net_salary = initial_salary * approximate_tax_factor

    # Calculate cumulative yearly reduction from expense cuts
    yearly_reduction = monthly_expense_reduction * 12
    new_net_salary = net_salary + yearly_reduction

    # Calculate equivalent gross salary increase
    equivalent_gross = new_net_salary / approximate_tax_factor
    return equivalent_gross - initial_salary

# Get user input
initial_salary = float(input("Enter your current annual salary: "))
num_points = int(input("How many data points do you want to calculate? "))
min_reduction = float(input("Minimum monthly reduction amount ($): "))
max_reduction = float(input("Maximum monthly reduction amount ($): "))

# Calculate data points
reductions = []
salary_increases = []
for monthly_reduction in range(int(min_reduction), int(max_reduction) + 1):
    increase = calculate_equivalent_salary(initial_salary, monthly_reduction)
    reductions.append(monthly_reduction)
    salary_increases.append(increase)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(reductions, salary_increases, 'b-', marker='o')
plt.title(f'Equivalent Salary Increase for Different Monthly Expense Reductions\nInitial Salary: ${initial_salary:,}')
plt.xlabel('Monthly Expense Reduction ($)')
plt.ylabel('Equivalent Salary Increase ($)')
plt.grid(True)
plt.show()

# created using deepseek R1

# ### Explanation:
# 1. **Function** `calculate_equivalent_salary`: This function calculates the equivalent salary increase based on monthly expense reductions, using your provided formula.
# 2. **User Input**: The script prompts you to enter:
#    - Initial annual salary
#    - Number of data points to calculate (range of expense reductions)
#    - Minimum and maximum monthly reduction amounts
# 3. **Data Collection**: For each monthly reduction amount in the range, the script calculates the equivalent salary increase.
# 4. **Plotting**: The script creates a clear graph showing the relationship between monthly expense reductions and corresponding salary increases.

# ### Optional Enhancements:
# - You can modify `approximate_tax_factor` to match your specific tax assumptions.
# - Adjust the number of data points or the range of reductions based on your needs.

# To use this script:

# 1. Save it as a Python file (e.g., `salary_increase_plot.py`).
# 2. Run it in a Python environment (like VS Code, Jupyter Notebook, or Terminal).
# 3. Enter the requested inputs and view the resulting graph.

# This will provide a clear visual representation of how different monthly expense reductions translate to equivalent salary increases.
