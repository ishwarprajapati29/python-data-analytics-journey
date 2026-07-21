#Single line if / ternary operator
#<var> = <val1> if <condition> else <val2>
food1 = input("food1 : ")
eat = "Yes" if food1 == "cake" else "no"
print(eat)

#<stt1> if <condition> else <stt2>
food2 = input("food2 : ")
print("sweet") if food2 == "cake" or food2 == "icecream" else print("not sweet")