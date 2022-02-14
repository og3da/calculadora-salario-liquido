# CALCULAR SALÁRIO LÍQUIDO
# VT 6%, VR 20% do valor total do vr, FGTS 8%
import os
sair=1
def continuarOUsair():
    print("")
    global sair
    sair=int(input(f"DIGITE 1 - para continuar \nDIGITE 2 - para sair: "))
    if sair==2:
        sair=2
    else:
        os.system("cls")

def calculo(descontos):
    print("")
    salarioLiquido= salarioBruto-descontos
    print(f'valor descontado dos beneficios + inss = R${descontos:.2f}')
    print(f'valor do salário líquido = R${salarioLiquido:.2f}')
    print('-' *20)
    recebido(salarioLiquido)

def recebido(sal):
    print("")
    global sair
    continuar=int(input(f"DIGITE 1 - se deseja saber o valor líquido recebido por dia \nDIGITE 2 - para finalizar: "))
    if (continuar==1):
        escala=int(input(f"\nDIGITE SUA ESCALA: \n 1 - 6x1 \n 2 - 5x2: "))
        if (escala==1):
            dia= sal/26
            print(f'valor recebido por dia= R${dia:.2f}')
            continuarOUsair()
        elif (escala==2 or 'DIGITE UMA OPÇÃO VÁLIDA'):
            dia= sal/22
            print(f'valor recebido por dia= R${dia:.2f}')
            continuarOUsair()

    elif (continuar==2 or 'DIGITE UMA OPÇÃO VÁLIDA'):
        sair=2

while sair==1:
    try:
        print("")
        print("--- CALCULO DE SALÁRIO LÍQUIDO ---")
        print("-- OPÇÕES PARA O PROGRAMA --")
        print("-- 1 RECEBO VR + VT --")
        print("-- 2 RECEBO apenas VT --")
        print("-- 3 RECEBO apenas VR --")
        print("descontos: VT - 6%, VR - 20% do valor total do VR, INSS - 8%")
        opcao=int(input("Digite a opção: "))
        if (opcao==1): #recebe VR + VT
            salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: R$"))
            vr=float(input("Digite o valor recebido em VR: R$"))
            descontos= (salarioBruto*0.06)+(vr*0.2)+(salarioBruto*0.08)
            calculo(descontos)

        elif (opcao==2): #recebe apenas VT
            salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: R$"))
            descontos= (salarioBruto*0.06)+(salarioBruto*0.08)
            calculo(descontos)

        elif (opcao==3): #recebe apenas VR
            salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: R$"))
            vr=float(input("Digite o valor recebido em VR: R$"))
            descontos= (vr*0.2)+(salarioBruto*0.08)
            calculo(descontos)
    except:
        print("Digite uma opção válida!")
        continuarOUsair()