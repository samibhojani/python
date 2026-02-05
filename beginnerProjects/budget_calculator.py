print("Add your income: ")
salary = int(input("Salary: "))
side_hustle = int(input("Side hustles: "))
roi = int(input("ROI: "))

total_income = salary + side_hustle + roi


print("Add your expenses: ")
rent = int(input("Rent Amount: "))
education = int(input("Educational Spent: "))
health = int(input("Medical Expense: "))
grocery = int(input("Groceries: "))
transport = int(input("Fuel & Transport expense: "))
other = int(input("Misc expense: "))

total_expense = rent + education + health + grocery + transport + other

persons = int(input("Bill divided into persons: "))


savings = total_income - total_expense

for i in range(0, 4):
    print("processing.......")

print(f"Total monthly income: {total_income} PKR")
print(f"Total monthly expense: {total_expense} PKR")
print(f"Saving amount: {savings}")
print(f"Share per person = {total_expense / persons}")
print(f"Amount required to quit the rat race: {total_expense * 6}")
