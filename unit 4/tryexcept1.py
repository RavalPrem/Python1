try:
    num = int(input('Enter num : '))
    #if entered character the runtime error occurs so for that the try and except block is there
    print(f'\nthe Num is {num} \n')
except:
    print('\nThe error occured, do not enter characters \n')

#perticular Exception in except 
#divisible by zero

    '''
        Hello world
    '''
try:
    num1 = int(input('Enter num1 : '))
    num2 = int(input('Enter num2 : '))

    ans = num1/num2
    print(f'\nThe answer of {num1} / {num2} = {ans} \n')
except ZeroDivisionError:
    print(f'\nThe ZeroDivisionError occured \n')


#Mutliple except blocks
try:
    a = int(input('Enter number not character : '))
    print(f'\nThe character is : {a} \n')
except TypeError as te: #for know more about the error
    print(f'\nThe type error occured -> {te}\n')
except:
    print('\nThe different error occured\n')


print('\n\nDown below the index error will be occured')

#Write Exception if error we didn't know
try:
    a = [1,2,3,4,5]
    print(f'\n6th number is : {a[6]}')
except Exception as e:
    print(f'\nThe error is : {e}')