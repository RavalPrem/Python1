#using the assert keyword for the debugging (used for small codes only I think)
try:
    age = int(input('Enter age : '))
    assert age > 18,"age should be > 18"
    print('\nvalid age for giving the vote \n')
except AssertionError as e:
    print(f"\nAssertion Error : {e} \n")
