import os, time, random

#cores
cor_amarela = "\033[93m"
cor_reset = "\033[0m"

#variaveis de personagem

inventario = []


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
        time.sleep(1)
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

# Funções de fim de jogo

def gameover():
    print('Fim de jogo, você perdeu!')

def youwin():
    print('fim de jogo, você conseguiu fugir')


#historia nodes

# Cada função é um "nó" que conta parte da história, todas essas funções devem ter o dicionário com as opções de escolha para o jogador, esse dicionário
# serve para permitir que o jogador navege entre os nós da história

def inicio():
    choices = { "levantar":levantou }
    clear()

    print('Eu acordei em uma cama desconhecida, o quarto não parece meu, algo está errado...')

    showChoices(choices)
    waitChoice(choices, inicio)

def levantou():
    choices = {"ligar televisão": ligou_tv, "abrir gaveta": abriu_gaveta, "abrir porta": abriu_porta}
    clear()

    #condicoes
    if exists_inv(inventario, "chave"):
        del choices["abrir gaveta"]

    print('Eu me levanto, percebendo que o quarto realmente não é meu...')
    print('ele está bastante limpo, além disso, posso ver uma escrivaninha com uma gaveta, uma televisão antiga e a porta que me leva para fora do quarto...')
    
    showChoices(choices)
    waitChoice(choices, levantou)

def abriu_gaveta():
    choices = {"forçar de novo": abriu_gaveta, "desistir":levantou}
    num = random.randint(1,3)
    clear()

    if num == 1:
        print('Eu tentei abrir a gaveta, mas ela não parece abrir, é como se estivesse presa...')
    elif num == 2:
        print('eu forcei a gaveta, ela parece estar um pouco solta, mas não abre.... talvez se eu tentar de novo...')
    elif num == 3:
        print('Consegui! Abri a gaveta, dentro dela tinha apenas uma chave, será que é a chave da porta? por que alguém colocaria só uma chave aqui?')
        inventario.append("chave")
        del choices["forçar de novo"]

    showChoices(choices)
    waitChoice(choices,abriu_gaveta)

def ligou_tv():
    choices = {"desistir":levantou}
    clear()
    print('A televisão parece estar quebrada...')
    showChoices(choices)
    waitChoice(choices, ligou_tv)

def abriu_porta():
    choices = {"tentar arrombar":arrombar_porta, "desistir":levantou}
    if "chave" in inventario:
        choices["usar chave"] = usou_chave
    
    clear()
    print('Eu tento abrir a porta, mas ela parece estar trancada...')
    showChoices(choices)
    waitChoice(choices, abriu_porta)

def arrombar_porta():
    choices = {"tentar de novo":arrombar_porta, "desistir":abriu_porta}
    clear()

    print("Eu dei um chute na porta, mas aparentemente nada aconteceu...")

    showChoices(choices)
    waitChoice(choices,arrombar_porta)

def usou_chave():
    choices = {"descer devagar":desceu_devagar, "descer correndo":desceu_correndo}

    clear()

    print('Eu usei a chave que encontrei na gaveta, a porta abriu sem problemas, na minha frente tem uma escada que leva para o andar de baixo...')
    print('estou ouvindo movimento lá em baixo, se eu descer correndo, posso ser ouvido, se eu descer devagar, talvez me peguem fugindo, estou indeciso...')

    showChoices(choices)
    waitChoice(choices, usou_chave)

def desceu_correndo():
    choices = {"fugir pela porta":fugiu_porta, "procurar esconderijo": procurou_esconderijo}
    clear()

    print('eu desci as escadas correndo, ao chegar lá em baixo, me deparei com a porta da frente aberta, ouço alguns barulhos vindos lá de fora, mas acho que consigo fugir')

    showChoices(choices)
    waitChoice(choices, desceu_correndo)

def fugiu_porta():
    clear()

    print('Eu corro para fora da  da casa, ouço passos atrás de mim, mas pela minha velocidade, esses passos ficam cada vez mais distantes')
    print('Eu consegui, escapei desse lugar')

    youwin()

def procurou_esconderijo():
    choices = {"esperar oportunidade": esperou_oportunidade, "desistir e fugir": desistiu_e_fugiu}
    clear()

    print('Eu aproveito que não tem ninguém perto para procurar um esconderijo.')
    print('Encontrei um armário vazio, entrei dentro dele e fiquei ouvindo tudo em volta')

    showChoices(choices)
    waitChoice(choices, procurou_esconderijo)

