from cs50 import get_int

card_number = get_int("Number: ")

# For converting the string of numbers into a list
credit_list = list(str(card_number))

length = len(credit_list)

# For calculating the Luhn's algorithm
total = 0

reversed_credit = credit_list[::-1]
for num in reversed_credit[1:length:2]:
    product = int(num) * 2
    digits = str(product)

# For converting the string of numbers into seperate digits
    for digit in digits:
        total = total + int(digit)

for num in reversed_credit[0:length:2]:

    total = total + int(num)


legit = total % 10

# For checking the type of credit card
no1 = credit_list[0]
no2 = credit_list[1]

# For checking the length
if length >= 13:

    # For checking if it is legit
    if legit == 0:

        # For checking for the AMEX card
        if length == 15 and ((int(no1) == 3 and int(no2) == 4) or (int(no1) == 3 and int(no2) == 7)):
            print("AMEX")

        # For checking for VISA card
        elif (length == 13 or length == 16) and int(no1) == 4:
            print("VISA")

        # For checking for MASTERCARD
        elif length == 16 and (int(no1) == 5 and int(no2) in range(1, 6)):
            print("MASTERCARD")

        else:
            print("INVALID")

    else:
        print("INVALID")
else:
    print("INVALID")
