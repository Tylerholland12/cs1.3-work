def compute_sum(n):
    if n == 1: #base case
        return 1 #will return one if the input is given as one
    else: #if the number or (n) value is greater than one then this code will execute
        f = compute_sum(n-1) #an operation that tells the number entered to decrease by one each time
        return n+f #as the number is decreasing, that number will be added to the previous number

print(compute_sum(5)) #will print out the result of 5 + 4 + 3 + 2 + 1


def compute_sum_2(n):
    