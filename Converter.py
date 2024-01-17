import os

def limpar_console():
    os.system('cls')

continueWhile = True

while continueWhile:
    print('1 - To convert Fahrenheit to Celsius')
    print('2 - To convert Celsius to Fahrenheit')
    print('3 - To convert Miles to Kilometers')
    print('4 - To convert Kilometers to Miles')
    print('5 - To exit')
    option = input()
    
    limpar_console()

    if option == '1':        
        print('Enter the temperature in Fahrenheit to convert to Celsius')
        valor = int(input())
        result = (value - 32) / 1.8
    elif option == '2':
        print('Enter the temperature in Celsius to convert to Fahrenheit')
        value = int(input())
        result = (value * 1.8) + 32
    elif option == '3':
        print('Enter speed in Miles to convert to Kilometers')
        value = int(input())
        result = value / 0.62137
    elif option == '4':
        print('Enter speed in Kilometers to convert to Miles')
        value = int(input())
        result = value * 0.62137
    elif option == '5':
        continueWhile = False
        continue

    print(result)
