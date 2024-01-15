#List = ["Apfel", "Banane", "Kirsch", "Kirsche", "Avocado"]

#print(max(List))
#print(min(List))


#for max in List:
#    return(List(set(input_list)))

transactions = [{'type':'purchase','amount':5,'date':'14.01.2024'},
               {'type':'sale','amount':8,'date':'15.01.2023'},]

transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']

def list_of(my_key):
    amount_value = [transaction['amount']for transaction in transactions]
print(list_of('amount')) 

def sum_up(my_type):
    amount_values=[transaction['amount']for transaction in transactions if
transaction['type'] == my_type]
    return(sum(amount_values))

income = sum_up('purchase')
expenses = sum_up('sale')
print("income=",income)
print("expenses =",expenses)

if(income>expenses): print("You made money")
else: print("You lost money!")

def find_all(my_key,my_value):
    values = [transactions for transaction in transactions if
transaction[my_key] == my_value]
    return(values)

my_transactions = find_all('date','14.01.2024')
print(my_transactions)
print(len(my_transactions))

#import re 

#def is_valid_date_format(date_string):
#    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}$')
#    return bool(date_pattern.match(date_string))

#my_date = my_transactions[0]['date']
#print(my_transactions[0]['date'])
#print(type(my_date))
#print(is_valid_date_format(my_date))
