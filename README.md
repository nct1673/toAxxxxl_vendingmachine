# toAxxxxl_vendingmachine

This repository only contain a python file(.py).
The data is not large, so it is not neccessary to create a csv to store the data.

# Assumption
1. Customer is limited to buy 1 drinks for each payment.
2. Customer can repeat the purchase many times to purchase multiple drinks.
3. The amount is listed under currency Malaysia Ringgit (RM).
4. The vending machine is only accept for notes RM1, 5, 10, 20, and 50.
5. The vending machine will keep request customer to insert notes until the amount inserted is >= the price of item selected.

# Logic About The Least Amount of Notes
1. Since all of the items have price less that RM 50, if customer insert a RM50 notes, the machine will start to compute the balance amount.
2. From (1.), we know that the amount inserted can't be more than RM 99, so if the amount inserted >= RM50, we only have to give back one RM 50 notes, there for we have "if balance >= 50, n_50 = 1". 
3. Now, we have balance < RM50. We use math.floor() function to compute the number of RM 20 notes we needs. For example we have balance RM 45, then n_20 = floor(45/20) = floor(2.25) = 2, this means that we need 2 pieces of RM20 notes, the remainder RM5 can't represent by using RM20 notes.
4. For n_10 and n_5 cases, using same idea with (2.) to compute the number of notes needed.
5. If balance < RM5, we use RM1 for the balance since there is no other choices.

# Instruction to Use The Vendoring Machine
1. When run the code, the system will show the ID, drinks, and price for each items.
2. You have to select the drinks by enter the ID of the drinks.
3. The system will show the details of drinks that you selected, and also the price you have to pay.
4. The system will show the amount that you have insert, please enter the amount for payment.
5. If you enter an invalid amount, the system will show "invalid" and you have to re-enter the amount.
6. Once you have insert enough money, the system will compute the balance and also the number of notes that have least number of notes.
7. The details of notes will be shown.

# Variable Used and Its Explanation

| Variable Name | Variable Type | Description |
| ------------- | ------------- | ------------- |
| drinks  | dictionary  | Details of each item, including ID, drinks name, and price |
| money_list  | list  | A list of notes amount that machine accepted |
| df  | data frame  | Convert drinks from dictionary to data frame so that we can use pandas library later |
| price  | integer  | The price of the drinks that selected by customer |
| insert_sum  | integer  | The total amount of money that inserted by customer |
| n_50  | integer  | The number of notes RM 50 needed in the balance (Same meaning for variables n_20, n_10, n_5, and n_1) |
| balance_table  | data frame  | The number of notes needed for each amount, this table will show to customer |
| balance_copy  | integer  | A copy of the balance amount, the variable balance will be updated when computing the number of notes needed, this variable used to show the amount of balance to customer |


# Function Defined
   
| Function Name |  Description |
| ------------- |  ------------- |
| main() | The main function to run the vendoring machine |   
| order() | Request customer to enter the ID of drinks selected, and show the details of drinks selected |
| check_money(x) | Verify that the amount enter by customer, exp: RM2 is invalid but RM5 is valid |
| purchase() | Request customer to insert money, and compute the balance that need to give back to customer |
| num_notes(balance) | Compute the number of notes for each amount of notes, so that the number of notes is least |
