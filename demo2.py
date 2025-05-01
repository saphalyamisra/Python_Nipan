# Write a program to reverse an integer without converting to string

def reverse_integer(a):
    op = 0
    while a != 0:
        temp = a%10
        op = op * 10 + temp
        a = a//10
    return op

a = reverse_integer(12345)
print(a)
