print("Bom dia, você acaba de entrar no verificador de ano bissexto")
 
    #Verificador de ano bissexto
ano = int(input("Digite um ano "))

        #Possiveis Casos
if (ano % 4==0 and ano% 100!=0) or (ano%400==0):
    print("É um ano bissexto")
else:
    print("Não é ano bissexto")
