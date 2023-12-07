#Normal Formatting in numbers
print("Hello {1}{0}".format('!', 'world'))

#repeatitive formatting in numbers
print("Hello {1} {1} {1} {1} {1} {0}{0}".format('!', 'world')) 

#repeatitive formatting in vars
print("Hello {w} {w} {w} {w} {w} {e}{e}".format(e='!', w='world'))

#number formatting
#Using only 2 numbers after the point (.)
result = 12.67490867438967
print("Hello {N:1.2f}".format(N = result)) 





