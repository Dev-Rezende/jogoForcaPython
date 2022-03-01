"""
 Jogo da forca criado por Gustavo Caris Rezende utilizando a linguagem python, sem o uso de bibliotecas
ou módulos adicionais, somente com um conhecimento básico obtido no curso citado abaixo.
 Projeto feito com o intuito de testar os conhecimentos e me desafiar a buscar por soluções encontrados
durante o desenvolvimento.
 GitHub profile: https://github.com/Dev-Rezende
 Curso: https://www.udemy.com/course/python-3-do-zero-ao-avancado/  --> Aula 40
 Python version: 3.8.10
"""

# Font Color
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
lightYellow = "\033[1;93m"
white = "\033[1;97m"
resetFontColor = "\033[0;0m"

# Pré definições do layout
meioLayout = 40
tamanhoLayout = (meioLayout * 2) + 1
separador = "#-" * meioLayout
separador += "#"
separador = cyan + separador + resetFontColor
separadorSecundario = cyan + ("-" * tamanhoLayout) + resetFontColor
mainTitle = "JOGO DA FORCA"
limpaTela = "\n" * 50
limpaTela += red + " " * 35 + "NÃO VALE ESPIAR\n" + resetFontColor
limpaTela += "\n" * 50

# Jogar novamente
dnv = "S"
while dnv == "S":

    # Regras
    regras = "REGRAS DO JOGO DA FORCA"
    print(separador)
    print(green + "\n" + mainTitle.center(tamanhoLayout) + "\n")
    print(separador)
    print(magenta + regras.center(tamanhoLayout) + resetFontColor)
    print(separadorSecundario)
    print(lightYellow +
          "\n-> DIGITE UMA PALAVRA PARA OUTRA PESSOA TENTAR ADIVINHAR\n"
          "-> O JOGADOR QUE ADIVINHAR POSSUÍ VIDAS, ONDE EM CADA ERRO UMA VIDA É PERDIDA\n"
          "-> OS ESPAÇOS DA PALAVRA SERÃO SUBSTÍTUIDOS POR '*'\n"
          "-> TODAS AS LETRAS SÃO CONVERTIDAS PARA CAIXA ALTA\n"
          "-> O SISTEMA CONVERTE AS LETRAS INSERIDAS EM CAIXA BAIXA\n"
          f"{blue}-> PLAYER 1 - ESCOLHA A PALAVRA SECRETA\n"
          "-> PLAYER 2 - TENTA ADIVINHAR A PALAVRA SECRETA\n"
          f"{lightYellow}-> A PALAVRA SERCRETA PODE TER NO {red}MÁXIMO 17 CARACTERES{yellow}\n"
          f"-> CADA DIFICULDADE TEM UMA QUANTIA DIFERENTE DE VIDAS\n" + resetFontColor)
    print(separadorSecundario)

    # Input: Dificuldade + Tratamento de erros
    print(lightYellow + "\nSELECIONE A DIFICULDADE:\n"
                        f"     {green}[0] EASY   -> 7 VIDAS{resetFontColor}\n"
                        f"     {cyan}[1] NORMAL ->  5 VIDAS{resetFontColor}\n"
                        f"     {red}[2] HARD   ->  3 VIDAS{lightYellow}\n")
    securityDificult = 0
    while securityDificult == 0:
        dificuldade = input("RES.: ")
        if dificuldade.isdigit():
            dificuldade = int(dificuldade)
            if dificuldade < 3:
                securityDificult = 1
            else:
                print(red + "NÚMERO DIGITADO INVÁLIDO, TENTE NOVAMENTE" + green)
        else:
            print(red + "O VALOR DIGITADO NÃO É UM NÚMERO, TENTE NOVAMENTE" + green)
    lifes = 0
    if dificuldade == 0:
        lifes = 7
    elif dificuldade == 1:
        lifes = 5
    elif dificuldade == 2:
        lifes = 3
    # ERRO 1FD1F1CULT1: O valor inserido na seleção de dificuldade é inválido
    else:
        print("OPS! ENCONTRAMOS UMA INCONSISTÊNCIA!\nCOD.: 1FD1F1CULT1")
        break
    print("\n" + separadorSecundario)

    # Definindo a palavra secreta
    keySecret = 404
    while keySecret == 404:
        palavraSecreta = input(f"{yellow}\nINFORME A PALAVRA SECRETA: ").upper().strip()
        if len(palavraSecreta) == 0:
            print(f"{red}\n" + " " * 18 + f"A PALAVRA PRECISA TER NO MÍNIMO 1 CARACTERE!{resetFontColor}\n")
        elif len(palavraSecreta) > 17:
            print(f"{red}\n" + " " * 19 + f"A PALAVRA PODE TER NO MÁXIMO 17 CARACTERES!{resetFontColor}")
        else:
            keySecret = 0
        print("\n" + separadorSecundario)

    # Centralizar a exibição da lista dentro do layout
    quantidadeCaracteres = len(palavraSecreta)
    espacoTotal = (quantidadeCaracteres + ((quantidadeCaracteres * 2) + ((quantidadeCaracteres - 1) * 2) + 2))
    espacoTotal = tamanhoLayout - espacoTotal
    espacoTotal = " " * round((espacoTotal / 2))

    # Configurando a palavra do visor
    palavraVisor = []  # Visor
    palavraVisorCompleta = []
    palavraSecretaLetras = []  # Letras da palavra secreta sem espaço
    for letra in palavraSecreta:
        if letra == " ":
            palavraVisor.append("*")
        else:
            palavraVisor.append("_")
            palavraSecretaLetras.append(letra)
            palavraVisorCompleta.append(letra)

    # Letras restantes
    letrasRestantes = len(palavraSecretaLetras)

    # The Game
    letrasDig = []
    while lifes > 0 and letrasRestantes > 0:

        # Layout
        print(limpaTela)
        print(separador)
        print(mainTitle.center(tamanhoLayout))
        print(f"VIDAS: {lifes}".center(tamanhoLayout))
        print(separador)
        print(f"{espacoTotal}{palavraVisor}")
        print(separadorSecundario)

        # Input letra + controle de caracteres digitados
        keyLetra = 404
        while keyLetra == 404:
            letra = input(f"{blue}Informe uma letra:{resetFontColor} ").upper().strip()
            if len(letra) > 1:
                print(f"{separadorSecundario}\n" + (" " * 19) +
                      f"{red}INFORME SOMENTE UMA LETRA! TENTE NOVAMENTE!{resetFontColor}\n"
                      f"{separadorSecundario}")
                input(f"\n{yellow}PRESSIONE ENTER PARA CONTINUAR...")
            elif len(letra) <= 0:
                print(f"{separadorSecundario}\n" + (" " * 27) +
                      f"{red}DIGITE PELO MENOS UMA LETRA!\n"
                      f"{separadorSecundario}")
            else:
                # Checagem de letra repetida
                keyRepeat = 0
                for checkLetra in letrasDig:
                    if checkLetra == letra:
                        keyRepeat = 404
                        print(f"{separadorSecundario}\n"
                              f"{red}" + (" " * 32) + f"LETRA JA DIGITADA!\n{separadorSecundario}")
                        input(f"\n{yellow}PRESSIONE ENTER PARA CONTINUAR...\n")
                        break
                keyLetra = 0
                letrasDig.append(letra)

        # Reiniciando execução do bloco se a letra for repetida
        if keyRepeat == 404:
            continue

        # Checando se a letra existe na palavra secreta
        key = 404
        for checkExiste in palavraSecretaLetras:
            if letra == checkExiste:
                letrasRestantes -= 1
                # Alterando o visor
                cont = 0
                for check in palavraSecreta:
                    if letra == check:
                        del (palavraVisor[cont])
                        palavraVisor.insert(cont, check)
                    cont += 1
                    key = 0
        else:
            if key == 404:
                lifes -= 1
                print(f"{red}\n" + " " * 20 + f"A LETRA {letra} NÃO EXISTE NA PALAVRA SECRETA!{resetFontColor}")
                input(f"\n{yellow}PRESSIONE ENTER PARA CONTINUAR...")
                print(separadorSecundario)

    # Definindo vencedor
    else:
        if letrasRestantes <= 0:
            # Win
            print(f"{separadorSecundario}\n" + (" " * 34) +
                  f"{green}PLAYER 1 GANHOU!{yellow}\n" + " " * 31 +
                  f"A PALAVRA SECRETA ERA{white}\n"
                  f"{espacoTotal}  {palavraVisorCompleta}\n"
                  f"{separadorSecundario}")
        elif lifes <= 0:
            # Perdeu
            print((" " * 34) +
                  f"{red}PLAYER 2 GANHOU!\n{yellow}" + " " * 31 +
                  f"A PALAVRA SECRETA ERA{white}\n"
                  f"{espacoTotal}  {palavraVisorCompleta}\n"
                  f"{separadorSecundario}")
        else:
            # ERRO 1FW1N0V3R: Problema na definição de ganhador ou perdedor
            print(f"\n\n\n{red}OPS ALGO DEU ERRADO!Z\n"
                  f"CÓDIGO ERRO: 1FW1N0V3R\n\n\n")

    # Input: Jogar novamente
    keyDNV = 404
    while keyDNV == 404:
        print(f"{yellow}DESEJA JOGAR NOVAMENTE [{green}S{yellow}/{red}N{yellow}]")
        dnv = input(f"{yellow}--> ").upper().strip()
        if len(dnv) == 0:
            print(f"{red}O VALOR INFORMADO NÃO PODE SER NULO!{resetFontColor}")
        elif len(dnv) > 1:
            print(f"{red}INFORME SOMENTE UMA LETRA!{resetFontColor}")
        elif dnv == "S":
            keyDNV = 0
            print(limpaTela)
        elif dnv == "N":
            keyDNV = 0
        else:
            print(f"{red}VALOR INFORMADO INVÁLIDO! TENTE NOVAMENTE{resetFontColor}")

else:
    print(separador)
    print(f"{magenta}\n" + " " * 24 + f"PROGRAMA ENCERRADO! VOLTE SEMPRE!\n{resetFontColor}")
    print(separador)
