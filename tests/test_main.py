```python
import pytest
import pygame
from hydra_game import HydraGame

@pytest.fixture
def game():
    return HydraGame(400, 400, "easy")

def test_initialization(game):
    assert game.width == 400
    assert game.height == 400
    assert game.difficulty == "easy"
    assert game.score == 0
    assert game.fatigue_points == 100
    assert len(game.obstacles) == 0
    assert game.player_position == (200, 200)

def test_add_obstacle(game):
    for _ in range(5):
        game.add_obstacle()
    assert len(game.obstacles) <= 5

def test_update_game(game):
    game.player_position = (20, 20)
    game.obstacles = [(18, 18), (22, 22)]
    game.update_game()
    assert game.fatigue_points == 90
    assert len(game.obstacles) == 1

def test_draw(game):
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    game.draw(screen)
    pygame.quit()

def test_run(game):
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.player_position = (game.player_position[0] - 1, game.player_position[1])
                elif event.key == pygame.K_RIGHT:
                    game.player_position = (game.player_position[0] + 1, game.player_position[1])
                elif event.key == pygame.K_UP:
                    game.player_position = (game.player_position[0], game.player_position[1] - 1)
                elif event.key == pygame.K_DOWN:
                    game.player_position = (game.player_position[0], game.player_position[1] + 1)
        game.update_game()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()