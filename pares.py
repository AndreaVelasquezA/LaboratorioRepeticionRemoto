cant=int(input("digite la cantidad de numeros:"))
pares=0
impares=0
for i in range(1, cant+1):
     num=int(input("digite el numero:"))
     if num==0:
        break
     else:
        if num%2==0:
           pares=(pares+1)
        else:
            impares=(impares+1)

print("pares:",pares)
print("impares:",impares)