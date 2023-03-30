import pygame
import os
pygame.font.init()
pygame.mixer.init()

class GameStyle():
    def __init__(self, game) -> None:
        self.game = game
        
        self.name = "Téras"
        self.background_colour = (255, 255, 255)
        
        self.apply_properties()
    
    def apply_properties(self):
        pygame.display.set_caption(self.name)
        self.game.window.fill(self.background_colour)
        
class Assets():
    def __init__(self) -> None:
        assets = [os.path.join("assets\\\\textures", name) for name in os.listdir("assets\\\\textures")]
        for asset in assets:
            setattr(self, asset.replace("assets\\\\textures\\", "").replace(".png", ""), pygame.image.load(asset))
        

class Game():
    def __init__(self) -> None:
        #Постоянные значения:
        self.fps = 60
        self.window_width, self.window_height = 900, 500
        
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        self.game_style = GameStyle(self)
        self.assets = Assets()
        self.main()

    def main(self):
        self.start()
        
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.update()
        pygame.quit()
        
    def start(self):
        self.draw_terrain()
    
    def update(self):
        pygame.display.update()
        
    def draw_terrain(self):
        self.terrain = self.generate_terrain()
        tile = lambda name: pygame.transform.scale(getattr(self.assets, name), (50, 50))
        
        for x in range(len(self.terrain)):
            for y in range(len(self.terrain[x])):
                if self.terrain[x][y] == "G":
                    self.window.blit(tile("ground_with_grass"), (x*50, y*50))
        
    def generate_terrain(self):
        #ToDo: Сделать генерацию ландшафта
        return [["G" for y in range(10)] for x in range(20)]
            
        
                
if __name__ == "__main__":
    Game()