import pygame
import random
pygame.init()

# Color
white = (255, 150, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

# Game Window 
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("SnakesTheGame")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snake Game", black, 250, 250)
        text_screen("Press Spacebar to  Play", black, 250, 300)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
                    
            if event.type == pygame.QUIT:
                exit_game = True

        pygame.display.update()
        clock.tick(60)

# Game Loop 
def gameloop():
    # Game specific variable
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    fps = 60
        
    snk_list = []
    snk_length = 1
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game Over! press Enter to continue", red,  100, 250)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 2
                        velocity_y = 0
            
                    if event.key == pygame.K_LEFT:
                        velocity_x = -2
                        velocity_y = 0
            
                    if event.key == pygame.K_UP:
                        velocity_y = -2
                        velocity_x = 0
            
                    if event.key == pygame.K_DOWN:
                        velocity_y = 2
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            # Ploating food in game 
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=10   
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score> int(highscore):
                    highscore = score

            gameWindow.fill(white)
            text_screen("Score: "+ str(score) + " Hiscore: " + str(highscore), red, 5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y> screen_height:
                game_over = True
                print("Game over")
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black,snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
# gameloop()
