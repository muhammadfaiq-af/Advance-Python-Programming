def sample(n):
    if(n == 1 or n == 0):
        return 1
    return n * sample(n-1)
    
print(sample(int(input("Enter The Number"))))

 