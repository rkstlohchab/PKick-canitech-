n = int(input("Enter number of customers:"))
my_list = []
for i in range(1, n + 1):
    budget = int(input("Enter the customer budgets:"))
    my_list.append(budget)
my_list.sort()

length = len(my_list)
revenue = []

for j in my_list:
    j *= length
    revenue.append(j)
revenue.sort()

print(revenue)