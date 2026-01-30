```python
import random
import pygame
from typing import List, Tuple

class HydraGame:
    def __init__(self, width: int, height: int, difficulty: str = "easy"):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.score = 0
        self.fatigue_points = 100
        self.obstacles = []
        self.player_position = (width // 2, height // 2)
        self.initialize_game()

    def initialize_game(self):
        if self.difficulty == "easy":
            self.max_obstacles = 5
        elif self.difficulty == "medium":
            self.max_obstacles = 10
        else:
            self.max_obstacles = 20

    def add_obstacle(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        self.obstacles.append((x, y))

    def update_game(self):
        if len(self.obstacles) < self.max_obstacles:
            self.add_obstacle()
        for obstacle in self.obstacles:
            distance = ((obstacle[0] - self.player_position[0]) ** 2 + (obstacle[1] - self.player_position[1]) ** 2) ** 0.5
            if distance < 20:
                self.fatigue_points -= 10
        self.obstacles = [obs for obs in self.obstacles if ((obs[0] - self.player_position[0]) ** 2 + (obs[1] - self.player_position[1]) ** 2) > 400]

    def draw(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), self.player_position, 10)
        for obstacle in self.obstacles:
            pygame.draw.circle(screen, (0, 0, 0), obstacle, 10)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score} Fatigue: {self.fatigue_points}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])
                    elif event.key == pygame.K_RIGHT:
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                    elif event.key == pygame.K_UP:
                        self.player_position = (self.player_position[0], self.player_position[1] - 1)
                    elif event.key == pygame.K_DOWN:
                        self.player_position = (self.player_position[0], self.player_position[1] + 1)
            self.update_game()
            self.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

def main():
    game = HydraGame(400, 400, "easy")
    game.run()

if __name__ == "__main__":
    main()