from typing import Tuple
import pygame
import time
import random
from lib.game.display import GameDisplay, Clock
from lib.game.engines import GameEngine
from lib.game.events import events
from lib.game.images import GameImages
from lib.game.navigation import Navigation
from lib.game.properties import Colors, Display, Images, Car
import logging

PAUSE = False

'''
TO DO:
- Rebuild the points/passed system
- Shrink Roads for Improved View

BUGS: 
- Inconsistent Button Response (Must Double Click Button to Activate)
    - FIXED???
'''

class _GameSetup:
    """The class represents setup for a game."""

    GAME = GameEngine()
    DISPLAY = GameDisplay(Display)
    CLOCK = Clock()
    GAME_IMAGES = GameImages(Images)
    GAME_DISPLAYS = DISPLAY.set_size()
    DISPLAY.set_title()
    CAR_IMAGE = GAME_IMAGES.car()
    BACKGROUND_PIC = GAME_IMAGES.grass()
    WHITE_STRIP = GAME_IMAGES.white_strip()
    STRIP = GAME_IMAGES.strip()
    INTRO_BACKGROUND = GAME_IMAGES.back()
    INSTRUCTION_BACKGROUND = INTRO_BACKGROUND


class _GameView:
    """The class represents game view."""

    GRAY = Colors.gray.value
    BLACK = Colors.black.value
    RED = Colors.red.value
    GREEN = Colors.green.value
    BLUE = Colors.blue.value
    BUTTON_GRAY = Colors.button_gray.value
    DARK_RED = Colors.dark_red.value
    DARK_GREEN = Colors.dark_green.value
    DARK_BLUE = Colors.dark_blue.value
    DARK_GRAY = Colors.dark_gray.value
    DISPLAY_WIDTH = Display.width.value
    DISPLAY_HEIGHT = Display.height.value


