import pygame
from winsound import Beep

def display_number(barcode):
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Set the background color to transparent
    screen.fill((60, 63, 65))
    screen.set_alpha(200)

    # Display the text
    font = pygame.font.SysFont(None, 400)
    text = font.render(barcode, True, (255, 255, 255))
    text_rect = text.get_rect(center=screen.get_rect().center)
    screen.blit(text, text_rect)
    pygame.display.flip()
    Beep(3000,800)
    # Wait for 1 second
    pygame.time.wait(1000)

    # Quit the program
    pygame.quit()
if __name__ == '__main__':

    display_number("1234567890")