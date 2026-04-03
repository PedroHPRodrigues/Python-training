# ============================================
# HANGMAN ART - Artes ASCII para o jogo
# ============================================

# Desenho do boneco em cada estágio do jogo
stages = [
    # estágio 0: jogo começou (forca vazia)
    r'''
       --------
       |      |
       |      
       |    
       |    
       |     
       -
    ''',
    # estágio 1: primeira vida perdida (cabeça)
    r'''
       --------
       |      |
       |      O
       |      
       |    
       |     
       -
    ''',
    # estágio 2: segunda vida perdida (corpo)
    r'''
       --------
       |      |
       |      O
       |      |
       |    
       |     
       -
    ''',
    # estágio 3: terceira vida perdida (braço esquerdo)
    r'''
       --------
       |      |
       |      O
       |     \|
       |    
       |     
       -
    ''',
    # estágio 4: quarta vida perdida (braço direito)
    r'''
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     
       -
    ''',
    # estágio 5: quinta vida perdida (perna esquerda)
    r'''
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / 
       -
    ''',
    # estágio 6: sexta vida perdida (perna direita - GAME OVER)
    r'''
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / \
       -
    '''
]

# Logo do jogo
logo = r'''
    ╔════════════════════════════════════╗
    ║                                    ║
    ║         HANGMAN GAME              ║
    ║                                    ║
    ║  Guess the word before drawing    ║
    ║    the complete hangman!          ║
    ║                                    ║
    ╚════════════════════════════════════╝
'''
