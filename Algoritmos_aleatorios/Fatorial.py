# Calcula o fatorial de um numero digitado pelo usuario


# Mude o falor para diferentes resultados
#num = 7

# Pega o numero digitado e faz o fatorial
num = int(input("Coloque um numero: "))

factorial = 1

# Checa se o numero é positivo, negativo ou igual a zero
if num < 0:
   print("Ops, Fatorial não existe para numeros negativos")
elif num == 0:
   print("O Fatorial de 0 é 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("O Fatorial de",num,"é",factorial)