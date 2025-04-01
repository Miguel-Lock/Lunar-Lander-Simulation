import pygame
pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)
text = ""
input_active = True

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode

        window.fill(0)
        text_surf = font.render(text, True, (255, 0, 0))
        window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
        pygame.display.flip()

pygame.quit()
exit()