def solve(balance, transactions):
    transactions.sort()
    for transaction in transactions:
        balance += transaction
        if balance < 0:
            balance -= 35
    return balance


ncases = int(input())
for index in range(1, ncases+1):
    balance = int(input())
    transactions = [ int(n) for n in input().strip().split(' ')[1:] ]
    solution = solve(balance, transactions)
    print(f"{index} {solution}")