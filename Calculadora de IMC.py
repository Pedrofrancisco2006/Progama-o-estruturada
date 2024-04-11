     #Calculadora do IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura*altura)

    #Classificação do IMC
if imc < 18.5:
   print("Magreza")
elif imc <= 24.9:
   print("Saudavel")
elif imc <=29.9:
   print("Sobrepeso")
elif imc <= 34.9:
   print("Obesidade Grau I")  
elif imc <= 39.9:
   print("Obesidade Grau II")
else:
   print("Obesidade Grau III")   

