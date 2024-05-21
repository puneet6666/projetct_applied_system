import tkinter as tk
from tkinter import messagebox
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYER_ONE = "red"
PLAYER_TWO = "yellow"

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_player = PLAYER_ONE
        self.game_mode = None
        self.move_history = []
        self.ai_difficulty = 1  # Default difficulty
        self.paused = False
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        tk.Label(self.menu_frame, text="Choose Game Mode", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.menu_frame, text="Player vs Player", command=self.start_pvp, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.menu_frame, text="Player vs AI", command=self.start_pvai, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.menu_frame, text="Settings", command=self.show_settings, font=("Arial", 14)).pack(pady=10)

    def show_settings(self):
        self.menu_frame.destroy()
        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack()

        tk.Label(self.settings_frame, text="Settings", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.settings_frame, text="AI Difficulty", font=("Arial", 14)).pack(pady=10)
        self.difficulty_var = tk.IntVar(value=self.ai_difficulty)
        tk.Radiobutton(self.settings_frame, text="Easy", variable=self.difficulty_var, value=1).pack()
        tk.Radiobutton(self.settings_frame, text="Medium", variable=self.difficulty_var, value=2).pack()
        tk.Radiobutton(self.settings_frame, text="Hard", variable=self.difficulty_var, value=3).pack()
        tk.Button(self.settings_frame, text="Save", command=self.save_settings, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.settings_frame, text="Back", command=self.back_to_menu, font=("Arial", 14)).pack(pady=10)

    def save_settings(self):
        self.ai_difficulty = self.difficulty_var.get()
        self.back_to_menu()

    def back_to_menu(self):
        self.settings_frame.destroy()
        self.create_menu()

    def start_pvp(self):
        self.game_mode = "PVP"
        self.menu_frame.destroy()
        self.create_widgets()

    def start_pvai(self):
        self.game_mode = "PVAI"
        self.menu_frame.destroy()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=700, height=600, bg="blue")
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_game, font=("Arial", 14))
        self.pause_button.pack(pady=10)
        self.history_button = tk.Button(self.root, text="Move History", command=self.show_history, font=("Arial", 14))
        self.history_button.pack(pady=10)

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                x1 = col * 100
                y1 = row * 100
                x2 = x1 + 100
                y2 = y1 + 100
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

    def handle_click(self, event):
        if self.paused:
            return
        col = event.x // 100
        if self.is_valid_location(col):
            self.handle_move(col)

    def handle_move(self, col):
        row = self.get_next_open_row(col)
        self.drop_piece(row, col, self.current_player)
        self.move_history.append((row, col, self.current_player))
        if self.winning_move(self.current_player):
            self.show_result(f"Player {self.current_player} wins!", self.current_player)
            return
        self.current_player = PLAYER_ONE if self.current_player == PLAYER_TWO else PLAYER_TWO
        if self.game_mode == "PVAI" and self.current_player == PLAYER_TWO:
            self.root.after(500, self.ai_move)

    def ai_move(self):
        if self.paused:
            return

        # AI logic with different difficulty levels
        col = self.choose_smart_move()
        self.handle_move(col)

    def choose_smart_move(self):
        # Check if AI can win in the next move
        for col in range(COLUMNS):
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.board[row][col] = PLAYER_TWO
                if self.winning_move(PLAYER_TWO):
                    self.board[row][col] = None
                    return col
                self.board[row][col] = None

        # Block opponent's winning move
        for col in range(COLUMNS):
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.board[row][col] = PLAYER_ONE
                if self.winning_move(PLAYER_ONE):
                    self.board[row][col] = None
                    return col
                self.board[row][col] = None

        # Choose the center column if it's available
        center_col = COLUMNS // 2
        if self.is_valid_location(center_col):
            return center_col

        # Choose a random valid column
        valid_columns = [c for c in range(COLUMNS) if self.is_valid_location(c)]
        return random.choice(valid_columns)

    def is_valid_location(self, col):
        return self.board[0][col] is None

    def get_next_open_row(self, col):
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] is None:
                return row

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece
        x1 = col * 100
        y1 = row * 100
        x2 = x1 + 100
        y2 = y1 + 100
        self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=piece)

    def winning_move(self, piece):
        # Check horizontal locations
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

        return False

    def show_result(self, message, winner):
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Over")
        result_window.geometry("300x200")

        tk.Label(result_window, text=message, font=("Arial", 16)).pack(pady=20)

        # Create a canvas to draw the colored circle
        circle_canvas = tk.Canvas(result_window, width=50, height=50)
        circle_canvas.pack(pady=10)
        circle_canvas.create_oval(5, 5, 45, 45, fill=winner)

        home_button = tk.Button(result_window, text="Home", command=lambda: self.go_home(result_window), font=("Arial", 12))
        home_button.pack(side="left", padx=20, pady=20)

        retry_button = tk.Button(result_window, text="Retry", command=lambda: self.retry_game(result_window), font=("Arial", 12))
        retry_button.pack(side="right", padx=20, pady=20)

    def pause_game(self):
        self.paused = not self.paused
        self.pause_button.config(text="Resume" if self.paused else "Pause")

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Move History")
        history_window.geometry("300x400")

        tk.Label(history_window, text="Move History", font=("Arial", 16)).pack(pady=20)

        history_text = tk.Text(history_window, wrap="word", font=("Arial", 12))
        history_text.pack(pady=10)

        for move in self.move_history:
            row, col, player = move
            history_text.insert(tk.END, f"Player {player} placed at row {row + 1}, column {col + 1}\n")

    def go_home(self, window):
        window.destroy()
        self.canvas.destroy()
        self.create_menu()

    def retry_game(self, window):
        window.destroy()
        self.reset_game()

    def reset_game(self):
        self.canvas.delete("all")
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_player = PLAYER_ONE
        self.move_history = []
        self.draw_board()

    def update_board(self):
        self.canvas.delete("all")
        self.draw_board()
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board[row][col] is not None:
                    x1 = col * 100
                    y1 = row * 100
                    x2 = x1 + 100
                    y2 = y1 + 100
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=self.board[row][col])

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
