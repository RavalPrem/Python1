#file handling in try except
try:
    f = open("f1.txt ","r")
    # f1 = open("f12.txt ","r") #uncomment to see the error
    content = f.read()
    print(f'\nThe content of the file \n {content} \n')
except FileNotFoundError as f:
    print(f'\nError -> {f} \n')

try:
    f = open("f1.txt","w")
    f.write('Here are some text \nDo not write anything in the code')
    print('\nThe write operation done')
except Exception as e:
    print(f'\nError -> {e}')