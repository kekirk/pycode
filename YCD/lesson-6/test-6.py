a = int(input("请输入数字："))
i = 2
is_prime = True
while i < a:
    if a%i == 0:
        is_prime = False
    i += 1
if is_prime:
    print(a,"is Prime Number.")
else:
    print(a,"is NOT Prime Number.")

i=0
while i<5:
    print("*")
    i+=1