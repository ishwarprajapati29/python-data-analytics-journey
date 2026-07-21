
A = int(input("A :  "))
G = input("G : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 200")
elif((A == 3 or A == 4 or G == "G")):
    print("Fee is 300")
elif(A == 5 and G == "M"):
    print("fee is 400")
else:
    print("no fee")


