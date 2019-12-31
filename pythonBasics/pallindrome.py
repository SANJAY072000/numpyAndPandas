a = int(input())
n = a
r = 0
while n > 0:
    b = n % 10
    r = r * 10 + b
    n //= 10

if a == r:
    print("Pallindrome no.")
else:
    print("Not Pallindrome no.")


