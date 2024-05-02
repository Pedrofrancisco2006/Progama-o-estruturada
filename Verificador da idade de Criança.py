    #Idade 
idade = float(input("Digite a sua Idade: "))

    #Classificação idade
if idade <0:
    print("Esta idade não pode ser usada")
elif idade <13:
    print("Esta idade é de uma criança")
elif idade <17:
    print("Esta idade é de um adolecente")
elif idade <59:
    print ("Esta idade é de um adulto")
else: 
    print("Esta idade é de um idoso")
