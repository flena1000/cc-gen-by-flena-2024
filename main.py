import random

# Fixed credits with ANSI escape codes for color
credits = [
    "\033[91m███████╗██╗░░░░░███████╗███╗░░██╗░█████╗░\n",
    "██╔════╝██║░░░░░██╔════╝████╗░██║██╔══██╗\n",
    "█████╗░░██║░░░░░█████╗░░██╔██╗██║███████║\n",
    "██╔══╝░░██║░░░░░██╔══╝░░██║╚████║██╔══██║\n",
    "██║░░░░░███████╗███████╗██║░╚███║██║░░██║\n",
    "╚═╝░░░░░╚══════╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝\033[0m\n",
    "\033[91mThis tool is made by Flena\n",
    "Discord id: flena1000\n",
    "Server Link: https://discord.gg/byteclub\033[0m\n",
]

# Generate expiry date
def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(23, 30)  # Assuming cards valid till 2030
    return f"{month:02d}/{year}"

# Generate CVC number
def generate_cvc():
    return f"{random.randint(100, 999)}"

# Generate credit card numbers based on BIN
def generate_credit_card(bin, count):
    length = 16
    generated_cards = []

    for _ in range(count):
        card_number = [int(x) for x in bin]
        while len(card_number) < (length - 1):
            card_number.append(random.randint(0, 9))

        # Calculate the checksum using Luhn algorithm
        checksum = 0
        card_number.reverse()
        for i, num in enumerate(card_number):
            if i % 2 == 0:
                double = num * 2
                if double > 9:
                    double = double - 9
                checksum += double
            else:
                checksum += num
        card_number.reverse()

        # Determine the last digit
        last_digit = (10 - (checksum % 10)) % 10
        card_number.append(last_digit)

        card_number_str = ''.join(map(str, card_number))
        expiry_date = generate_expiry_date()
        cvc = generate_cvc()
        card_details = f"{card_number_str}|{expiry_date}|{cvc}'"
        generated_cards.append(card_details)
        save_credit_card(card_details)

    print("\033[91mThe generation of CC has been completed (check creditcards.txt for more info)\033[0m")
    print(f"Generated {count} credit card number(s).")

# Save generated credit card details to creditcards.txt
def save_credit_card(card_details):
    with open('creditcard.txt', 'a') as file:
        file.write(f"{card_details}\n")
    print(f"Generated credit card details saved: {card_details}")

# Main function to choose between options
def main():
    print("\033[91mRead the README.md for more information.")
    for line in credits:
        print(line.strip())
    print("\033[0m")
    bin = input("\033[93mEnter the BIN (Bank Identification Number): \033[0m").strip()
    count = int(input("\033[93mEnter the number of credit cards to generate: \033[0m").strip())
    generate_credit_card(bin, count)

if __name__ == "__main__":
    main()