def intro_loop() -> None:
    """Runs into game loop."""
    while True:
        for event in events():
            if event.type == Navigation.is_quit(event):
                _GameSetup.GAME.stop()
        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INTRO_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 75)
        text_surf, text_rect = text_objects("Highway Simulator", large_text)
        text_rect.center = (400, 100)

        title_background = pygame.Surface((710, 200), pygame.SRCALPHA)
        pygame.draw.rect(title_background, (101, 148, 186, 150), (0, 0, 710, 100))
        _GameSetup.GAME_DISPLAYS.blit(title_background, (45, 50))

        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        playButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(playButton_background, (56, 142, 60, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(playButton_background, (46, 416))
        button("Start", 50, 420, 200, 60, _GameView.GREEN, _GameView.DARK_GREEN, "play")

        helpButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(helpButton_background, (25, 118, 210, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(helpButton_background, (296, 416))
        button("Help", 300, 420, 200, 60, _GameView.BLUE, _GameView.DARK_BLUE, "help")

        quitButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(quitButton_background, (211, 47, 47, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(quitButton_background, (546, 416))
        button("Quit", 550, 420, 200, 60, _GameView.RED, _GameView.DARK_RED, "quit")
        pygame.display.update()
        _GameSetup.CLOCK.tick(50)


def button(message, x_coordinate, y_coordinate, weight, height, from_color, back_color, action=None) -> None:
    """Returns a game button."""
    mouse = Navigation.get_mouse_position()
    click = Navigation.get_mouse_pressed()
    if x_coordinate + weight > mouse[0] > x_coordinate and y_coordinate + height > mouse[1] > y_coordinate:
        pygame.draw.rect(_GameSetup.GAME_DISPLAYS, back_color, (x_coordinate, y_coordinate, weight, height))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                _GameSetup.GAME.stop()
            elif action == "help":
                help()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                pause_game()
            elif action == "unpause":
                unpause_game()
    else:
        pygame.draw.rect(_GameSetup.GAME_DISPLAYS, from_color, (x_coordinate, y_coordinate, weight, height))
    mediumText = pygame.font.Font("freesansbold.ttf", 35)
    text_surf, text_rect = text_objects(message, mediumText)
    text_rect.center = ((x_coordinate + (weight / 2)), (y_coordinate + (height / 2)))
    _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)


def help() -> None:
    """Displays game instruction screen."""
    while True:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INSTRUCTION_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 75)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        small_text = pygame.font.Font('freesansbold.ttf', 20)

        '''

        INSTRUCTIONS

        '''
        h1_text_surf, h1_text_rect = text_objects("Instructions", large_text)
        h1_text_rect.center = (400, 100)
        h1_background = pygame.Surface((480, 200), pygame.SRCALPHA)
        pygame.draw.rect(h1_background, (101, 148, 186, 150), (0, 0, 480, 100))
        _GameSetup.GAME_DISPLAYS.blit(h1_background, (160, 50))
        _GameSetup.GAME_DISPLAYS.blit(h1_text_surf, h1_text_rect)

        # Background
        desc_background = pygame.Surface((400, 325), pygame.SRCALPHA)
        pygame.draw.rect(desc_background, (101, 148, 186, 200), (0, 0, 375, 295))
        _GameSetup.GAME_DISPLAYS.blit(desc_background, (30, 175))
        
        # Line 1
        desc_text_surf, desc_text_rect = text_objects("\"Keep Right, Pass Left\" is a", small_text)
        desc_text_rect.center = (178, 200)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 2
        desc_text_surf, desc_text_rect = text_objects("fundamental rule when driving on", small_text)
        desc_text_rect.center = (214, 225)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 3
        desc_text_surf, desc_text_rect = text_objects("highways.", small_text)
        desc_text_rect.center = (92, 250)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 4
        desc_text_surf, desc_text_rect = text_objects("Stay in the right lane until a car is", small_text)
        desc_text_rect.center = (210, 300)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 5
        desc_text_surf, desc_text_rect = text_objects("in your way, then move back over.", small_text)
        desc_text_rect.center = (208, 325)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 6
        desc_text_surf, desc_text_rect = text_objects("You'll get hit by someone going", small_text)
        desc_text_rect.center = (196, 350)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)

        # Line 7
        desc_text_surf, desc_text_rect = text_objects("faster if you don't move.", small_text)
        desc_text_rect.center = (162, 375)
        _GameSetup.GAME_DISPLAYS.blit(desc_text_surf, desc_text_rect)


        '''

        CONTROLS TEXT

        '''
        h2_text_surf, h2_text_rect = text_objects("Controls", mediumtext)
        h2_text_rect.center = (572, 205)
        h2_background = pygame.Surface((300, 325), pygame.SRCALPHA)
        pygame.draw.rect(h2_background, (101, 148, 186, 200), (0, 0, 300, 295))
        _GameSetup.GAME_DISPLAYS.blit(h2_background, (470, 175))
        _GameSetup.GAME_DISPLAYS.blit(h2_text_surf, h2_text_rect)

        th3_text_surf, th3_text_rect = text_objects("W", small_text)
        th3_text_rect.center = (500, 250)
        td3_text_surf, td3_text_rect = text_objects("Speed Up", small_text)
        td3_text_rect.center = (602, 250)
        _GameSetup.GAME_DISPLAYS.blit(th3_text_surf, th3_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(td3_text_surf, td3_text_rect)

        th1_text_surf, th1_text_rect = text_objects("A", small_text)
        th1_text_rect.center = (500, 300)
        td1_text_surf, td1_text_rect = text_objects("Move to Left Lane", small_text)
        td1_text_rect.center = (643, 300)
        _GameSetup.GAME_DISPLAYS.blit(th1_text_surf, th1_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(td1_text_surf, td1_text_rect)

        th4_text_surf, th4_text_rect = text_objects("S", small_text)
        th4_text_rect.center = (500, 350)
        td4_text_surf, td4_text_rect = text_objects("Slow Down", small_text)
        td4_text_rect.center = (610, 350)
        _GameSetup.GAME_DISPLAYS.blit(th4_text_surf, th4_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(td4_text_surf, td4_text_rect)
        
        th2_text_surf, th2_text_rect = text_objects("D", small_text)
        th2_text_rect.center = (500, 400)
        td2_text_surf, td2_text_rect = text_objects("Move to Right Lane", small_text)
        td2_text_rect.center = (650, 400)
        _GameSetup.GAME_DISPLAYS.blit(th2_text_surf, th2_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(td2_text_surf, td2_text_rect)

        th5_text_surf, th5_text_rect = text_objects("P", small_text)
        th5_text_rect.center = (500, 450)
        td5_text_surf, td5_text_rect = text_objects("Pause", small_text)
        td5_text_rect.center = (584, 450)
        _GameSetup.GAME_DISPLAYS.blit(th5_text_surf, th5_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(td5_text_surf, td5_text_rect)

        backButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(backButton_background, (128, 128, 128, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(backButton_background, (566, 496))
        button("Back", 570, 500, 200, 60, _GameView.BUTTON_GRAY, _GameView.DARK_GRAY, "menu")

        pygame.display.update()
        _GameSetup.CLOCK.tick(30)


def pause_game() -> None:
    """Pause the game."""
    global PAUSE
    while PAUSE:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INSTRUCTION_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 75)
        pausedTitle_surf, pausedTitle_rect = text_objects("Paused", large_text)
        pausedTitle_rect.center = (400, 100)
        pausedTitle_background = pygame.Surface((350, 200), pygame.SRCALPHA)
        pygame.draw.rect(pausedTitle_background, (101, 148, 186, 150), (0, 0, 290, 85))
        _GameSetup.GAME_DISPLAYS.blit(pausedTitle_background, (255, 55))
        _GameSetup.GAME_DISPLAYS.blit(pausedTitle_surf, pausedTitle_rect)

        continueButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(continueButton_background, (56, 142, 60, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(continueButton_background, (296, 196))
        button("Continue", 300, 200, 200, 60, _GameView.GREEN, _GameView.DARK_GREEN, "unpause")

        restartButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(restartButton_background, (25, 118, 210, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(restartButton_background, (296, 336))
        button("Restart", 300, 340, 200, 60, _GameView.BLUE, _GameView.DARK_BLUE, "play")

        menuButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(menuButton_background, (211, 47, 47, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(menuButton_background, (296, 476))
        button("Menu", 300, 480, 200, 60, _GameView.RED, _GameView.DARK_RED, "menu")

        pygame.display.update()
        _GameSetup.CLOCK.tick(30)


def unpause_game() -> None:
    """Unpause a game."""
    global PAUSE
    PAUSE = False


def countdown_background() -> None:
    """Displays game background."""
    font = pygame.font.SysFont(None, 35)
    x = 500
    y = 350
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 300))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 500))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 600))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.CAR_IMAGE, (x, y))
    
    score = font.render("Score: 0", True, _GameView.RED)
    score_background = pygame.Surface((350, 200), pygame.SRCALPHA)
    pygame.draw.rect(score_background, (101, 148, 186, 200), (0, 0, 135, 35))
    _GameSetup.GAME_DISPLAYS.blit(score_background, (15, 15))
    _GameSetup.GAME_DISPLAYS.blit(score, (21, 20))

    text = font.render("Passed: 0", True, _GameView.BLACK)
    score_background = pygame.Surface((350, 200), pygame.SRCALPHA)
    pygame.draw.rect(score_background, (101, 148, 186, 200), (0, 0, 135, 35))
    _GameSetup.GAME_DISPLAYS.blit(score_background, (15, 60))
    _GameSetup.GAME_DISPLAYS.blit(text, (20, 65))

    pauseButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
    pygame.draw.rect(pauseButton_background, (25, 118, 210, 255), (0, 0, 208, 68))
    _GameSetup.GAME_DISPLAYS.blit(pauseButton_background, (581, 11))
    button("Pause", 585, 15, 200, 60, _GameView.BLUE, _GameView.DARK_BLUE, "pause")


def countdown() -> None:
    """Counts down game loop."""
    while True:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("3", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("2", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("1", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("Go!!", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        game_loop()


def obstacle(obs_start_x: int, obs_start_y: int, obs: int) -> None:
    """Visualize some game canvas obstacle."""
    images = {
        0: _GameSetup.GAME_IMAGES.car(),
        1: _GameSetup.GAME_IMAGES.car_one(),
        2: _GameSetup.GAME_IMAGES.car_two(),
        3: _GameSetup.GAME_IMAGES.car_three(),
        4: _GameSetup.GAME_IMAGES.car_four(),
        5: _GameSetup.GAME_IMAGES.car_five(),
        6: _GameSetup.GAME_IMAGES.car_six()
    }
    _GameSetup.GAME_DISPLAYS.blit(images[obs], (obs_start_x, obs_start_y))


def score_system(passed: str, score: int) -> None:
    """Displays scoring table."""
    font = pygame.font.SysFont(None, 35)

    score = font.render("Score: " + str(score), True, _GameView.RED)
    score_background = pygame.Surface((350, 200), pygame.SRCALPHA)
    pygame.draw.rect(score_background, (101, 148, 186, 200), (0, 0, 135, 35))
    _GameSetup.GAME_DISPLAYS.blit(score_background, (15, 15))
    _GameSetup.GAME_DISPLAYS.blit(score, (21, 20))

    text = font.render("Passed: " + str(passed), True, _GameView.BLACK)
    score_background = pygame.Surface((350, 200), pygame.SRCALPHA)
    pygame.draw.rect(score_background, (101, 148, 186, 200), (0, 0, 135, 35))
    _GameSetup.GAME_DISPLAYS.blit(score_background, (15, 60))
    _GameSetup.GAME_DISPLAYS.blit(text, (20, 65))



    


def text_objects(text: str, font: pygame.font.Font) -> Tuple[str, str]:
    """Returns some text object."""
    text_surface = font.render(text, True, _GameView.BLACK)
    return text_surface, text_surface.get_rect()


def message_display(text: str) -> None:
    """Displays some message."""
    large_text = pygame.font.Font("freesansbold.ttf", 80)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
    _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash() -> None:
    """Displays crash message."""
    message_display("You Crashed")


def background() -> None:
    """Displays background on the canvas."""
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 300))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, 500))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 200))


def display_car(x_coordinate: int, y_coordinate: int) -> None:
    """Displays car on the canvas."""
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.CAR_IMAGE, (x_coordinate, y_coordinate))


def game_loop() -> None:
    """Starts main game loop."""
    global PAUSE
    x = 500
    y = 350
    LEFT_LANE_X = 200
    RIGHT_LANE_X = 500
    x_change = 0
    obstacle_speed = 5
    obs = 0
    obs_start_x = random.choice([LEFT_LANE_X, RIGHT_LANE_X])
    obs_start_y = _GameView.DISPLAY_HEIGHT
    obs_width = 56
    obs_height = 125
    obstacle_id = 0
    counted_obstacles = set()
    passed = 0
    level = 0
    score = 0
    npc_counted_for_scoring = False
    y2 = 5

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

            if Navigation.is_down(event):
                if Navigation.is_left(event):
                    x = LEFT_LANE_X
                elif Navigation.is_right(event):
                    x = RIGHT_LANE_X
                if Navigation.is_accelerate(event):
                    obstacle_speed += 2
                if Navigation.is_brake(event):
                    obstacle_speed -= 2
                if Navigation.is_pause(event):
                    pause_game()
            if Navigation.is_up(event):
                if Navigation.is_left(event) or Navigation.is_right(event):
                    x_change = 0

        x += x_change
        PAUSE = True
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)

        rel_y = y2 % _GameSetup.BACKGROUND_PIC.get_rect().width
        _GameSetup.GAME_DISPLAYS.blit(
            _GameSetup.BACKGROUND_PIC, (0, rel_y - _GameSetup.BACKGROUND_PIC.get_rect().width)
        )
        _GameSetup.GAME_DISPLAYS.blit(
            _GameSetup.BACKGROUND_PIC, (700, rel_y - _GameSetup.BACKGROUND_PIC.get_rect().width)
        )
        if rel_y < 800:
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y + 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y + 200))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y + 300))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y + 400))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y + 500))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.WHITE_STRIP, (400, rel_y - 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y - 200))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y + 20))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y + 30))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y - 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y + 20))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y + 30))

        y2 += obstacle_speed



        if obs_start_x == LEFT_LANE_X:
            obs_start_y -= obstacle_speed
        else:
            obs_start_y += obstacle_speed
        
        npc_y = obs_start_y


        obstacle(obs_start_x, obs_start_y, obs)
        display_car(x, y)

        if not npc_counted_for_scoring and ((obs_start_x == LEFT_LANE_X and npc_y < y) or (obs_start_x == RIGHT_LANE_X and npc_y > y)):
            
            passed += 1
            score += 10
            npc_counted_for_scoring = True
                
            # Level progression
            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                large_text = pygame.font.Font("freesansbold.ttf", 80)
                text_surf, text_rect = text_objects("Level " + str(level), large_text)
                text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
                _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
                pygame.display.update()
                time.sleep(2)

        # Reset NPC after disappearing
        if npc_y < 0 - obs_height or npc_y > _GameView.DISPLAY_HEIGHT:
            npc_counted_for_scoring = False
            obs_start_y = _GameView.DISPLAY_HEIGHT if obs_start_x == LEFT_LANE_X else 0 - obs_height
            obs = random.randrange(0, 7)
            obs_start_x = random.choice([LEFT_LANE_X, RIGHT_LANE_X])
            obstacle_id += 1

        score_system(passed, score)

        # Car Crash
        car_top = y
        car_bottom = y + Car.height.value
        car_left = x
        car_right = x + Car.width.value
        obstacle_bottom = obs_start_y + obs_height
        obstacle_left = obs_start_x
        obstacle_right = obs_start_x + obs_width
        
        # Right Wall Crash
        if x > 690 - Car.width.value or x < 110:
            crash()
        # Left Wall Crash
        if x > _GameView.DISPLAY_WIDTH - (Car.width.value + 110) or x < 110:
            crash()

        # Car Collision
        if car_bottom > obs_start_y and car_top < obstacle_bottom:
            if car_right > obstacle_left and car_left < obstacle_right:
                crash()
        
        pauseButton_background = pygame.Surface((208, 68), pygame.SRCALPHA)
        pygame.draw.rect(pauseButton_background, (25, 118, 210, 255), (0, 0, 208, 68))
        _GameSetup.GAME_DISPLAYS.blit(pauseButton_background, (581, 11))
        button("Pause", 585, 15, 200, 60, _GameView.BLUE, _GameView.DARK_BLUE, "pause")
        
        pygame.display.update()
        _GameSetup.CLOCK.tick(60)


def _run_game() -> None:
    """Starts game runner."""
    _GameSetup.GAME.start()
    intro_loop()
    game_loop()
    _GameSetup.GAME.stop()


if __name__ == "__main__":
    _run_game()
