cant=10
positivos=0
negativos=0
ceros=0
for i in range(1, cant+1):
 num=int(input("digite el numero:"))
 if num>0:
      positivos=(positivos+1)
 else:
       if num<0:
          negativos=(negativos+1)
       else:
         if num==0:
           ceros=(ceros+1)


print("positivos:",positivos)
print("negativos",negativos)
print("ceros",ceros)


