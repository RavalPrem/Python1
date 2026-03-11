#file handling in try except
try:
    f = open("f1.txt ","r")
    # f1 = open("f12.txt ","r") #uncomment to see the error
    content = f.read()
    print(f'\nThe content of the file \n {content} \n')

    f.close()
except FileNotFoundError as f:
    print(f'\nError -> {f} \n')

try:
    f = open("f1.txt","w")
    f.write('Here are some text \nDo not write anything in the code')
    print('\nThe write operation done')
    f.close() 
except Exception as e:
    print(f'\nError -> {e}')

#file handling using the with open
print('\n\nThe down below using the with keyword\n')
try:
    with open("f2.txt","r") as f:
        print(f.read())
except:
    print(f'\nThe error occured \n')