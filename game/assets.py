import pygame

# Load intro font
intro_font = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 40)

# Load font to count seconds
count_font = pygame.font.Font("../assets/fonts/game-of-squids/Game Of Squids.ttf", 48)

# Load game title font
title_font1 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 60)
title_font2 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 62)

# Game over font
game_over_font1 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 60)
game_over_font2 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 26)

# Load background music
b_sound = pygame.mixer.Sound("../assets/sounds/background.mp3")
channel1 = pygame.mixer.Channel(1)
channel1.play(b_sound)

# Sound effects
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
channel2 = pygame.mixer.Channel(2)
channel2.play(hurt)
