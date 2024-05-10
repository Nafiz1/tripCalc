def minimize_transactions(balance):
    debtors = [person for person, debt in balance.items() if debt > 0]
    creditors = [person for person, debt in balance.items() if debt < 0]
    transactions = []
    
    while debtors and creditors:
        debtor = debtors.pop(0)
        creditor = creditors.pop(0)
        
        transfer_amount = min(abs(balance[debtor]), abs(balance[creditor]))
        balance[debtor] -= transfer_amount
        balance[creditor] += transfer_amount
        
        transactions.append((debtor, creditor, transfer_amount))
        
        if balance[debtor] > 0:
            debtors.append(debtor)
        elif balance[debtor] < 0:
            creditors.append(debtor)
            
        if balance[creditor] < 0:
            creditors.append(creditor)
        elif balance[creditor] > 0:
            debtors.append(creditor)
    
    return transactions

def calculate_payment(costs_part1, costs_part2):
    total_cost_part1 = sum(costs_part1.values())
    total_cost_part2 = sum(costs_part2.values())
    
    # Calculate the number of people involved in each part
    num_people_part1 = len(costs_part1)
    num_people_part2 = len(costs_part2)
    
    # Calculate the cost per person for each part
    cost_per_person_part1 = total_cost_part1 / num_people_part1
    cost_per_person_part2 = total_cost_part2 / num_people_part2
    
    # Initialize balances for both parts
    balance_part1 = {person: cost_per_person_part1 - cost for person, cost in costs_part1.items()}
    balance_part2 = {person: cost_per_person_part2 - cost for person, cost in costs_part2.items()}
    
    # Combine balances for participants in both parts
    combined_balance = {}
    for person in set(balance_part1.keys()) | set(balance_part2.keys()):
        combined_balance[person] = balance_part1.get(person, 0) + balance_part2.get(person, 0)
    
    transactions = minimize_transactions(combined_balance)
    
    print("\n")
    for debtor, creditor, amount in transactions:
        print(f"{debtor} should pay {amount} to {creditor}.")
    
    print(f"\nThe total cost of part 1 is: {total_cost_part1}.")
    print(f"The cost per person for part 1 is: {cost_per_person_part1}.")
    
    print(f"\nThe total cost of part 2 is: {total_cost_part2}.")
    print(f"The cost per person for part 2 is: {cost_per_person_part2}.")

# Inputs for part 1
costs_part1 = {}
names_part1 = ["nafiz", "hammad", "bilal", "samir", "amadis", "kevin"]

for name in names_part1:
    cost = float(input(f"Enter cost for {name} for part 1: "))
    costs_part1[name] = cost

# Inputs for part 2
costs_part2 = {}
names_part2 = ["nafiz", "hammad", "bilal", "amadis"]

for name in names_part2:
    cost = float(input(f"Enter cost for {name} for part 2: "))
    costs_part2[name] = cost

calculate_payment(costs_part1, costs_part2)
