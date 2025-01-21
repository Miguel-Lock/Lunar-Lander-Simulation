import pygame

from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
    )

def main():
    '''
    Future Music Implementation
    pygame.mixer.init()
    pygame.mixer.music.load("BackgroundMusic.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(1)
    '''

    # Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    clock = pygame.time.Clock()


    # Ever Running Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # Manage key presses
                if event.key == pygame.K_ESCAPE: # Quit game if escape key is pressed
                    running = False
                    
    pygame.quit()


if __name__ == "__main__":
    main()