def power(a,b):
    if (b == 0):
        return 1
    else: 
        print("\n" , a , " * " , a**(b-1) )           
        return(a*power(a , b-1) )


n = power(2,3)
print("Ans = " , n)       