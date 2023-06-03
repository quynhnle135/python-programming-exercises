from rock_paper_scissors import rpsWinner


def main():
    player1 = input("Hey player 1! Rock, Paper, Scissors: ")
    player2 = input("Player 2! Rock, Paper, Scissors: ")
    print(f"Result: {rpsWinner(player1, player2)}")


if __name__ == "__main__":
    main()