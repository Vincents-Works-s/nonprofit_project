def intro_message():
    print("Welcome to the Non Profit/Charity Donater")
    
def print_nonprofit():
    gates_foundation_amount = 0
    spaceX_amount = 0
    trump_amount = 0
    dnc_amount = 0
    
    print(f"Bill and Melinda Gates Foundation: {gates_foundation_amount}")
    print(f"spaceX: {spaceX_amount}")
    print(f"Trump Administration: {trump_amount}")
    print(f"Democratic National Committee: {dnc_amount}")
    foundation = input("Which foundation would you like to donate to? ")
    amount = input("How much would you like to donate? ")
    
    if foundation == "Bill and Meilinda Gates Foundation":
        gates_foundation_amount = amount
    elif foundation == "spaceX":
        spaceX_amount = amount
    elif foundation == "Trump Administration":
        trump_amount = amount
    elif foundation == "Democratic National Committee":
        dnc = amount
    else:
        print("Error not found")
    
def main():
    intro_message()
    
    print("""
    """)
    
    print_nonprofit()
    
main()