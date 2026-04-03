import wonderwords
from hangman_art import stages, logo
def random_word():
    """
    Bibiloteca que tem funcao de pegar palavra aleatoria
    Retorna sempre em maiusuculas e esta limitado de 4 a 10 letras pra n ficar grandao tbm
    """
    while True:
        word = wonderwords.RandomWord().word().upper()
        # Filtra apenas palavras entre 4 e 10 letras
        if 4 <= len(word) <= 10:
            return word
def blank_word(word, guessed_letters):
    """
    Exibe o painel com as palavras descobertas ou nao pelo player
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display
def game_state(word, guessed_letters, wrong_guesses, lives):
    """
    Exibe o estado do jogo atualizado:
    """
    # Exibe o boneco de acordo com o número de vidas q ele tem
    print(stages[lives])
    # Exibe a palavra
    print("\n" + "=" * 50)
    print("WORD:", blank_word(word, guessed_letters))
    print("=" * 50)
    # Exibe informações sobre o jogo
    print(f"\nCorrect letters: {guessed_letters}")
    print(f"Wrong letters: {wrong_guesses}")
    print(f"\nLives remaining: {lives}/6")
    print("=" * 50) #isso é só p deixar mais bntin

def input_validation(guess, guessed_letters, wrong_guesses):
    """
    debug do input do player, funcao de garantir que ele ta jogando certo
    """
    if len(guess) != 1 or not guess.isalpha():
        print("Please type only ONE valid letter!")
        return False
    
    if guess in guessed_letters or guess in wrong_guesses:
        print(f"You already guessed the letter '{guess}'!")
        return False
    return True

def game():
    # definindo as variaveis do jogo e a interface incial
    word = random_word()
    guessed_letters = []  
    wrong_guesses = []   
    lives = 6               
    
    print(logo)
    # Loop principal - roda enquanto o jogador tiver vidas
    while lives > 0:
        # Exibe o estado atual do jogo
        game_state(word, guessed_letters, wrong_guesses, lives)
         # Verifica condição de vitória
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print("=" * 50)
            print(f"The word was: {word}")
            return True  # Retorna True para indicar vitória
         # Solicita palpite do jogador
        guess = input("\nGuess a letter: ").upper()
        # Valida o palpite
        if not input_validation(guess, guessed_letters, wrong_guesses):
            continue
        # Verifica se a letra está na palavra
        if guess in word:
            guessed_letters.append(guess)
            print(f"Correct! The letter '{guess}' is in the word!")
        else:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"Wrong! The letter '{guess}' is not in the word!")
    
    # Jogo terminou - jogador perdeu (lives == 0)
    print(stages[6])  # Exibe o boneco completo
    print("\n" + "=" * 50)
    print("GAME OVER! YOU LOST!")
    print(f"The word was: {word}")
    print("=" * 50)
    return False  # Retorna False para indicar derrota

def again():
    """
    Função principal que inicia o jogo e oferece a opção de jogar novamente.
    """
    while True:
        result = game()
        # Pergunta se deseja jogar novamente
        play_again = input("\nDo you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("\nThank you for playing! Goodbye!")
            break
# Inicia o jogo
if __name__ == "__main__":
    again()
