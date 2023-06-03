import pygame

# Class handles the storage of x and y coordinated.
class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y

# Class handles the storage of positional, rotational and local scale values.
class Transform:
    def __init__(self, position: Vector2 = Vector2(), rotation: Vector2 = Vector2(), localScale: Vector2 = Vector2(1, 1)):
        self.position = position
        self.rotation = rotation

        # If localScale argument is 50. localScale will equal to (50, 50)
        if type(localScale) == float or type(localScale) == int:
            self.localScale = Vector2(localScale, localScale)
        else:
            self.localScale = localScale

# Class stores the application's size and label.
class Application:
    def __init__(self, iconPath: str, w: int, h: int, title: str):
        pygame.init()

        self.w: int = w
        self.h: int = h
        self.title: str = title
        self.iconSurface = pygame.image.load("Assets/Images/" + iconPath) 
        self.display: pygame.Surface = pygame.display.set_mode((w, h))
        
        pygame.display.set_icon(self.iconSurface)
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
    def __init__(self, path: str, w: int = 10, h: int = 10, scale: Vector2 = 1):
        self.path: str = "Assets/Images/" + path
        self.transform: Transform = Transform(localScale = scale)
        self.w = w
        self.h = h

        self.SetRect()
    
    def SetRect(self):
        self.surface = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), (self.w * self.transform.localScale.x, self.h * self.transform.localScale.y))
        self.rect = self.surface.get_rect()
    
    # Outputs the image onto the screen.
    def Draw(self, screen: pygame.Surface):
        self.SetRect()
        screen.blit(self.surface, (self.transform.position.x, self.transform.position.y), self.rect)

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