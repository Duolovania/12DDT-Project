import pygame
from abc import ABC, abstractclassmethod
from Modules.transform import *

# Blueprint abstract class for visual objects (objects on screen).
class GameObject(ABC):
    # Abstract method. Must be implemented in child.
    @abstractclassmethod
    def reset_rect(self):
        pass

    # Outputs the object onto the screen.
    def draw(self, screen: pygame.Surface):
        self.rect.x = self.transform.position.x
        self.rect.y = self.transform.position.y
        screen.blit(self.surface, self.rect)

# Class handles all image properties. Inherits GameObject Draw().
class Texture(GameObject):
    def __init__(self, path: str, scale: Vector2 = 1):
        self.path: str = "Assets/Images/" + path
        self.transform: Transform = Transform(localScale = scale)

        self.reset_rect()
    
    # Resets the rect. This updates any values in __init__() before image is drawn on screen.
    def reset_rect(self):
        self.image: pygame.Surface = pygame.image.load(self.path).convert_alpha()
        self.surface = pygame.transform.scale(self.image, (self.image.get_width() * self.transform.localScale.x, self.image.get_height() * self.transform.localScale.y))

        self.rect = self.surface.get_rect()
        

# Class handles all text properties. Inherits GameObject Draw().
class Text(GameObject):
    black: tuple = (0, 0, 0)
    white: tuple = (255, 255, 255)

    def __init__(self, textValue: any, path: str, scale: float = 1, antiAlias: bool = False, fillColor: tuple = black, borderColor: tuple = None):
        self.fontPath: str = path
        self.antiAlias: bool = antiAlias

        self.fillColor: tuple = fillColor
        self.borderColor: tuple = borderColor

        self.transform: Transform = Transform(localScale = scale)
        self.text: any = textValue

        self.reset_rect()

    # Resets the rect. This updates any values in __init__() before text is drawn on screen.
    def reset_rect(self):
        self.fontObj: pygame.font = pygame.font.Font("Assets/Fonts/" + self.fontPath, 64)
        renderedText: pygame.Surface = self.fontObj.render(str(self.text), self.antiAlias, self.fillColor, self.borderColor)
        width = renderedText.get_width()
        height = renderedText.get_height()

        self.surface = pygame.transform.scale(renderedText, (width * self.transform.localScale.x, height * self.transform.localScale.y))
        
        self.rect = self.surface.get_rect()