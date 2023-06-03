def rpsWinner(player1, player2) -> str:
    if player1 == "rock" and player2 == "paper":
        return "player 2"
    elif player1 == "rock" and player2 == "scissors":
        return "player 1"
    elif player1 == "rock" and player2 == "rock":
        return "tie"

    if player1 == "paper" and player2 == "paper":
        return "tie"
    elif player1 == "paper" and player2 == "scissors":
        return "player 2"
    elif player1 == "paper" and player2 == "rock":
        return "player 1"

    if player1 == "scissors" and player2 == "paper":
        return "player 1"
    elif player1 == "scissors" and player2 == "scissors":
        return "tie"
    elif player1 == "scissors" and player2 == "rock":
        return "player 2"

