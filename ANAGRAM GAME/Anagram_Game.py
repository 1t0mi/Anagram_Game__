import random
import json
import time
import pygame
import pygame.mixer

pygame.font.init()
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font("game_over.ttf", 70)
font_welcome = pygame.font.Font("GAMERIA.ttf", 45)
font_rules = pygame.font.Font("Gamer_bold.ttf", 45)
font_texto = pygame.font.Font("Game-Font_1.ttf", 45)
font_l = pygame.font.Font("Quinquefive-ALoRM.ttf", 10)
font_k = pygame.font.Font("Quinquefive-ALoRM.ttf", 15)
font_r = pygame.font.Font("Quinquefive-ALoRM.ttf", 15)
font_p = pygame.font.Font("Emulogic-zrEw.ttf", 45)
font_s = pygame.font.Font("game_text.ttf", 45)
font_player = pygame.font.Font("Player1.ttf", 45)

#biblioteca de sons
pygame.mixer.init()

#defenição de som
correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")
music_ambiente = pygame.mixer.Sound("music_ambiente.wav")
GAMEOVER = pygame.mixer.Sound("GAMEOVER.wav")
VICTORY = pygame.mixer.Sound("VICTORY.wav")


# Inicialização do Pygame
pygame.init()

# Inicialização da musica
music_ambiente.play()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
cor_azul_claro = pygame.Color("#6AB3EF")
cor_amarelo = pygame.Color("#FFE86F")
cor_azul_Escuro = pygame.Color("#012153")
cor_vermelho = pygame.Color("#D15844")
cor_verde = pygame.Color("#00FF00")

# Definição das dimensões da janela
WIDTH = 854
HEIGHT = 480

# Definição das teclas
KEY_ENTER = pygame.K_RETURN
KEY_QUIT = pygame.K_ESCAPE
KEY_GIVE_UP = pygame.K_0
KEY_CHANGE_WORD = pygame.K_1

# Definição das configurações do jogo
MAX_ATTEMPTS = 6

# Carregamento do arquivo de dicionário
with open('dictionary.json') as file:
    data = json.load(file)
    dicionario = list(data.items())



# Variáveis do jogo
player_name = ""
score = 0
attempts = 0
hint_given = True
game_over = False

# Inicialização da janela do Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anagram Game")

# Variáveis do campo de entrada da palavra
input_box = pygame.Rect(62, 200, 200, 62)
color_inactive = cor_amarelo
color_active = GREEN
color = color_inactive
active = True

palavra = ""
 
# Escolha aleatória da palavra
sistema = random.choice(dicionario)
palavra = sistema[0].upper().strip()
listap = list(palavra)
random.shuffle(listap)
st_b = ''.join(listap)

hint = sistema[1].upper().strip()

palpite = ""
palpite = palpite.upper().strip()

message_green = ""
message_red = ""


print(palavra)
print(st_b)
print(hint)

correct = "Congratulations! You guessed correctly!"
wrong = "Wrong guess. Try Again!"
game_over_text = "Game over!"
game_over_text += f" The correct word was '{palavra}'."

# Função para processar o palpite do jogador
def process_guess():
    global score, attempts, hint_given, game_over, palpite, st_b, message_green, message_red, sistema, correct, wrong, game_over_text

# Limpar as mensagens antes de processar o novo palpite
    message_green = ""
    message_red = ""
    
    if palpite == palavra:
        score += 5
        attempts = 0
        hint_given = False
        listap = list(palavra)
        random.shuffle(listap)
        st_b = ''.join(listap)
        message_green  = correct
        VICTORY.play()
        hint = sistema[1]
        

        
    else:
        attempts += 1
        if attempts == 1:
            hint = sistema[1] # Obtém a dica do dicionário
            hint_given = True
            print("Hint:", hint)  # Exibe a dica no console
            
        elif attempts < MAX_ATTEMPTS:
            game_over = False
            message_red = wrong
            wrong_sound.play()
            
        else:
            game_over = True
            message_red = game_over_text
            GAMEOVER.play()
            

    


