import json
def add_expense(expenses,description,amount):
        expenses.append({"description" : description,"amount" : amount})
        print("Expense recorded!")

def get_total_expenses(expenses):
    sum=0
    for exp in expenses:
        sum += exp['amount']
    return sum

def get_balance(budget,expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget,expenses):
    print("Total Budget: {}".format(budget))
    print("Expenses: ")
    for exp in expenses:
        print("-{} : {}".format(exp['description'],exp['amount']))

    print("Total spent: {}".format(get_total_expenses(expenses)))
    print("Remaining budget: {}".format(get_balance(budget,expenses)))

def load_budget_data(filepath):
    try:
        with open(filepath,'r') as file:
            data = json.load(file)
            return data['initial_budget'],data['expenses']
    except(FileNotFoundError,json.JSONDecodeError):
        return 0,[]

def save_budget(filepath,initial_budget,expenses):
    data = {
        'initial_budget' : initial_budget,
        'expenses':expenses
    }

    with open(filepath,'w') as file:
        json.dump(data,file,indent=4)

def main():
    print("Salam! Welcome to tracr")
    
    filepath = "budget_data.json"
    initial_budget,expenses = load_budget_data(filepath)
    if initial_budget==0:
        initial_budget = float(input("Please enter your initial budget:"))
    budget = initial_budget
    
    while True:
        print("\n What would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enetr expense amount: "))
            add_expense(expenses,description,amount)

        elif choice == "2":
            show_budget_details(budget,expenses)

        elif choice == "3":
            save_budget(filepath,initial_budget,expenses)
            print("Exiting Trackr, Salam!")
            break
        else:
            print("Invalid choice, please choose again")

    
    




if __name__ == "__main__":
    main()