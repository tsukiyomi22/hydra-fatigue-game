# Hydra Fatigue Game

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/release/python-370/)
[![License](https://img.shields.io/github/license/yourusername/hydra-fatigue-game)](https://opensource.org/licenses/MIT)

## Description

**Hydra Fatigue Game** is a simple, engaging game designed to help players understand and practice fatigue management in a fun and interactive way. The game features an adjustable difficulty level that can be tailored to suit the skill level of individual players.

## Features

- **Interactive game interface**: Players control a character to navigate through obstacles while avoiding collisions.
- **Score tracking**: The game keeps track of your score based on how long you avoid obstacles, promoting better fatigue management skills.
- **Adjustable difficulty levels**: Customize the challenge level to suit your current state of alertness and fatigue tolerance.

## Installation

To install the Hydra Fatigue Game, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hydra-fatigue-game.git
   cd hydra-fatigue-game
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To play the game, simply run the `main.py` script:

```bash
python main.py
```

The game will launch in a window where you can use the arrow keys to move your character and avoid obstacles. The difficulty level is set to medium by default, but you can adjust it using the `--difficulty` flag:

```bash
python main.py --difficulty easy
```

Available difficulty levels are `easy`, `medium`, and `hard`.

### Example Code Snippet

Here's a simple example of how to start the game with an easy difficulty level:

```python
from hydra_fatigue_game import main

def main():
    # Start the game with easy difficulty
    main.start(difficulty='easy')

if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

---

Thank you for using Hydra Fatigue Game! We hope it helps you manage fatigue more effectively and enjoyably.