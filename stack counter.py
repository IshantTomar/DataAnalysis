amount = int(input("Enter amount: "))
temp = amount
non_stack = temp%64
stacks = temp/64

print(f"{int(stacks)} stacks and {non_stack}.")
