import pygame
import sys
from settings import WIDTH, HEIGHT, FPS
from player import Player
from wave_manager import WaveManager
from background import Background

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    bg = Background()
    player = Player()
    waves = WaveManager()
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update
        bg.update()
        player.update()
        waves.update(player)
        
        # Draw
        screen.fill((0,0,0))
        bg.draw(screen)
        player.draw(screen)
        waves.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()