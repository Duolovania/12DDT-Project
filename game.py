from mods import *
import math

# userName: str = input("Please enter your username: ")
darkPurple: tuple = (67, 37, 52)
mahogany: tuple = (196, 73, 0)
wheat: tuple = (239, 214, 172)
slateGray: tuple = (24, 58, 55)
richBlack: tuple = (4, 21, 31)

window: Application = Application("tommy.JPG", 800, 600, "12DDT") # Creates new window.
gameRunning: bool = True # Status of game loop.
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0) # New audio channel for mouse SFX.

tommy: Texture = Texture("thanus.png")
mouseCursor: Texture = Texture("cursor.png", scale = 0.3)
background: Texture = Texture("backg.png", scale = 1.2)

music: SFX = SFX("bad.mp3") # Background music.
AGuitar: SFX = SFX("a.wav")
eshay = 0

music.SetMusicVolume(0.25)
music.LoadMusic()
score: int = 0 # Game score.

moonFarkFont: str = "moonfark-font/MOONFARK-goova-studio.ttf" # Font path.
bitFont: str = "8_bit_arcade/8-bit Arcade In.ttf"
scoreText: Text = Text(score, bitFont, size = 60)

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

        scoreText.text = score

        tommy.transform.position = Vector2(math.cos((pygame.time.get_ticks() / 3 % 1000) / 100) * 100 + 100, math.sin((pygame.time.get_ticks() / 3 % 1000) / 100) * 100 + 200)
        tommy.transform.localScale = Vector2(score / 5, score / 10)

        mousepos = pygame.mouse.get_pos()
        mouseCursor.transform.position = Vector2(mousepos[0], mousepos[1])

        if scoreText.rect.collidepoint(mousepos):
            scoreText.fillColor = darkPurple
        else:
            scoreText.fillColor = richBlack

        background.Draw(window.display)
        tommy.Draw(window.display)
        scoreText.Draw(window.display)
        mouseCursor.Draw(window.display)

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
                        AGuitar.PlayThroughChannel(mouseChannel, volume = 0.25)
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