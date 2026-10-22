#just a program that does basic mathematics
a=int(input('enter first number '))
b=int(input('enter second number '))
op=input('enter mathematical operation to perform:+,-,*,/,%,// ')
match op:
    case '+':
        print("addition of the numbers, " ,a+b)
    case '-':
        print("subtraction of the numbers, " ,a-b)
    case '*':
        print("multiplication of the numbers, " ,a*b)
    case '/':
        print("division of the numbers, quotient=  " ,a/b)
    case '%':
        print("division of the numbers, remainder=  " ,a%b)
    case '//':
        print("division of the numbers, whole number quotient=  " ,a//b)
