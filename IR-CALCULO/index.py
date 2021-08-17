from time import sleep
salario = float(input("Digite o seu salário (valor bruto):R$ "))
print("Calculando...")
sleep(2)
if salario <= 1903.98:
    n = salario
if salario >= 1903.99:
    n = salario - (salario * 7.5 / 100)
if salario > 3751.06:
    n = salario - (salario * 15 / 100)
if salario > 3751.06:
    n =  salario - (salario * 22.5 / 100)
else:
    n = salario - (salario * 27.5 / 1000)
print("Seu salário no valor bruto é R${}, com o desconto IRRF o valor líquido será: R${}".format(salario, n))