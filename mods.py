import pygame

# Class stores the application's size and label.
class Application:
    def __init__(self, w: int, h: int, title: str):
        pygame.init()

        self.w: int = w
        self.h: int = h
        self.title: str = title
        self.display: pygame.Surface = pygame.display.set_mode((w, h))

        pygame.display.set_caption(title)
    
    # Refreshes an object on the screen.
    def Refresh(self, refreshedObj: object):
        if not hasattr(refreshedObj, "surface"):
            print("The object does not have a surface variable. Variable of type '{0}' cannot be refreshed.".format(type(refreshedObj)))
            return
        elif refreshedObj is None:
            print("The object is null. Variable of type '{0}' cannot be refreshed.".format(type(refreshedObj)))
            return
        
        objSurface: pygame.Surface = refreshedObj.surface
        objRect: pygame.Rect = objSurface.get_rect()
        self.display.blit(objSurface, objRect)

# Class handles all image properties.
class Texture:
    def __init__(self, path: str, x: int = 0, y: int = 0, w: int = 10, h: int = 10, scale: int = 1):
        self.path: str = "Assets/Images/" + path
        self.x: int = x
        self.y: int = y

        self.surface: pygame.Surface = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), (w * scale, h * scale))
        self.rect: pygame.Rect = self.surface.get_rect()
    
    # Outputs the image onto the screen.
    def Draw(self, screen: pygame.Surface):
        screen.blit(self.path, (self.x, self.y), self.rect)

# Class handles all sound properties.
class SFX:
    def __init__(self, path: str):
        self.path: str = "Assets/SFX/" + path
        self.sound: pygame.mixer.Sound = pygame.mixer.Sound(self.path)
    
    # Plays background music (plays music forever by default)
    def LoadMusic(self, loopCount: int = -1):
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play(loopCount)

    # Plays sound effect through default channel
    def Play(self, loopCount: int = 0, volume: float = 1):
        self.sound.set_volume(volume)
        pygame.mixer.Sound.play(self.sound, loopCount)
    
    # Plays sound effect through specific channel
    def PlayThroughChannel(self, channel, loopCount: int = 0, volume: float = 1):
        self.sound.set_volume(volume)
        channel.play(self.sound, loopCount)
    
    # Sets the music volume.
    def SetMusicVolume(self, volume: float):
        pygame.mixer.music.set_volume(volume)

# Class handles all text properties.
class Text:
    green: tuple = (0, 255, 0)
    blue: tuple = (0, 0, 128)
    white: tuple = (0, 0, 0)

    def __init__(self, textValue: any, path: str, size: float = 32, antiAlias: bool = True, fillColor: tuple = white, borderColor: tuple = green):
        self.fontPath: str = path
        self.fontSize: int = size
        self.antiAlias: bool = antiAlias
        self.fillColor: tuple = fillColor
        self.borderColor: tuple = borderColor

        self.fontObj: pygame.font = pygame.font.Font("Assets/Fonts/" + path, size)
        self.surface: pygame.Surface = self.fontObj.render(str(textValue), antiAlias, fillColor, borderColor)
        self.rect: pygame.rect = self.surface.get_rect()
    
    # Sets new text value.
    def Refresh(self, newValue: any, hasAA: bool = True, newFill: tuple = white, newBorder: tuple = green):
        self.surface = self.fontObj.render(str(newValue), hasAA, newFill, newBorder)