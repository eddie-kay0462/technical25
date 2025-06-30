#Iterative approach
# def find_sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum+=i
#     return sum


#recursive approach
# def find_sum(n):
#     if n ==1:
#         return 1
#     return n + find_sum(n-1)


# print(find_sum(6))


def fib(n):
    if n==0 or n==1:
        return n
    #the above short form version of the below 2 lines of code
    #if n==0 return 0 
    #if n==1 return 1
    return fib(n-1) + fib(n-2)

print(fib(4))
