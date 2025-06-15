import random

celebrities_net_worth = {
    "Elon Musk": 210_000_000_000,
    "Oprah Winfrey": 2_800_000_000,
    "Taylor Swift": 1_100_000_000,
    "Kanye West": 400_000_000,
    "Rihanna": 1_400_000_000,
    "Dwayne Johnson": 800_000_000,
    "Kim Kardashian": 1_700_000_000,
    "Tom Cruise": 600_000_000,
    "Beyoncé": 540_000_000,
    "Shah Rukh Khan": 770_000_000,
}

celebrities = list(celebrities_net_worth.items())


def get_random_celebrity(exclude=None):
    """Returns a random celebrity, optionally excluding one."""
    options = [c for c in celebrities if c != exclude]
    return random.choice(options)


def higher_lower_game():
    score = 0
    game_over = False

    celeb_a = get_random_celebrity()
    celeb_b = get_random_celebrity(exclude=celeb_a)

    while not game_over:
        print("\nWho has a higher net worth?")
        print(f"A: {celeb_a[0]}")
        print("    VS")
        print(f"B: {celeb_b[0]}")

        choice = input("Type 'A' or 'B': ").strip().upper()

        # Determine which is higher
        if celeb_a[1] > celeb_b[1]:
            correct_answer = "A"
        else:
            correct_answer = "B"

        if choice == correct_answer:
            score += 1
            print(f"✅ Correct! Current score: {score}")
            # The correct celeb stays, new opponent comes in
            celeb_a = celeb_a if choice == "A" else celeb_b
            celeb_b = get_random_celebrity(exclude=celeb_a)
        else:
            print(
                f"❌ Wrong! {celeb_a[0]}: ${celeb_a[1]:,}, {celeb_b[0]}: ${celeb_b[1]:,}"
            )
            print(f"Your final score: {score}")
            game_over = True


# Start the game
higher_lower_game()
