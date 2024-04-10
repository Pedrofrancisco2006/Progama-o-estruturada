peso = float(input("digite seu Peso "))
altura = float(input("digite sua Altura "))
imc = peso/(altura*altura)
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
   print("Começe a rezar pra sobreviver")   

