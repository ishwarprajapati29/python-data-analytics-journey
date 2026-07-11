#String & Numeric values can operate together with*
A,B=2,3
Txt="@"
print(A*Txt*B) 


# String & String can operate with +
a,b="2",3
txt="@"
print((a+txt)*b)

# Numeric values can operate with +, -, *, /, %, ** all arithmetic operstors can be used with numeric values
C,D=2,3
F=4
print(C+D*F)

#Arthmetic expression with integer and float will result in float value
x=5
y=3.14
T=x*y
print(T)

#Result of division operator with two integers will be float value
K,L=10,2
D=K/L
print(D)


#Integer division with float and int will give int displayed as float value
M,N=10,3
R=M//N
print(R, M/N)

#Floor gives closest integer, which is lesser  than or equal to the float value
#Result of (A//B) is same as floor (A/B)
A1,B1=12,5
C1=A1//B1
print(C1)

A2,B2=-12,5
C2=A2//B2
print(C2)

A3,B3=12,-5
C3=A3//B3
print(C3)

#Remainder is negative when denominator is negative
A4,B4=-5,2
C4=A4%B4
print(C4)

A5,B5=5,2
C5=A5%B5
print(C5)

A6,B6=5,-2
C6=A6%B6
print(C6)