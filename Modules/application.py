import pygame

# Class stores the application's size and label.
class Application:
    def __init__(self, iconPath: str, w: int, h: int, flags: int, title: str, showCursor: bool = True):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()

        self.w: int = w
        self.h: int = h
        self.flags: int = flags
        self.title: str = title
        self.iconSurface = pygame.image.load("Assets/Images/" + iconPath) 
        self.display: pygame.Surface = pygame.display.set_mode((w, h), flags)

        pygame.display.set_icon(self.iconSurface)
        pygame.mouse.set_visible(showCursor)
        pygame.display.set_caption(title)
    
    # Refreshes the window. Use this to change screen dimensions or fullscreen.
    def Refresh(self):
        self.display = pygame.display.set_mode((self.w, self.h), self.flags)