import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Multiple Saved Sprites")

# Load sprite sheet image
sprite_sheet = pygame.image.load('../assets/sprites/astronaut_spritesheet.png')

# Load individual sprites
player_sprite1 = sprite_sheet.subsurface((0, 0, 64, 64))
player_sprite2 = sprite_sheet.subsurface((0, 64, 64, 64))
player_sprite3 = sprite_sheet.subsurface((0, 128, 64, 64))
player_sprite4 = sprite_sheet.subsurface((0, 192, 64, 64))

# # Function to extract individual sprites from sprite sheet
# def get_individual_sprite(x, y, width, height):
#     sprite = sprite_sheet.subsurface((x, y, width, height))
#     return sprite
#
# # Define the coordinates and dimensions of the sprites you want to extract
# sprites_info = [
#     (0, 0, 64, 64),  # (x, y, width, height)
#     (0, 64, 64, 64),
#     (0, 128, 64, 64),
#     (0, 192, 64, 64)
# ]
#
# # Create an empty list to store the extracted sprites
# sprites_list = []
#
# # Extract and store sprites in the list
# for info in sprites_info:
#     individual_sprite = get_individual_sprite(*info)
#     sprites_list.append(individual_sprite)
#
# # Main loop
# running = True
# clock = pygame.time.Clock()
#
# while running:
#     screen.fill((255, 255, 255))
#
#     # Display the sprites from the list
#     # x_offset = 0
#     # for sprite in sprites_list:
#     #     screen.blit(sprite, (100 + x_offset, 100))
#     #     x_offset += 50  # Adjust the spacing between sprites
#     screen.blit(player_sprite1, (0,150))
#     screen.blit(player_sprite2, (0,210))
#     screen.blit(player_sprite3, (0, 270))
#     screen.blit(player_sprite4, (0, 320))
#
#     pygame.display.flip()
#
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     clock.tick(60)  # Set the frame rate
#
# # Quit Pygame
# pygame.quit()