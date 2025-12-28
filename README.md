# The Farmer Was Replaced Scripts

A collection of automation scripts for [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/), a programming game where you code a drone to automate farming.

## IDE Development Support

Stub modules (`utils.py`, `instances.py`) that mirror the game's API, enabling:

- Autocompletion in your IDE
- Syntax checking outside the game
- Faster iteration during script development

## Features

### Maze Navigation (`maze.py`)

Implements the **right-hand wall follower algorithm** to solve in-game mazes and collect treasures.

## Usage

1. Develop scripts locally with full IDE support
2. Copy the relevant code into the game's built-in editor
3. Run and profit 🌾

## Project Structure

```text
├── instances.py   # Game API stubs (constants & enums)
├── utils.py       # Game API stubs (functions)
├── maze.py        # Maze solving algorithm
└── main.py        # Entry point (WIP)
```

## License

MIT
