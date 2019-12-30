amt = int(input())

if amt > 500:
    a = amt*0.05
    print("5% discount", abs(amt-a))
else:
    print("No discount", amt)


