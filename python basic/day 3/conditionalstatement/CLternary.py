#Clever IF / Ternary Operator
# <var> =(false_val, true_value)[condition]
#example one
age = int(input("age : "))
vote = ("yes", "no") [age >= 18]


#example two
sal = float(input("salary : "))
tax = sal*(0.1, 0.2) [sal >= 50000]
print(tax)