from dataclasses import dataclass
import random
from typing import Tuple

# State Model

@dataclass
class GameState:
    round: int = 0
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False

# Tools

def validate_move(move: str, bomb_used: bool) -> Tuple[bool, str]:
    valid_moves = {"rock", "paper", "scissors", "bomb"}
    move = move.strip().lower()

    if move not in valid_moves:
        return False, "Invalid input (choose rock/paper/scissors/bomb)"

    if move == "bomb" and bomb_used:
        return False, "Bomb already used (only once allowed)"

    return True, move


def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"

    if bot_move == "bomb":
        return "bot"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    return "user" if beats[user_move] == bot_move else "bot"


def apply_outcome(state: GameState, outcome: str) -> None:
    if outcome == "user":
        state.user_score += 1
    elif outcome == "bot":
        state.bot_score += 1

    state.round += 1

# Bot Policy

def bot_move(state: GameState) -> str:
    if not state.bot_bomb_used and random.random() < 0.2:
        state.bot_bomb_used = True
        return "bomb"

    return random.choice(["rock", "paper", "scissors"])

# Referee Agent

class RefereeAgent:
    def __init__(self):
        self.state = GameState()

    def show_rules(self) -> None:
        print("\n========================================")
        print(" Rock–Paper–Scissors–Plus (Best of 3)")
        print("========================================")
        print("Valid moves: rock, paper, scissors, bomb")
        print("Bomb beats all moves, but can be used once.")
        print("Bomb vs Bomb → Draw")
        print("Invalid move wastes the round.")
        print("========================================\n")

    def play_round(self) -> None:
        s = self.state

        print(f"--- Round {s.round + 1} of 3 ---")
        user_input = input("Enter your move: ")

        ok, user_move = validate_move(user_input, s.user_bomb_used)

        if not ok:
            print(f" {user_move}")
            print("Round wasted.\n")
            s.round += 1
            return

        if user_move == "bomb":
            s.user_bomb_used = True

        bot_choice = bot_move(s)

        outcome = resolve_round(user_move, bot_choice)
        apply_outcome(s, outcome)

        print("\nReferee Decision:")
        print(f"  You played : {user_move}")
        print(f"  Bot played : {bot_choice}")

        if outcome == "draw":
            print("  Outcome    : Draw round")
        elif outcome == "user":
            print("  Outcome    : You win the round ")
        else:
            print("  Outcome    : Bot wins the round ")

        print("\nCurrent Score:")
        print(f"  You : {s.user_score}")
        print(f"  Bot : {s.bot_score}")
        print("----------------------------------------\n")

    def final_result(self) -> None:
        s = self.state

        print("\n========================================")
        print("🏁 Game Finished (3 rounds complete)")
        print("========================================")

        if s.user_score > s.bot_score:
            print("Final Winner: YOU ")
        elif s.bot_score > s.user_score:
            print("Final Winner: BOT ")
        else:
            print("Final Result: DRAW ")

        print("========================================\n")

    def run(self) -> None:
        self.show_rules()

        while self.state.round < 3:
            self.play_round()

        self.final_result()


# Entry Point

if __name__ == "__main__":
    RefereeAgent().run()
