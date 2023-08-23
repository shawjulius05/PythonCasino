import random

# Constants for the slot machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# The amount of symbols in the slot machine
symbol_amount = {
    "Gold Coin": 2,
    "Berry": 4,
    "Cherry": 6,
    "Smile": 8
}

# The value of the symbols in the slot machine
symbol_value = {
    "Gold Coin": 8,
    "Berry": 4,
    "Cherry": 2,
    "Smile": 1
}


# Function to check the amount of winnings a person has after spinning the machine
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # Loops through the first line of every row and checks the symbol
    for line in range(lines):
        symbol = columns[0][line]
        # Loops through each of the columns to see if the symbol matches the first one in the row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        # If the entire row has the same symbol the winnings are awarded
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Prompts the user to see how much they want to deposit and then gets that value as a variable
def deposit():
    while True:
        amount = input("How much do you want to put in? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount


# Asks the user how many lines they are betting on and returns that as a variable
def number_lines():
    while True:
        lines = input("Enter amount of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number must be a valid number of lines")
        else:
            print("Enter a number")
    return lines


# Asks the user how much they want to bet and then returns the bet amount as a variable
def get_bet():
    while True:
        bet_amount = input("How much do you want to bet? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number")
    return bet_amount


# Randomly selects slot values from the symbols table and returns them in a nested array
def slots_spin(rows, cols, symbols):
    all_symbols = []
    # Loops through the symbol_amount list and puts the symbol name in variable symbol and the number in symbol_number
    for symbol, symbol_number in symbols.items():
        # For each symbol repeat the process symbol_number times and add it to the all_symbol list
        for _ in range(symbol_number):
            all_symbols.append(symbol)

    columns = []
    # Loop through every column and make a copy of the all_symbols list
    for _ in range(cols):
        column = []
        copy_symbols = all_symbols[:]
        # Loop through all rows and remove one of the symbols randomly selected from the list and add value to column
        for _ in range(rows):
            value = random.choice(copy_symbols)
            copy_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# Prints the slot machine rows out in the terminal
def print_slot_machine(columns):
    # Loops for every element in the first column (or every row basically)
    for row in range(len(columns[0])):
        # Loops for every column and indexes every time it loops, also prints the slots
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")

        print()


# function that plays the slots game on the terminal
def slots(balance):
    lines = number_lines()
    # Calculates the total bet and then makes sure you don't overdraw your balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough, your balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines}. Your total bet is ${total_bet}")
    spin = slots_spin(ROWS, COLS, symbol_amount)
    print_slot_machine(spin)
    winnings, winning_lines = check_winnings(spin, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += slots(balance)

    print(f"You left with ${balance}")


main()
