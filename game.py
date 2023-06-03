from mods import *
import math

# userName: str = input("Please enter your username: ")

window: Application = Application("tommy.JPG", 800, 600, "12DDT") # Creates new window.
gameRunning: bool = True # Status of game loop.
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0) # New audio channel for mouse SFX.

tommy: Texture = Texture("tommy.JPG", w = 40)
music: SFX = SFX("Arcadia.mp3") # Background music.
AGuitar: SFX = SFX("a.wav")
randomNum: float = 0
eshay = 0
music.LoadMusic()
score: int = 0 # Game score.

moonFarkFont: str = "moonfark-font/MOONFARK-goova-studio.ttf" # Font path.
scoreText: Text = Text(score, moonFarkFont)

# Class handles game events.
class Game:
    # Function controls game loop and closes window after game loop is terminated.
    def Run():
        while gameRunning:
            Game.Forever()
        
        pygame.quit()
        quit()

    # Game loop.
    def Forever():
        window.display.fill((0, 0, 0))
        pygame.time.delay(16)
        global eshay

        tommy.transform.position = Vector2(math.cos((pygame.time.get_ticks() / 3 % 1000) / 100) * 100 + 100, math.sin((pygame.time.get_ticks() / 3 % 1000) / 100) * 100 + 200)
        tommy.transform.localScale = Vector2(score / 5, score / 5)
        
        tommy.Draw(window.display)

        scoreText.Refresh(score)
        window.Refresh(scoreText)
        
        Game.HandleEvents()
        pygame.display.update()
    
    # Handles user's keyboard and mouse events.
    def HandleEvents():
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    global gameRunning
                    gameRunning = False
                case pygame.KEYDOWN:
                    Game.KeyEvents(event)
                case pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    if scoreText.rect.collidepoint(mousepos):
                        AGuitar.PlayThroughChannel(mouseChannel, volume = 0.8)
                        global score
                        score += 1

    # Defines what each key press does.
    def KeyEvents(gameEvent: pygame.event):
        match gameEvent.key:
            case pygame.K_UP:
                music.SetMusicVolume(pygame.mixer.music.get_volume() + 0.1)
            case pygame.K_DOWN:
                music.SetMusicVolume(pygame.mixer.music.get_volume() - 0.1)
            case pygame.K_m:
                music.SetMusicVolume(0)