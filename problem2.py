def toBinary (n):
  ch=""
  m=0
  while (n!=0):
    m=n%2
    ch=str(m)
    n=n//2
  b=""  
  for i in range (len(ch)) : 
      b[i]=ch[len(ch)-i-1]
  return b
while True :
   n=int(input("donner un entier non_negative  "))
   if n>0 :
    break
ch=toBinary(n)
print (n,"en binaire = ",ch)

   
