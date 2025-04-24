import os
os.system("cls || clear")

login = []
usuario_salvo = input("Crie seu login (nome): ").upper()
login.append(usuario_salvo)


senha_mestre = []
senha_salvar = input("Crie sua senha: ").upper()
senha_mestre.append(senha_salvar) 

os.system("cls || clear")

salario = 0

def calcular_inss(salario):

    if salario <= 1320.00:
       desconto = salario * 0.075

    elif salario > 1320.00 or salario <= 2571.29:
        desconto = salario * 0.09

    elif salario > 2571.29 or salario <= 3856.94:
        desconto = salario * 0.12

    elif salario > 3856.94 or salario <= 7507.49:
        desconto = salario * 0.14

    else:
        desconto = 1051.05

    return min(desconto,1051.05)


def calcular_irrf(salario,dependentes):
    descontar = dependentes * 189.59
    base = salario - descontar

    if base <= 2112.00:
        return 0.0
    
    elif base > 2112.00 or base <= 2826.65:
        return base * 0.075
    
    elif base > 2826.65 or base <= 3544.00:
        return base * 0.15

    elif base > 3544.00 or base <= 4256.00:
        return base * 0.225

    else:

        return base * 0.275
    
def calcular_vale(salario,quer_vale):

    return salario * 0.06 if quer_vale else 0.0

def calcular_refeicao(valor):
    return valor * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00



print("===Folha de pagamento===")

matricula= input("\n:Digite seu login: ").upper()
senha = input("\nDigite sua senha: ").upper()




 
     

if matricula == usuario_salvo and senha == senha_salvar:

    print("\nAcesso autorizado!")



    salario_base = (float(input("\nDigite seu salario base(R$): "))) 
    vale_transporte = input("Deseja receber vale transporte (s/n)?: ").strip().lower() == "s"
    vale_refeicao = float(input("Qual o valor do vale refeição fornecido pela empresa(R$):"))
    dependentes = 1

    desconto_inss = calcular_inss(salario_base)

    desconto_irrf = calcular_irrf(salario_base,dependentes)

    desconto_transporte = calcular_vale(salario_base,vale_transporte)

    desconto_refeicao = calcular_refeicao(vale_refeicao)

    desconto_saude = calcular_plano_saude(dependentes)

    total_descontos = ( desconto_inss + desconto_irrf + desconto_transporte + desconto_refeicao + desconto_saude)

    salario_liquido = salario_base - total_descontos

    print(f"Salario Base: R${salario_base:.2f} ")
    print(f"Numero de Dependentes: {dependentes} ")
    print(f"Desconto INSS: R${desconto_inss:.2f} ")
    print(f"Desconto IRRF: R${desconto_irrf:.2f} ")
    print(f"Desconto Transporte: R${desconto_transporte:.2f} ")
    print(f"Desconto Refeição: R${desconto_refeicao:.2f} ")
    print(f"Desconto Plano de Saude: R${desconto_saude:.2f} ")
    print(f"Salario Liquido: R${salario_liquido:.2f} ")




else:
  
 
  print("\nLogin ou Senha invalidos, tente novamente!")
     
 

 






     


       




        



















































                      
    
     




































































