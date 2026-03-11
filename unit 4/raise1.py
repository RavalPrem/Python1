#using the raise
print('\nusing the raise keyword in both \n')

try:
    a = [1,2,3,4,5]
    print(f'\nThe 6th num : {a[6]}')
    raise Exception('\nThe index error occured in the list')
except:
    print('\nThe error down below ')
    raise

