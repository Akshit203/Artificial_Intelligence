import numpy as np

#   [emp_id, age, salary]

employees = np.array([
    [101, 25, 30000],
    [102, 30, 45000],
    [103, 28, 38000],
    [104, 35, 60000],
    [105, 26, 32000]
])

print(employees[employees[:, 2] > 40000])

# avg salary
print(np.mean(employees[:,1]))

# replace salary less than 35000 with 35000

employees[:,2] = np.where(employees[:,2] < 35000, 35000, employees[:,2])
print(employees)

#################################

sales = np.array([
    [[200, 220, 210], [300, 320, 310]],   # Day 1
    [[250, 260, 255], [330, 340, 335]],   # Day 2
    [[270, 280, 275], [360, 370, 365]]    # Day 3
])
#   shape → (days, stores, products)

print(np.sum(sales, axis =(1,2)))
