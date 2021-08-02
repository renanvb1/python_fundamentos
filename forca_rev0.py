# -*- coding utf-8 -*-

# hangman game (jogo da forca)
# programacao orientada a objeto

# import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.palavra=word
        self.erradas=[]
        self.certas=[]

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.palavra:
            if letter not in self.certas:
                self.certas.append(letter)
            else:
                return False
        else:
            if letter not in self.erradas:
                self.erradas.append(letter)
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.erradas) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        aux=''
        for let in self.palavra:
            if let in self.certas:
                aux+=let
            else:
                aux+= '_'
        return aux

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        aux=len(self.erradas)
        print(board[aux])
        print('\n Palavra: ' + self.hide_word())
        print('\n Letras erradas:')
        for let in self.erradas:
            print(let,)

        print('\n Letras certas:')
        for let in self.certas:
            print(let,)




# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras2.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while game.hangman_over() == False:
        game.print_game_status()
        newletter=input('\n Digite uma letra: ')
        game.guess(newletter)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
