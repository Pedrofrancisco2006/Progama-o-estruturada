    #Verificador de idade 
idade = float(input("Digite a sua Idade: "))
    #Possíveis resultados dependendo da idade
if idade <13:
    print("Esta idade é de uma criança")
elif idade <17:
    print("Esta idade é de um adolecente")
elif idade <59:
    print ("Esta idade é de uma pessoa adulta")
else: 
    print("Esta idade é de uma pessoa mais velha")
