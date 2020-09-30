#steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
def intro_message():
    print("Welcome to the Non Profit/Charity donater")
    
def print_nonprofit():
    print(gates_foundation)
    print(spaceX)
    print(donald_trump)
    print(dnc)
    print("Which foundation would you like to donate to? ")
    
def main():
    intro_message()
    gates_foundation = "Bill and Melinda Gates Foundation: "
    spaceX = "spaceX: "
    donald_trump = "Trump Administration: "
    dnc = "Democratic National Committee: "
main()