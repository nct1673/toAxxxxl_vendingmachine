# toAxxxxl_vendingmachine

This repository only contain a python file(.py).
The data is not large, so it is not neccessary to create a csv to store the data.

Assumption
1. Customer is limited to buy 1 drinks for each payment.
2. Customer can repeat the purchase many times to purchase multiple drinks.
3. The amount is listed under currency Malaysia Ringgit (RM).
4. The vending machine is only accept for notes RM1, 5, 10, 20, and 50.
5. The vending machine will keep request customer to insert notes until the amount insert is >= the price of item selected.

Logic About The Least Amount of Notes
1. Since all of the items have price less that RM 50, if customer insert a RM50 notes, the machine will start to compute the balance amount.
2. From (1.), we know that the amount inserted can't be more than RM 99, so if the amount inserted >= RM50, we only have to give back one RM 50 notes, there for we have "if balance >= 50, n_50 = 1". 
3. Now, we have balance < RM50. We use math.floor() function to compute the number of RM 20 notes we needs. For example we have balance RM 45, then n_20 = floor(45/20) = floor(2.25) = 2, this means that we need 2 pieces of RM20 notes, the remainder RM5 can't represent by using RM20 notes.
4. For n_10 and n_5 cases, using same idea with (2.) to compute the number of notes needed.
5. If balance < RM5, we use RM1 for the balance since there is no other choices.

Instruction to Use The Vendorint Machine


Variable Used Explanation
1. drinks
2. money_list
3. df
4. price
5. sum
6. n_50 (same meaning for n_20, 10, 5, and 1)


Function Defined
1. main()
2. order()
3. check_money()
4. purchase()
5. num_notes(balance)

   
