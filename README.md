# Rock–Paper–Scissors–Plus Referee Agent

This project implements a minimal conversational referee bot for the game  
**Rock–Paper–Scissors–Plus**, played between a user and the bot.

The goal is to enforce game rules, persist state across turns, and provide
clear round-by-round feedback in a simple CLI chat loop.

---

## Game Rules Implemented

- The game runs for exactly **3 rounds** (best of 3).
- Valid moves:
  - rock
  - paper
  - scissors
  - bomb (allowed only once per player)
- Bomb beats all other moves.
- Bomb vs Bomb results in a draw.
- Invalid input wastes the round automatically.
- After 3 rounds, the game ends with a final winner or draw.

---

## State Model

The game uses a persistent `GameState` dataclass that tracks:

- Current round number
- User score and bot score
- Whether the user has already used bomb
- Whether the bot has already used bomb

This ensures the game behaves as a state machine across multiple turns,
instead of relying on prompt-only memory.

---

## Tool / Function Design

Core logic is separated into explicit tool-like functions:

### `validate_move`
Handles intent validation and constraint checks:
- Ensures input is one of the valid moves
- Prevents bomb reuse

### `resolve_round`
Encapsulates the winner resolution logic:
- Draw handling
- Bomb dominance rules
- Standard rock-paper-scissors outcomes

### `apply_outcome`
Responsible for state mutation:
- Updates scores
- Advances the round counter

This separation makes the agent easier to extend and debug.

---

## Agent Boundary & Flow

The `RefereeAgent` class acts as the conversational controller:

- Displays rules at the start
- Prompts the user each round
- Uses tools for validation, resolution, and state updates
- Generates clear referee-style responses
- Ends automatically after 3 rounds

Responsibilities are cleanly divided between:
- Intent understanding (validation)
- Game logic (winner decision)
- State persistence (mutations)
- Response formatting (user-visible output)

---

## Tradeoffs

- Implemented as a lightweight CLI loop instead of a hosted server or UI,
  as required by the assignment constraints.
- Bot strategy is intentionally simple (random play + optional bomb usage).

---

## Improvements With More Time

Given more development time, I would add:

- Smarter bot decision-making instead of random strategy
- More natural language understanding (e.g., "I choose rock")
- Structured tool registration using full Google ADK runtime primitives
- Better conversational UX for edge cases and replay support

---

## How to Run

```bash
python rps_plus_referee.py
