numero = float(input('Digite um numero: '))
if numero  > 0  and numero % 2 == 0 :
    print("Positivo e Par")
elif numero > 0 and numero % 3 == 0 :   
    print("Positivo e Multiplo de três")
elif numero < 0 and numero % 2 != 0:
    print("Impar e negativo")    
elif numero == 0:
    print("Zero")
else:
    print-("Este numero não está relacionado com tais dados descritos a cima")         
    