def esperou_oportunidade():
    chance = random.randint(1,3)
    choices = {"esperar":esperou_oportunidade, "sair do esconderijo": fugiu_porta}
    clear()

    if chance == 1:
        print("Ouço passos muito perto, não parece ser uma boa ideia sair agora")
        choices["sair do esconderijo"] = fugiu_e_morreu
    elif chance == 2:
        print("Os passos estão próximos, mas não tão perto...")
        choices["sair do esconderijo"] = desistiu_e_fugiu
    elif chance == 3:
        print("Não ouço nada por perto, parece seguro...")

    showChoices(choices)
    waitChoice(choices,esperou_oportunidade)

def fugiu_e_morreu():
    clear()

    print("No momento que eu pulei para fora do esconderijo, alguma coisa me atingiu na perna, e eu caí no chão agonizando de dor...")
    print("Tudo que consegui ver, foi o homem mascarado com seu machado, acertando a minha cabeça...")
    print('É o meu fim.')

    gameover()

    

def desistiu_e_fugiu():
    clear()

    print('Esqueça o esconderijo, eu vou sair correndo daqui, não tenho tempo para pensar sobre isso...')
    print('No instante que eu passei pela porta, alguma coisa me agarrou pelo pescoço...')
    print('Só pude ver seu rosto mascarado, antes de seu machado entrar na minha barriga...')
    print('É o meu fim.')

    gameover()



def desceu_devagar():

    choices = {"voltar para o quarto":voltou_quarto, "descer correndo": terminou_correndo, "ficar parado":ficou_parado}

    clear()

    print('Eu estou descendo a escada bem devagar, prestando atenção nos barulhos lá em baixo...')
    print('Acabei de ouvir o som de uma porta fechando, agora, ouço passos que estão vindo na minha direção...')

    showChoices(choices)
    waitChoice(choices, desceu_devagar)

def ficou_parado():
    choices = {"voltar para o quarto": voltou_quarto, "continuar descendo": terminou_correndo}
    clear()

    print('Eu paralisei no meio da escada...')
    print('Não tenho certeza se foi alguma obra divina, mas ninguém veio até mim ainda...')
    print('Talvez haja tempo de voltar para o quarto, ou continuar descendo')

    showChoices(choices)
    waitChoice(choices,ficou_parado)

def terminou_correndo():
    clear()

    print('Eu terminei de descer as escadas correndo, mas o que eu encontrei lá em baixo não foi nada bom...')
    print('O sujeito mascarado estava me esperando com o machado na mão, e sem pensar duas vezes, me acertou com o machado...')
    print('É o meu fim...')

    gameover()

def voltou_quarto():
    choices = {"fechar a porta": fechou_porta, "me esconder": se_escondeu}
    clear()

    print('Voltei correndo para o quarto, ouço passos pesados vindo atrás de mim, tenho que pensar rápido')

    showChoices(choices)
    waitChoice(choices, voltou_quarto)

def se_escondeu():
    clear()

    print('Eu pulei para debaixo da cama, mas não fui rápido o bastante, alguma coisa me segurou antes que eu pudesse me esconder...')
    print('Não tive tempo de sequer olhar para o rosto da criatura, tudo que senti foi uma machadada em minhas costas... é o meu fim.')

    gameover()

def fechou_porta():
    choices = {"continuar segurando": continuou_segurando, "abrir porta":reabriu_porta}
    clear()

    print('Fechei a porta com tudo e segurei ela lá, alguém do outro lado está batendo muito forte, na tentativa de derrubar a porta...')

    showChoices(choices)
    waitChoice(choices, fechou_porta)

def continuou_segurando():
    choices = {"reabrir porta": abriu_porta}
    clear()

    print('Eu segurei a porta com toda a minha força, algumas batidas depois, seja lá o que estava do outro lado desistiu de tentar abrir...')
    print('Parece que aquela coisa voltou lá para baixo...')

    showChoices(choices)
    waitChoice(choices,continuou_segurando)

def reabriu_porta():
    clear()

    print('Eu levemente soltei a porta, e isso foi suficiente para a porta cair por cima de mim')
    print('A última coisa que eu consegui ver, foi a lâmina afiada de um machado, é o meu fim.')

    gameover()




inicio()
