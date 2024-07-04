import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

# Scale images
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Font
font = pygame.font.SysFont("comicsans", 50)

# Game variables
choices = ['rock', 'paper', 'scissors']
user_choice = ""
comp_choice = ""
result = ""

def get_result(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def draw_window():
    win.fill(white)
    win.blit(rock_img, (50, 400))
    win.blit(paper_img, (325, 400))
    win.blit(scissors_img, (600, 400))

    if user_choice:
        user_text = font.render(f'You chose: {user_choice}', True, black)
        win.blit(user_text, (50, 200))

    if comp_choice:
        comp_text = font.render(f'Computer chose: {comp_choice}', True, black)
        win.blit(comp_text, (50, 100))

    if result:
        result_text = font.render(result, True, black)
        win.blit(result_text, (50, 300))

    pygame.display.update()

# Main loop
run = True
while run:
    draw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 50 < x < 200 and 400 < y < 550:
                user_choice = 'rock'
            elif 325 < x < 475 and 400 < y < 550:
                user_choice = 'paper'
            elif 600 < x < 750 and 400 < y < 550:
                user_choice = 'scissors'

            if user_choice:
                comp_choice = random.choice(choices)
                result = get_result(user_choice, comp_choice)

pygame.quit()
