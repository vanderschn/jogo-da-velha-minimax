
def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
    print("-" * 5)


def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def jogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    return False

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()

    iniciar = input("Deseja iniciar o jogo? S/N\n")
    print("")

    if iniciar.lstrip()[:1].upper() == "S":
        jogador_atual = "X"
    else:
        jogador_atual = "O"
    
    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
            
        if jogador_atual == "O":
            linha, coluna = melhor_jogada(tabuleiro)
            #print(f"{linha} {coluna}")
        else:
            linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha sua jogada (linha e coluna): ").split())

        if jogada(tabuleiro, linha, coluna, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                return
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Jogada inválida! Tente novamente.")
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")



# IA ######################################

def avaliar_tabuleiro(tabuleiro):
    for jogador in ["X", "O"]:
        if verificar_vitoria(tabuleiro, jogador):
            return 1 if jogador == "O" else -1
    return 0

def movimentos_disponiveis(tab):
    return [(i, j) for i in range(3) for j in range(3) if tab[i][j] == " "]

buscas = 0

def minimax(tabuleiro, profundidade, maximizando):
    pontuacao = avaliar_tabuleiro(tabuleiro)
    global buscas
    buscas += 1
  
    #imprimir_tabuleiro(tabuleiro)
    #if pontuacao != 0 or profundidade == 9:
    #if (pontuacao != 0 or not movimentos_disponiveis(tabuleiro)) and profundidade < 10:
    if pontuacao != 0 or not movimentos_disponiveis(tabuleiro):
        #imprimir_tabuleiro(tabuleiro)
        #print(f"{pontuacao} | {profundidade}")
        #if profundidade == 5 or profundidade == 6:
        #    print(f"{pontuacao} | {profundidade}")
        return pontuacao
    
    #buscas += 1

    if maximizando:
        melhor_valor = float("-inf")
        #melhor_valor = 0
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "O"
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[linha][coluna] = " "
                    melhor_valor = max(melhor_valor, valor)
                    #buscas += 1
                    #melhor_valor += max(melhor_valor, valor)
                    #melhor_valor += valor
        #imprimir_tabuleiro(tabuleiro)
        #print(f"max: {melhor_valor}")
        return melhor_valor
    else:
        melhor_valor = float("inf")
        #melhor_valor = 0
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "X"
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[linha][coluna] = " "
                    melhor_valor = min(melhor_valor, valor)
                    #buscas += 1
                    #melhor_valor += min(melhor_valor, valor)
                    #melhor_valor += valor
        #imprimir_tabuleiro(tabuleiro)
        #print(f"min: {melhor_valor}")
        return melhor_valor
    

def melhor_jogada(tabuleiro):
    melhor_valor = float("-inf")
    melhor_movimento = (-1, -1)
    
    global buscas
    buscas = 0
    
    print("Mov.| Peso")

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "O"
                valor = minimax(tabuleiro, 1, False)
                #imprimir_tabuleiro(tabuleiro)
                tabuleiro[linha][coluna] = " "
                print(f"{linha} {coluna} | {valor}")
                if valor > melhor_valor:
                    melhor_valor = valor
                    #print(f"IF Peso | movimento {melhor_valor} {linha} {coluna}")
                    melhor_movimento = (linha, coluna)
    
    print(f"\n{melhor_movimento[0]} {melhor_movimento[1]} | {melhor_valor} <<<")
    print(f"{buscas} buscas\n")
    return melhor_movimento

# IA FIM #################################

jogo_da_velha()
       