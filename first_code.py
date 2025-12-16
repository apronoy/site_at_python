print('A canculator app')



num1=float(input('Enter 1st num:'))
num2=float(input('Enter 2nd num :'))

print('1 . Add ')
print('2 . Subtract')
print('3 . Multiply')
print('4 . Divide')

choice=input('Choose an option : ')

if choice=='1':
    print('Sum of two Numbers is :',num1+num2)
elif choice=='2':
    print('Subtraction of two Number :',num2-num1)
elif choice == '3':
    print('Multiply is :',num1*num2)
elif choice =='4':
    print('Division is :',num2/num1)

