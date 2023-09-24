import os, time
#cores
cor_amarela = "\033[93m"
cor_reset = "\033[0m"

#limpa a tela com um comando no terminal (pode ser diferente no windows)
def clear():
    os.system('clear')

# Essa função recebe um dicionário com as escolhas possíveis, caso o input do usuário não exista nas chaves desse dicionário,
# a função exibe uma mensagem de erro, e executa o argumento passado na initialFunction
def waitChoice(choices, initialFunction):
    acao = input('O que eu vou fazer agora? >> ')
    if acao in choices.keys():
        choices[acao]()
    else:
        clear()
        print('você não faz nada...')
        time.sleep(2)
        initialFunction()

# Essa função aqui recebe o dicionário com as escolhas, e exibe elas na tela, a cor é alterada apenas para fins estéticos
def showChoices(choices):
    print('ações: ')
    for choice in choices.keys():
        print(cor_amarela + '- '+choice + cor_reset)

def exists_inv(array, procurada):
    for item in array:
        if item == procurada:
            return True
    return False

#nós ------------------------------------------------------------

def iniciar():
    choices = {"opção 1": selecionou_opcao_01, "opção 2": selecionou_opcao_02}

    clear()

    print("Isso é um nó de história...")
    print("Esses prints são a forma como a sua história é contada")

    showChoices(choices)
    waitChoice(choices, iniciar)

def selecionou_opcao_01():
    choices = {"voltar": iniciar, "opcao 2": selecionou_opcao_02}

    clear()

    print("Voce selecionou a primeira opção")
    
    showChoices(choices)
    waitChoice(choices, selecionou_opcao_01)

def selecionou_opcao_02():
    choices = {"voltar": iniciar}

    clear()

    print("Voce selecionou a segunda opcao")

    showChoices(choices)
    waitChoice(choices, selecionou_opcao_02)

iniciar()
