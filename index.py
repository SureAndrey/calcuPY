import re
import sys


calculos_feitos = 0


def mostrar_contas_feitas():
    global calculos_feitos
    print(f"\nForam feitos: {calculos_feitos} calculos\n")


def sair():
    mostrar_contas_feitas()
    print("saindo...\n")
    sys.exit()


def ajuda():
    print(
        '\ndigite "sair" para sair \n'
        'digite "ajuda" para ajuda \n'
        'digite "contas" para ver a quantidade de contas feitasn \n'
    )


def calcular(value):
    try:
        if value == "":
            print("Erro: Calculo vazio")
        else:
            print('\n', eval(value), '\n')
            global calculos_feitos
            calculos_feitos += 1
    except SyntaxError:
        if re.findall("^0", value) == ['0']:
            print("\nErro: Zero à esquerda não é permitido\n")
        else:
            # espaco_em_branco = re.split("\s", calculo)
            print("\nErro: conta com varios calculos\n")
            # for i in re.split('\s', value):
            #     print(eval(i))


print("CALCUPY")

while True:
    try:
        calculo = input('> ')

        if calculo == "ajuda" or re.findall("ajuda", calculo) == ['ajuda']:
            ajuda()
        elif calculo == "sair" or re.findall("sair", calculo) == ['sair']:
            sair()
        elif calculo == "contas" or re.findall("contas", calculo) == ['contas']:
            mostrar_contas_feitas()
        elif calculo.isalpha():
            print("\nErro: Letras não são permitidas\n")
        else:
            calcular(calculo)

    except KeyboardInterrupt:
        sair()
