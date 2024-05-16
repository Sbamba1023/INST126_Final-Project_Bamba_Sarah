import random

def roll_dice(num_dice=3):
    """Roll the specific number of dice and produce the results."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def check_tuple(rolls):
    """Check and see if all dice have the same value (tuple out)."""
    return len(set(rolls)) == 1

def check_doubles(rolls):
    """Check and see if two dice have the same value (fixed dice)."""
    return len(set(rolls)) == 2

def get_score(rolls):
    """Calculate the score based on the dice rolls."""
    if check_tuple(rolls):
        return 0
    else:
        return sum(rolls)

def play_turn(score):
    """Handle a player's turn, rolling dice and updating the score."""
    turn_score = 0
    fixed_dice = []
    while True:
        rolls = roll_dice()
        if check_tuple(rolls):
            print("Tupled out! Turn score: 0")
            return score
        if check_doubles(rolls):
            fixed_dice = [roll for roll in rolls if rolls.count(roll) > 1]
            unfixed_rolls = [roll for roll in rolls if roll not in fixed_dice]
            print(f"Rolled: {rolls} (Fixed: {fixed_dice})")
            if not unfixed_rolls:
                turn_score = get_score(rolls)
                break
        else:
            print(f"Rolled: {rolls}")
            turn_score = get_score(rolls)
            break
    print(f"Turn score: {turn_score}")
    return score + turn_score


def play_game(num_players, target_score=50, max_turns=5):
    """Play the "Tuple Out" Dice Game."""
    scores = [0] * num_players
    turn = 0
    while max(scores) < target_score and turn < max_turns:
        player = turn % num_players
        print(f"\nPlayer {player + 1}'s turn (Score: {scores[player]})")
        scores[player] = play_turn(scores[player])
        turn += 1
        print(f"\nCurrent scores: {scores}")
    if max(scores) >= target_score:
        winner = max(enumerate(scores), key=lambda x: x[1])
        print(f"\nPlayer {winner[0] + 1} wins with a score of {winner[1]}!")
    else:
        print("\nGame over! No one reached the target score.")

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    play_game(num_players)
