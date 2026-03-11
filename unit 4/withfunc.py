def checkAge(age):
    try:
        if age > 18:
            print('\nValid age for giving vote \n')
        else:
            print('\nNot a valid age for giving vote \n')
    except:
        print('\nThe age error occured \n')



age = int(input('Enter age : '))
checkAge(age)

# try:
#     age = int(input('Enter age : '))
#     checkAge(age)
# except:
#     print('\nInvalid type error \n')