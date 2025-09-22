
def printpairs(n,m):
    n = 3
    m = 5
    """
    Print pairs of number,the first number varies from 0 to n-1 and each first number is paired with each second number. the second number varies form 0 to m-1
    """
    for i in range(n):
        for j in range(m):
            print( "(",i,j,")" )
print (printpairs(3,5))