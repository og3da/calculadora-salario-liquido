# CALCULAR SALÁRIO LÍQUIDO
# VT 6%, VR 20% do valor total do vr, FGTS 8%

def calculo(descontos):
    print("")
    salarioLiquido= salarioBruto-descontos
    print(f'valor descontado dos beneficios + inss = {descontos:.2f}')
    print(f'valor do salário líquido = {salarioLiquido:.2f}')

print("")
print("--- CALCULO DE SALÁRIO LÍQUIDO ---")
print("-- OPÇÕES PARA O PROGRAMA --")
print("-- 1 RECEBO VR + VT --")
print("-- 2 RECEBO apenas VT --")
print("-- 3 RECEBO apenas VR --")
print("descontos: VT - 6%, VR - 20% do valor total do VR, INSS - 8%")
opcao=int(input("Digite a opção: "))
if (opcao==1): #recebe VR + VT
    salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: "))
    vr=float(input("Digite o valor recebido em VR: "))
    descontos= (salarioBruto*0.06)+(vr*0.2)+(salarioBruto*0.08)
    calculo(descontos)

elif (opcao==2): #recebe apenas VT
    salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: "))
    descontos= (salarioBruto*0.06)+(salarioBruto*0.08)
    calculo(descontos)

elif (opcao==3): #recebe apenas VR
    salarioBruto=float(input("DIGITE SEU SALÁRIO BRUTO: "))
    vr=float(input("Digite o valor recebido em VR: "))
    descontos= (vr*0.2)+(salarioBruto*0.08)
    calculo(descontos)