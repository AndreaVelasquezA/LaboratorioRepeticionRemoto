num=int(input("digite el numero:"))
cant_div=0
for i in range(1, num):
    if num%i==0:
        cant_div=(cant_div+1)


if cant_div<=2:
   print("es primo")
else:
   print("no es primo")