# Função para exibir a mensagem de "Welcome"
def show_welcome_message():
    welcome_text = "WELCOME TO THE ANAGRAMA GAME"
    continue_text = "Press Enter to continue..."

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_ENTER:
                    return

        screen.fill(cor_azul_Escuro)
        welcome_label = font_welcome.render(welcome_text, 1, cor_amarelo)
        continue_label = font_l.render(continue_text, 1, WHITE)

        screen.blit(welcome_label, (WIDTH // 2 - welcome_label.get_width() // 2, HEIGHT // 2 - welcome_label.get_height() // 2))
        screen.blit(continue_label, (WIDTH // 2 - continue_label.get_width() // 2, HEIGHT // 2 + welcome_label.get_height()))

        pygame.display.update()

# Função para exibir as regras e obter o nome do jogador
def show_rules():
    global player_name, correct, wrong, game_over_text

    name_input = ""
    
    rules_text = "RULES:"
    rule_1 = "1. Unscramble the word"
    rule_2 = "2. Press 0 to give up"
    rule_3 = "3. Press 1 to change word"
    rule_4 = "4. Press Esc to quit"
    enter_name_text = "Enter your name:"
    press_enter_text = "Press Enter to start..."

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_ENTER and name_input != "":
                    player_name = name_input
                    
                    print(player_name)
    
                elif event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                else:
                    name_input += event.unicode
                    
        if player_name != "":
            break
            

        screen.fill(cor_azul_Escuro)
        
        rules_label = font_rules.render(rules_text, 1, cor_amarelo)
        rule_1_label = font_texto.render(rule_1, 1, WHITE)
        rule_2_label = font_texto.render(rule_2, 1, WHITE)
        rule_3_label = font_texto.render(rule_3, 1, WHITE)
        rule_4_label = font_texto.render(rule_4, 1, WHITE)
        
        enter_name_label = font_texto.render(enter_name_text, 1, cor_amarelo)
        press_enter_label = font_r.render(press_enter_text, 1, cor_amarelo)
        name_input_label = font_r.render(name_input, 1, WHITE)

        screen.blit(rules_label, (WIDTH // 2 - rules_label.get_width() // 2, 50))
        screen.blit(rule_1_label, (WIDTH // 2 - rule_1_label.get_width() // 2, 100))
        screen.blit(rule_2_label, (WIDTH // 2 - rule_2_label.get_width() // 2, 150))
        screen.blit(rule_3_label, (WIDTH // 2 - rule_3_label.get_width() // 2, 200))
        screen.blit(rule_4_label, (WIDTH // 2 - rule_4_label.get_width() // 2, 250))
        screen.blit(enter_name_label, (WIDTH // 2 - enter_name_label.get_width() // 2, 300))
        screen.blit(name_input_label, (WIDTH // 2 - name_input_label.get_width() // 2, 340))
        screen.blit(press_enter_label, (WIDTH // 2 - press_enter_label.get_width() // 2, 385))

        pygame.display.update()
        


# Loop principal do jogo
def game_loop():
    global game_over, score, attempts, hint_given, start_time, palavra, palpite, st_b, hint, message_green, message_red, sistema, correct, wrong, game_over_text
    
    input_text= ""
    
    # Tempo inicial
    start_time = time.time()
    
    input_box = pygame.Rect(10, 200, 300, 62)
    exit_loop = False
    while not game_over and not exit_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_GIVE_UP:
                    game_over = True
                    exit_loop = True
                    
                elif event.key == KEY_CHANGE_WORD:
                    sistema = random.choice(dicionario)
                    palavra = sistema[0].upper().strip()
                    listap = list(palavra)
                    random.shuffle(listap)
                    st_b = ''.join(listap)
                    attempts = 0
                    hint = sistema[1]
                    
                elif event.key == KEY_QUIT:
                    game_over = True
                elif active and event.key == pygame.K_RETURN:
                    palpite = input_text
                    process_guess()
                    input_text = ""  # Limpar o input_text após processar o palpite

                elif active and event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    
                elif active:
                    input_text += event.unicode
                 
        screen.fill(cor_azul_Escuro)

        time_label = font_r.render(f"Time: {int(time.time() - start_time)}", 1, cor_amarelo)
        score_label = font_r.render(f"Score: {score}", 1, cor_amarelo)
        attempts_label = font_r.render(f"Attempts: {attempts}/{MAX_ATTEMPTS}", 1, cor_amarelo)
        hint_given_label = font_k.render(hint, 1, cor_amarelo)
        input_text_label = font_texto.render( input_text , 1, WHITE)
        input_palavra = font_rules.render( st_b , 1, WHITE)
        message_label = game_over_font.render(message_red, 1, cor_vermelho)
        message_label_2 = game_over_font.render(message_green, 1, cor_verde)
        
        screen.blit(time_label, (WIDTH - time_label.get_width() - 10, 10))
        screen.blit(score_label, (10, 10))
        screen.blit(attempts_label, (10, 50))
        screen.blit(hint_given_label, (10, 150))
        screen.blit(input_palavra, (10, 110))
        screen.blit(message_label, (10, 300))
        screen.blit(message_label_2, (10, 350))
        
        pygame.draw.rect(screen, color, input_box, 2)
        input_text_label = font_rules.render(input_text, 1, WHITE)
        screen.blit(input_text_label, (input_box.x + 10 , input_box.y + 10))
        
        print(input_text)

        pygame.display.update()
        
        if game_over == True :
            
            message_red = game_over_text
            
            message_label_2 = game_over_font.render(message_red, 1, cor_vermelho)
            screen.blit(message_label_2, (10, 300))
            
            pygame.time.delay(4000)
            
            
        pygame.quit
        
show_welcome_message()
show_rules()
game_loop()
pygame.quit()
