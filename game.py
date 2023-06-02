from mods import *

# userName: str = input("Please enter your username: ")

window: Application = Application(800, 600, "12DDT") # Creates new window.
gameRunning: bool = True # Status of game loop.
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0) # New audio channel for mouse SFX.

tommy: Texture = Texture("tommy.JPG", scale = 80)
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
        pygame.display.update()
        
        window.display.fill((0, 0, 0))

        global eshay
        eshay += 10
        
        # scoreText.rect = pygame.Rect(10, 5)

        window.Refresh(tommy)
        scoreText.Refresh(score)
        window.Refresh(scoreText)
        
        Game.HandleEvents()
    
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

    # Defines what each key press does.
    def KeyEvents(gameEvent: pygame.event):
        match gameEvent.key:
            case pygame.K_w:
                AGuitar.Play(volume = 0.8)
                global score
                score += 1
            case pygame.K_UP:
                music.SetMusicVolume(pygame.mixer.music.get_volume() + 0.1)
            case pygame.K_DOWN:
                music.SetMusicVolume(pygame.mixer.music.get_volume() - 0.1)
            case pygame.K_m:
                music.SetMusicVolume(0)