from mods import *
import math

# userName: any = input("Please enter your username: ")
darkPurple: tuple = (67, 37, 52)
mahogany: tuple = (196, 73, 0)
wheat: tuple = (239, 214, 172)
slateGray: tuple = (24, 58, 55)
richBlack: tuple = (4, 21, 31)
celeste: tuple = (185, 250, 248)
columbiaBlue: tuple = (184, 208, 235)
wisteria: tuple = (178, 152, 220)
amethyst: tuple = (166, 99, 204)
grape: tuple = (111, 45, 189)

window: Application = Application("tommy.JPG", 800, 600, 0, "12DDT", False) # Creates new window.
gameRunning: bool = True # Status of game loop.
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0) # New audio channel for mouse SFX.

mouseCursor: Texture = Texture("mouse cursor.png", scale = 1.2)
background: Texture = Texture("back.png", scale = 3)
background.transform.position = Vector2(-10, 0)

currentAlbum: Texture = Texture("Albums/Tame Impala.png", scale = 1)
albums = ["Tame Impala", "Rihanna", "Billy Joel", "Kendrick Lamar", "Fleetwood Mac", "Michael Jackson", "The Weeknd", "Post Malone", "Don Toliver", "Post Malone again"]
btn1Options = ["Tame Impala", "Kendrick Lamar", "Billy Joel", "Bruno Mars", "twenty one pilots", "Da Baby", "The Weeknd", "Thomas Rhett", "Don Toliver", "Post Malone again"]
btn2Options = ["DJ Khaled", "Rihanna", "Morgan Wallen", "Lil Baby", "Fleetwood Mac", "Queen", "Lil Nas X", "Post Malone", "Janet Jackson", "Jack Black"]
btn3Options = ["Glass Animals", "Elton John", "Lauv", "Kendrick Lamar", "Rod Stewart", "J. Cole", "The Weekend", "Swae Lee", "Drake", "Lil Nas X"]
btn4Options = ["Maroon 5", "Taylor Swift", "Social House", "Da Baby", "Barbra Streisand", "Michael Jackson", "Drake", "Justin Moore", "Da Baby", "Lauv"]

music: SFX = SFX("ov.mp3") # Background music.
AGuitar: SFX = SFX("a.wav")

music.SetMusicVolume(0.25)
music.LoadMusic()
score: int = 0 # Game score.
questionNum: int = 0

bitFont: str = "8_bit_arcade/8-bit Arcade In.ttf"
scoreText: Text = Text(score, bitFont, scale = 2, fillColor = celeste)
scoreText.transform.position = Vector2(20, 0)

questionText: Text = Text("Guess the artist", bitFont, scale = 1.5, fillColor = celeste)
questionText.transform.position = Vector2(40, 520)

option1: Text = Text("Tame Impala", bitFont, scale = 1, fillColor = amethyst)
option1.transform.position = Vector2(40, 360)

option2: Text = Text("Tame Impala", bitFont, scale = 1, fillColor = wisteria)
option2.transform.position = Vector2(40, 400)

option3: Text = Text("Tame Impala", bitFont, scale = 1, fillColor = richBlack)
option3.transform.position = Vector2(40, 440)

option4: Text = Text("Tame Impala", bitFont, scale = 1, fillColor = richBlack)
option4.transform.position = Vector2(40, 480)

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

        scoreText.text = score
        currentAlbum.transform.position = Vector2(240, math.sin((pygame.time.get_ticks() / 3 % 1000) / 100) * 10 + 50)
        currentAlbum.path = "Assets/Images/Albums/" + albums[questionNum] + ".png"

        option1.text = btn1Options[questionNum]
        option2.text = btn2Options[questionNum]
        option3.text = btn3Options[questionNum]
        option4.text = btn4Options[questionNum]

        mousepos = pygame.mouse.get_pos()
        mouseCursor.transform.position = Vector2(mousepos[0], mousepos[1])

        background.Draw(window.display)
        currentAlbum.Draw(window.display)

        scoreText.Draw(window.display)
        questionText.Draw(window.display)

        option1.Draw(window.display)
        option2.Draw(window.display)
        option3.Draw(window.display)
        option4.Draw(window.display)
        
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
                    if option1.rect.collidepoint(mousepos):
                        Game.CheckAnswer(option1.text)
                    elif option2.rect.collidepoint(mousepos):
                        Game.CheckAnswer(option2.text)
                    elif option3.rect.collidepoint(mousepos):
                        Game.CheckAnswer(option3.text)
                    elif option4.rect.collidepoint(mousepos):
                        Game.CheckAnswer(option4.text)

    # Checks if user picks the correct answer.
    def CheckAnswer(text: str):
        global questionNum
        AGuitar.Play(volume = 0.25)

        if text == albums[questionNum]:
            scoreText.transform.localScale = Vector2(4, 4)
            
            global score
            score += 1

            pygame.time.wait(50)
            scoreText.transform.localScale = Vector2(2, 2)
        else:
            score -= 1
            pygame.time.wait(50)
        
        questionNum += 1
                    

    # Defines what each key press does.
    def KeyEvents(gameEvent: pygame.event):
        match gameEvent.key:
            case pygame.K_UP:
                music.SetMusicVolume(pygame.mixer.music.get_volume() + 0.1)
            case pygame.K_DOWN:
                music.SetMusicVolume(pygame.mixer.music.get_volume() - 0.1)
            case pygame.K_m:
                music.SetMusicVolume(0)
            case pygame.K_ESCAPE:
                if window.flags != 0:
                    window.flags = 0
                    window.Refresh()
                else:
                    global gameRunning
                    gameRunning = False
            case pygame.K_f:
                window.flags = pygame.FULLSCREEN
                window.Refresh()