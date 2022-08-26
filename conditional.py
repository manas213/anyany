
#Working model of atm machine
total_price = 0
card_type = "visa"
is_same_bank = True
is_expired = False

print("Please insert your card:")
required_amt = int(input("Please enter the amount: "))

def read_card():
    card_details = [1200, True, False]
    total_price = card_details[0]
    is_same_bank = card_details[1]
    is_expired = card_details[2]
    
    if is_expired:
        print("Sorry, this card cannot be accepted here.") 
    else:
        perform_transaction(total_price, is_same_bank)

def perform_transaction(total_price, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge =5
        if required_amt > total_price:
            return "Not enough balance."
        else:
            print(f"Remaining available balance: {total_price-required_amt-charge}")
            return required_amt
    else:
        if required_amt > total_price:
            return "Not enough balance."
        else:
            print(f"Amount withdrawn {required_amt}") 
            print(f"Remaining available balance: {total_price-required_amt}")

read_card()
