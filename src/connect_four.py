class ConnectFourGame:
    def __init__(self):
        # A cozy little Connect Four board for our players.
        self.board = [['🔵' for _ in range(7)] for _ in range(6)]
        self.current_token = '🔴'  # The red player goes first!

    def show_board(self):
        # Let's print out the board so players can see the current state.
        print("\nCurrent board:")
        for row in self.board:
            print("  ".join(row))
        print("\nChoose a column number from 1 to 7:")

    def place_token(self, column):
        # Attempt to place a token in the chosen column.
        if 1 <= column <= 7:
            column -= 1  # Adjusting because humans count from 1, not 0 like computers.
            for row in reversed(self.board):
                if row[column] == '🔵':  # Look for the first empty space from the bottom.
                    row[column] = self.current_token
                    return True
            print("Whoops, that column's full. Try a different one!")
        else:
            print("Hmm, that's not right. Pick a number between 1 and 7, please!")
        return False

    def alternate_turn(self):
        # Time to give the other player a turn.
        self.current_token = '🟡' if self.current_token == '🔴' else '🔴'

    def check_victory(self):
        # Define the rules for winning the game. Left as an exercise.
        pass

    def play(self):
        # This is where the fun begins and the game is played.
        while True:
            self.show_board()
            try:
                chosen_column = int(input(f"Player with the {self.current_token}, it's your move: "))
                if self.place_token(chosen_column):
                    if self.check_victory():
                        print(f"Wow! The player with the {self.current_token} token wins!")
                        self.show_board()
                        break
                    self.alternate_turn()
            except ValueError:
                print("Let's stick to numbers for the column choice, okay?")
            
# Let the game begin!
new_game = ConnectFourGame()
new_game.play()
