      #Calculadora de juros simples
capital= float(input("Qual o seu capital inicial?: "))
tempo= float(input("Qual será o tempo tde aplicação: "))
taxa= float(input("Digite o valor taxa:"))
juros= (capital*taxa*tempo)/100
print("a sua nova taxa de juros é:",juros,"")
