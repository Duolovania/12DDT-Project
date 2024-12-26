from Modules.application import *
from Modules.gameobject import *
from Modules.sound import *
from enum import Enum
import math

userName: any = input("Please enter your username: ")
mahogany: tuple = (196, 73, 0)
richBlack: tuple = (4, 21, 31)
celeste: tuple = (185, 250, 248)
wisteria: tuple = (178, 152, 220)
amethyst: tuple = (166, 99, 204)

score: int = 0 # Game score.
questionNum: int = 0
optionSize: float = 0.5

window: Application = Application("warning.png", 800, 600, 0, "12DDT", False) # Creates new window.
gameRunning: bool = True # Status of game loop.
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0) # New audio channel for mouse SFX.

mouseCursor: Texture = Texture("mouse cursor.png", scale = 1.2)
background: Texture = Texture("Backgrounds/MainMenu.png", scale = 3)
background.transform.position = Vector2(-10, 0)

answers = ["Tame Impala", "Rihanna", "Billy Joel", "Kendrick Lamar", "Fleetwood Mac", "Michael Jackson", "The Weeknd", "Post Malone", "Don Toliver", "Post Malone again"]
btn1Options = ["Tame Impala", "Kendrick Lamar", "Billy Joel", "Bruno Mars", "twenty one pilots", "Da Baby", "The Weeknd", "Thomas Rhett", "Don Toliver", "Post Malone again"]
btn2Options = ["DJ Khaled", "Rihanna", "Morgan Wallen", "Lil Baby", "Fleetwood Mac", "Queen", "Lil Nas X", "Post Malone", "Janet Jackson", "Jack Black"]
btn3Options = ["Glass Animals", "Elton John", "Lauv", "Kendrick Lamar", "Rod Stewart", "J. Cole", "The Weekend", "Swae Lee", "Drake", "Lil Nas X"]
btn4Options = ["Maroon 5", "Taylor Swift", "Social House", "Da Baby", "Barbra Streisand", "Michael Jackson", "Drake", "Justin Moore", "Da Baby", "Lauv"]

currentAlbum: Texture = Texture("Albums/" + answers[questionNum] + ".png", scale = 1)

music: SFX = SFX("Kubbi - Up In My Jam  NO COPYRIGHT 8-bit Music.mp3") # Background music.
rightAns: SFX = SFX("Right.wav")
wrongAns: SFX = SFX("Wrong.wav")

music.set_music_volume(0.25)
music.load_music()

bitFont: str = "nokia_cellphone/nokiafc22.ttf"
scoreText: Text = Text(score, bitFont, scale = 1, fillColor = celeste)
scoreText.transform.position = Vector2(20, 20)

fpsText: Text = Text(score, bitFont, scale = 0.4, fillColor = wisteria)
fpsText.transform.position = Vector2(680, 20)

questionText: Text = Text("Guess the artist", bitFont, scale = 1, fillColor = celeste)
questionText.transform.position = Vector2(40, 520)

option1: Text = Text(btn1Options[questionNum], bitFont, scale = optionSize, fillColor = amethyst)
option1.transform.position = Vector2(40, 360)

option2: Text = Text(btn2Options[questionNum], bitFont, scale = optionSize, fillColor = wisteria)
option2.transform.position = Vector2(40, 410)

option3: Text = Text(btn3Options[questionNum], bitFont, scale = optionSize, fillColor = richBlack)
option3.transform.position = Vector2(40, 450)

option4: Text = Text(btn4Options[questionNum], bitFont, scale = optionSize, fillColor = richBlack)
option4.transform.position = Vector2(40, 490)

endText:Text = Text("ggs, " + userName, bitFont, scale = 1, fillColor = celeste)
endText.transform.position = Vector2(20, 20)

refreshAll: bool = False
clock = pygame.time.Clock()

creator: Texture = Texture("DLogo.png", 0.15)
creator.transform.position = Vector2(10, 10)

title: Texture = Texture("ehs.png", 0.1)
title.transform.position = Vector2(220, 150)

playGame: Text = Text("Play Game", bitFont)
playGame.transform.position = Vector2(40, 490)

class GameState(Enum):
    MainMenu = 0
    GameScreen = 1
    EndScreen = 2

gameState: GameState = GameState(GameState.MainMenu)

