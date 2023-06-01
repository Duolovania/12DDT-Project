from mods import Texture, SFX, pygame, Application, Text

window: Application = Application(800, 600, "12DDT")
gameRunning: bool = True
mouseChannel: pygame.mixer.Channel = pygame.mixer.Channel(0)

tommy: Texture = Texture("tommy.JPG", scale = 80)
music: SFX = SFX("Arcadia.mp3")
AGuitar: SFX = SFX("a.wav")

music.LoadMusic()
score: int = 0

moonFarkFont: str = "moonfark-font/MOONFARK-goova-studio.ttf"
scoreText: Text = Text(score, moonFarkFont)

# Class handles game events.
class Game:
    def Run():
        while gameRunning:
            Game.Forever()
        
        pygame.quit()
        quit()

    def Forever():
        pygame.display.update()
        
        window.display.fill((0, 0, 0))

        window.Refresh(tommy)
        scoreText.Refresh(score)
        window.Refresh(scoreText)
        Game.HandleEvents()

        
        
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