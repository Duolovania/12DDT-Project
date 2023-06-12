import pygame

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