# Class handles game events.
class Game:
    # Function controls game loop and closes window after game loop is terminated.
    def run():
        while gameRunning:
            Game.forever()
        pygame.quit()
        quit()

    # Game loop.
    def forever():
        window.display.fill((0, 0, 0))
        pygame.time.delay(10)

        fpsText.text = "FPS: " + str(int(clock.get_fps()))
        clock.tick(60)
        background.path = "Assets/Images/Backgrounds/" + str(gameState.name) + ".png"
        background.reset_rect()
        background.draw(window.display)
        
        if gameState == GameState.GameScreen:
            scoreText.text = score
            currentAlbum.transform.position = Vector2(240, math.sin((pygame.time.get_ticks() / 3 % 1000) / 100) * 10 + 50)

            if questionNum < len(answers) - 1:
                currentAlbum.path = "Assets/Images/Albums/" + answers[questionNum] + ".png"
                
                option1.text = btn1Options[questionNum]
                option2.text = btn2Options[questionNum]
                option3.text = btn3Options[questionNum]
                option4.text = btn4Options[questionNum]

            if refreshAll:
                Game.refresh_all()
            
            currentAlbum.draw(window.display)

            scoreText.draw(window.display)
            questionText.draw(window.display)

            option1.draw(window.display)
            option2.draw(window.display)
            option3.draw(window.display)
            option4.draw(window.display)
        elif gameState == GameState.MainMenu:
            playGame.transform.position = Vector2(math.cos((pygame.time.get_ticks() / 3 % 1000) / 100) * 10 + 50, playGame.transform.position.y)

            title.draw(window.display)
            playGame.draw(window.display)
            creator.draw(window.display)
        else:
            playGame.transform.position = Vector2(math.cos((pygame.time.get_ticks() / 3 % 1000) / 100) * 10 + 50, playGame.transform.position.y)

            playGame.draw(window.display)
            endText.draw(window.display)
            
        mousepos = pygame.mouse.get_pos()
        mouseCursor.transform.position = Vector2(mousepos[0], mousepos[1])

        fpsText.reset_rect()
        fpsText.draw(window.display)
        mouseCursor.draw(window.display)
        
        Game.handle_events()
        pygame.display.update()

    # Refreshes all GameObjects.
    def refresh_all():
        scoreText.reset_rect()
        currentAlbum.reset_rect()
        option1.reset_rect()
        option2.reset_rect()
        option3.reset_rect()
        option4.reset_rect()

        global refreshAll
        refreshAll = False
    
    # Handles user's keyboard and mouse events.
    def handle_events():
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    global gameRunning
                    gameRunning = False
                case pygame.KEYDOWN:
                    Game.key_events(event)
                case pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    if option1.rect.collidepoint(mousepos):
                        Game.check_answer(option1.text)
                    elif option2.rect.collidepoint(mousepos):
                        Game.check_answer(option2.text)
                    elif option3.rect.collidepoint(mousepos):
                        Game.check_answer(option3.text)
                    elif option4.rect.collidepoint(mousepos):
                        Game.check_answer(option4.text)
                    elif playGame.rect.collidepoint(mousepos):
                        global gameState
                        global score
                        global questionNum

                        gameState = GameState.GameScreen
                        score = 0 
                        questionNum = 0
                        pygame.time.wait(50)

    # Checks if user picks the correct answer.
    def check_answer(text: str):
        global questionNum
        global refreshAll
        global score
        global gameState

        if questionNum + 2 > len(answers) - 1:
            gameState = GameState.EndScreen
            return

        if text == answers[questionNum]:
            score += 1
            rightAns.play(volume = 0.25)
            pygame.time.wait(50)            
        else:
            score -= 1
            wrongAns.play(volume = 0.25)
            pygame.time.wait(50)

        refreshAll = True
        questionNum += 1

    # Defines what each key press does.
    def key_events(gameEvent: pygame.event):
        match gameEvent.key:
            case pygame.K_UP:
                music.set_music_volume(pygame.mixer.music.get_volume() + 0.1)
            case pygame.K_DOWN:
                music.set_music_volume(pygame.mixer.music.get_volume() - 0.1)
            case pygame.K_m:
                music.set_music_volume(0)
            case pygame.K_ESCAPE:
                if window.flags != 0:
                    window.flags = 0
                    window.refresh()
                else:
                    global gameRunning
                    gameRunning = False
            case pygame.K_f:
                window.flags = pygame.FULLSCREEN
                window.refresh()