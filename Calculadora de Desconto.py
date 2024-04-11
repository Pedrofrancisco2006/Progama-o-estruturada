#Calculadora de desconto
preco = float(input("Digite o Preço: "))
desconto = float(input("Digite seu desconto: "))
formula = preco-(preco*desconto/100)
print("Seu preço com desconto é de",formula, ".")
