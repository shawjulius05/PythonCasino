import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_amount = {
    "Gold Coin": 2,
    "Berry": 4,
    "Cherry": 6,
    "Smile": 8
}


symbol_value = {
    "Gold Coin": 8,
    "Berry": 4,
    "Cherry": 2,
    "Smile": 1
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def deposit():
    while True:
        amount = input("How much do you want to put in? $" )
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount


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


def slots_spin(rows, cols, symbols):
    all_symbols = []
    # Loop through the symbols dictionary
    for symbol, symbol_amount in symbols.items():
        # For each symbol repeat the process 'symbol_amount' times
        for _ in range(symbol_amount):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        copy_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(copy_symbols)
            copy_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")

        print()



def slots(balance):
    lines = number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough, your balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines}. Your total bet is ${total_bet}")
    slots = slots_spin(ROWS, COLS, symbol_amount)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += slots(balance)

    print(f"You left with ${balance}")


main()