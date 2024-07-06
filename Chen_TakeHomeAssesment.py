import pandas as pd
import math
from tabulate import tabulate


drinks = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Drink': ['Mineral 500ml', 'Coke 500ml', 'Pepsi 500ml', '100 Plus 1L', 'Mineral 1.5L', 'Teh O Ais', 'Kopi Ais', 'Pepsi 2L', 'Coke 3L'],
    'Price': [1, 2, 2, 3, 3, 5, 5, 6, 8]}

money_list = [1, 5, 10, 20, 50]
df = pd.DataFrame(drinks)




def order():
    global price
    print(df.to_string(index=False))
    id = int(input("Enter the ID that you want to purchase (make sure that you enter an integer): "))
    cart = df[df["ID"] == id]
    price = cart.iloc[0]['Price']
    print("Here is the drinks you selected:")
    print(cart.to_string(index=False))
    print("Please insert the money:")
    print("You should pay RM" + str(price))


def check_money(x):
    global money_list
    if x in money_list:
        return True
    else:
        return False


def purchase():
    repeat = True
    global insert_sum
    while repeat == True:
        print("You have insert RM" + str(insert_sum))
        cash = int(input("Please select the notes that you want to insert (We only accept RM1, 5, 10, 20, 50): "))
        if check_money(cash) == False:
            cash = 0
            print(".")
            print("You have entered an invalid amount, please enter a valid amount.")

        insert_sum += cash
        if insert_sum >= price:
            repeat = False

def num_notes(balance):
    global n_50, n_20, n_10, n_5, n_1, balance_table, balance_copy
    while balance != 0:
        balance_copy = balance
        if balance >= 50:
            n_50 = 1
            balance = balance -  50

        if balance >= 20:
            n_20 = math.floor(balance/20)
            balance = balance - n_20 * 20

        if balance >= 10:
            n_10 = 1
            balance = balance - 10

        if balance >= 5:
            n_5 = 1
            balance = balance - 5

        if balance >= 1:
            n_1 = balance
            balance = 0

    num = [n_50, n_20, n_10, n_5, n_1]

    balance_table = {
        'Notes': ['RM50', 'RM20', 'RM10', 'RM5', 'RM1'],
        'Pieces': [n_50, n_20, n_10, n_5, n_1]
    }

    balance_table = pd.DataFrame(balance_table)
    return num





def main():
    global insert_sum, n_50, n_20, n_10, n_5, n_1, price, balance_table, balance_copy
    insert_sum = 0
    (n_50, n_20, n_10, n_5, n_1) = (0, 0, 0, 0, 0)
    price = 0
    order()

    purchase()

    balance = insert_sum - price
    num_notes(balance)

    print(tabulate(balance_table, headers = 'keys', tablefmt= 'psql'))
    print("Please collect your balance RM" + str(balance_copy) + ", Thank you !")



main()





