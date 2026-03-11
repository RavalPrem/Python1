#try with else
try:
    a = int(input("Enter num : "))
    print(f'\na -> {a}')
except Exception as e:
    print(f'\nError -> {e} \n')
else:
    print(f'\nNothing goes wrong \n')
finally: #always Executes
    print('\nThe finally block that always executes even if error occured or not\n')

