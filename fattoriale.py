n=int(input('Inserire il numero: '))
f=1

for i in range(1,n+1):
    f*=i
    
print(n)
n = int(input('Inserire il numero: '))

def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

print ('Il fattoriale è', fattoriale(n))