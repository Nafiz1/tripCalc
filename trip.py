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


def calculate_payment(costs):
    # Calculate the total cost and number of people for each part
    total_costs = []
    num_people = []
    for part_costs in costs:
        total_cost = sum(part_costs.values())
        total_costs.append(total_cost)
        num_people.append(len(part_costs))

    # Calculate the cost per person for each part
    cost_per_persons = [
        total_cost / num for total_cost, num in zip(total_costs, num_people)
    ]

    # Initialize balances for each part
    balances = [
        {person: cost_per_person - cost for person, cost in part_costs.items()}
        for part_costs, cost_per_person in zip(costs, cost_per_persons)
    ]

    # Combine balances for participants in all parts
    combined_balance = {}
    for balance in balances:
        for person, amount in balance.items():
            combined_balance[person] = combined_balance.get(person, 0) + amount

    transactions = minimize_transactions(combined_balance)

    print("\n")
    for debtor, creditor, amount in transactions:
        print(f"{debtor} should pay {amount:.2f} to {creditor}.")

    for i, (total_cost, num_persons, cost_per_person) in enumerate(
        zip(total_costs, num_people, cost_per_persons), 1
    ):
        print(f"\nThe total cost of part {i} is: {total_cost:.2f}.")
        print(f"The cost per person for part {i} is: {cost_per_person:.2f}.")


def get_costs_for_part(names):
    costs = {}
    for name in names:
        cost = float(input(f"Enter cost for {name}: "))
        costs[name] = cost
        cost = round(cost, 2)
    return costs


# Initialize an empty list to store costs for each part
all_costs = []
part_number = 1

while True:
    names_part = input(
        f"Enter names separated by commas for part {part_number} (or type 'done' to stop): "
    ).split(",")
    names_part = [name.strip().lower() for name in names_part]

    if "done" in names_part:
        break

    costs_part = get_costs_for_part(names_part)
    all_costs.append(costs_part)
    part_number += 1

# Call the modified function with the list of costs
calculate_payment(all_costs)
