class ConnectFourGame:
    def __init__(self):
        #  A cozy little Connect Four board for our players.
        self.board = [['🔵' for _ in range(7)] for _ in range(6)]
        self.current_token = '🔴'  # Player red goes first!

    def show_board(self):
        # Let's print out the board so players can see the current state.
        print("\nCurrent board:")
        for row in self.board:
            print("  ".join(row))
        print("\nChoose a column number from 1 to 7 or type 'e' to exit:")

    def place_token(self, column):
        #  Attempt to place a token in the chosen column.
        if 1 <= column <= 7:
            column -= 1
            for row in reversed(self.board):
                if row[column] == '🔵':
                    row[column] = self.current_token
                    return True
            print("Ohh, that column's full. Maybe a different one!")
        else:
            print("Well, that's not okay. You have to pick a number between 1 and 7, Understood!")
        return False

    def alternate_turn(self):
        # Time to give the other player a turn.
        self.current_token = '🟡' if self.current_token == '🔴' else '🔴'

    def check_victory(self):
        # Check for horizontal, vertical, and diagonal wins
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == '🔵': continue  
                
                # Check horizontal
                if col <= 3 and all(self.board[row][col+i] == self.current_token for i in range(4)):
                    return True
                
                # Check vertical
                if row <= 2 and all(self.board[row+i][col] == self.current_token for i in range(4)):
                    return True
                
                # Check diagonal (down-right and down-left)
                if row <= 2 and col <= 3 and all(self.board[row+i][col+i] == self.current_token for i in range(4)):
                    return True
                if row <= 2 and col >= 3 and all(self.board[row+i][col-i] == self.current_token for i in range(4)):
                    return True
        return False
    
    
    def check_draw(self):
        # If there is no cells empty ('🔵'), it's a draw
        return all(cell != '🔵' for row in self.board for cell in row)

    def play(self):
        # Modified to include a quit option and draw check
        while True:
            self.show_board()
            user_input = input(f"Player with the {self.current_token}, it's your move (type 'e' to exit): ")
            if user_input.lower() == 'q':
                print("Game ended by the player.")
                break  # Exit the game loop
            
            try:
                chosen_column = int(user_input)
                if self.place_token(chosen_column):
                    if self.check_victory():
                        print(f"Wohoo! The player with the {self.current_token} token winner!")
                        self.show_board()
                        break  # Exit the game loop
                    elif self.check_draw():
                        print("The game is a draw!")
                        self.show_board()
                        break  # Exit the game loop
                    self.alternate_turn()
            except ValueError:
                print("Invalid input. Please enter a number between 1 to 7, or 'e' to exit1.")

# Let the game begin!
new_game = ConnectFourGame()
new_game.play()
