print("Enter which table you want to view")
maxTable = int(input())

for factor1 in range(1, maxTable + 1, 1):
    for factor2 in range(1, 11, 1):
        print(f'{factor1} x {factor2} = {factor1 * factor2}')
    
    print('\n-----------------\n')