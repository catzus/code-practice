import random
import time
import tkinter as tk
from tkinter import messagebox
import os
import json
import matplotlib.pyplot as plt

class ArithmeticGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Game")
        self.root.configure(bg="#2E2E2E")  # Dark background theme

        # Initialize game variables
        self.score = 0
        self.current_answer = None
        self.selected_operations = []
        self.start_time = None
        self.duration = 120  # Default duration in seconds
        self.awaiting_next_question = False  # Flag to prevent multiple triggers

        # File to store scores
        self.scores_file = "scores.json"

        # Create GUI frames
        self.create_settings_frame()
        self.create_game_frame()

    def create_settings_frame(self):
        """Creates the settings frame where users can select operations, ranges, and duration."""
        self.settings_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.settings_frame.pack(pady=20)

        # Operation Selection
        tk.Label(
            self.settings_frame,
            text="Choose Operations:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 12)
        ).grid(row=0, column=0, columnspan=4, pady=5, sticky="w")

        self.addition_var = tk.BooleanVar(value=True)
        self.subtraction_var = tk.BooleanVar(value=True)
        self.multiplication_var = tk.BooleanVar(value=True)
        self.division_var = tk.BooleanVar(value=True)

        tk.Checkbutton(
            self.settings_frame,
            text="Addition",
            variable=self.addition_var,
            bg="#2E2E2E",
            fg="white",
            selectcolor="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=1, column=0, sticky="w", padx=5)

        tk.Checkbutton(
            self.settings_frame,
            text="Subtraction",
            variable=self.subtraction_var,
            bg="#2E2E2E",
            fg="white",
            selectcolor="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=1, column=1, sticky="w", padx=5)

        tk.Checkbutton(
            self.settings_frame,
            text="Multiplication",
            variable=self.multiplication_var,
            bg="#2E2E2E",
            fg="white",
            selectcolor="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=1, column=2, sticky="w", padx=5)

        tk.Checkbutton(
            self.settings_frame,
            text="Division",
            variable=self.division_var,
            bg="#2E2E2E",
            fg="white",
            selectcolor="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=1, column=3, sticky="w", padx=5)

        # Separator
        tk.Label(
            self.settings_frame,
            text="-"*60,
            fg="white",
            bg="#2E2E2E"
        ).grid(row=2, column=0, columnspan=4, pady=10)

        # Range Selection for Addition and Subtraction
        tk.Label(
            self.settings_frame,
            text="Addition & Subtraction Range:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10, "bold")
        ).grid(row=3, column=0, columnspan=4, pady=5, sticky="w")

        tk.Label(
            self.settings_frame,
            text="1st Number:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=4, column=0, pady=5, sticky="e")

        self.add_sub_min_entry = tk.Entry(self.settings_frame, width=5)
        self.add_sub_min_entry.grid(row=4, column=1, padx=5, pady=5)
        self.add_sub_min_entry.insert(0, "2")

        self.add_sub_max_entry = tk.Entry(self.settings_frame, width=5)
        self.add_sub_max_entry.grid(row=4, column=2, padx=5, pady=5)
        self.add_sub_max_entry.insert(0, "100")

        tk.Label(
            self.settings_frame,
            text="2nd Number:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=5, column=0, pady=5, sticky="e")

        self.add_sub_min_entry2 = tk.Entry(self.settings_frame, width=5)
        self.add_sub_min_entry2.grid(row=5, column=1, padx=5, pady=5)
        self.add_sub_min_entry2.insert(0, "2")

        self.add_sub_max_entry2 = tk.Entry(self.settings_frame, width=5)
        self.add_sub_max_entry2.grid(row=5, column=2, padx=5, pady=5)
        self.add_sub_max_entry2.insert(0, "100")

        # Range Selection for Multiplication and Division
        tk.Label(
            self.settings_frame,
            text="Multiplication & Division Range:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10, "bold")
        ).grid(row=6, column=0, columnspan=4, pady=10, sticky="w")

        tk.Label(
            self.settings_frame,
            text="1st Number:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=7, column=0, pady=5, sticky="e")

        self.mul_div_min_entry = tk.Entry(self.settings_frame, width=5)
        self.mul_div_min_entry.grid(row=7, column=1, padx=5, pady=5)
        self.mul_div_min_entry.insert(0, "2")

        self.mul_div_max_entry = tk.Entry(self.settings_frame, width=5)
        self.mul_div_max_entry.grid(row=7, column=2, padx=5, pady=5)
        self.mul_div_max_entry.insert(0, "12")

        tk.Label(
            self.settings_frame,
            text="2nd Number:",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=8, column=0, pady=5, sticky="e")

        self.mul_div_min_entry2 = tk.Entry(self.settings_frame, width=5)
        self.mul_div_min_entry2.grid(row=8, column=1, padx=5, pady=5)
        self.mul_div_min_entry2.insert(0, "2")

        self.mul_div_max_entry2 = tk.Entry(self.settings_frame, width=5)
        self.mul_div_max_entry2.grid(row=8, column=2, padx=5, pady=5)
        self.mul_div_max_entry2.insert(0, "100")

        # Separator
        tk.Label(
            self.settings_frame,
            text="-"*60,
            fg="white",
            bg="#2E2E2E"
        ).grid(row=9, column=0, columnspan=4, pady=10)

        # Duration
        tk.Label(
            self.settings_frame,
            text="Game Duration (seconds):",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 10)
        ).grid(row=10, column=0, pady=5, sticky="e")

        self.duration_entry = tk.Entry(self.settings_frame, width=5)
        self.duration_entry.grid(row=10, column=1, padx=5, pady=5)
        self.duration_entry.insert(0, "120")  # Default duration set to 120 seconds

        # Start Button
        start_button = tk.Button(
            self.settings_frame,
            text="Start Game",
            command=self.start_game,
            bg="#00A2FF",
            fg="white",
            font=("Arial", 12),
            width=20
        )
        start_button.grid(row=11, column=0, columnspan=4, pady=20)

        # Bind Enter key to start the game (only when in settings)
        self.root.bind('<Return>', self.start_game)

    def create_game_frame(self):
        """Creates the game frame where questions are displayed and answered."""
        self.game_frame = tk.Frame(self.root, bg="#2E2E2E")

        # Timer and Score Labels
        self.timer_label = tk.Label(
            self.game_frame,
            text=f"Seconds left: {self.duration}",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 14)
        )
        self.timer_label.pack(anchor="nw", padx=10, pady=10)

        self.score_label = tk.Label(
            self.game_frame,
            text="Score: 0",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 14)
        )
        self.score_label.pack(anchor="ne", padx=10, pady=10)

        # Frame for Question and Answer Entry on the Same Line
        qa_frame = tk.Frame(self.game_frame, bg="#2E2E2E")
        qa_frame.pack(pady=20)

        self.question_label = tk.Label(
            qa_frame,
            text="",
            fg="white",
            bg="#2E2E2E",
            font=("Arial", 24)
        )
        self.question_label.pack(side="left")

        self.answer_entry = tk.Entry(
            qa_frame,
            font=("Arial", 24),
            width=10,  # Increased width
            justify="center"
        )
        self.answer_entry.pack(side="left", padx=10)
        self.answer_entry.bind("<KeyRelease>", self.check_answer)  # Bind KeyRelease event

    def generate_problem(self, operation, ranges):
        """Generates a math problem based on the operation and provided ranges."""
        if operation in ["addition", "subtraction"]:
            num1 = random.randint(*ranges['add_sub']['range1'])
            num2 = random.randint(*ranges['add_sub']['range2'])
        elif operation in ["multiplication", "division"]:
            if operation == "division":
                # Generate all valid (num1, num2) pairs
                valid_pairs = []
                for num1 in range(ranges['mul_div']['range1'][0], ranges['mul_div']['range1'][1] + 1):
                    for num2 in range(ranges['mul_div']['range2'][0], ranges['mul_div']['range2'][1] + 1):
                        if num2 != 1 and num2 != num1 and num1 % num2 == 0:
                            valid_pairs.append((num1, num2))
                if not valid_pairs:
                    raise ValueError("No valid division problems available with the current settings.")
                num1, num2 = random.choice(valid_pairs)
            else:
                num1 = random.randint(*ranges['mul_div']['range1'])
                num2 = random.randint(*ranges['mul_div']['range2'])

        if operation == "addition":
            return f"{num1} + {num2}", num1 + num2
        elif operation == "subtraction":
            # Ensure no negative results
            num1, num2 = max(num1, num2), min(num1, num2)
            return f"{num1} - {num2}", num1 - num2
        elif operation == "multiplication":
            return f"{num1} × {num2}", num1 * num2
        elif operation == "division":
            return f"{num1} ÷ {num2}", num1 // num2

    def update_timer(self):
        """Updates the timer on the GUI."""
        if self.start_time is None:
            return

        elapsed_time = int(time.time() - self.start_time)
        remaining_time = self.duration - elapsed_time

        if remaining_time >= 0:
            self.timer_label.config(text=f"Seconds left: {remaining_time}")
            self.root.after(1000, self.update_timer)
        else:
            self.save_score()
            average = self.calculate_average_score()
            self.plot_progress()
            messagebox.showinfo(
                "Time's Up",
                f"Game Over!\nYour Score: {self.score}\nAverage Score: {average:.2f}"
            )
            self.ask_restart()

    def save_score(self):
        """Saves the final score along with settings to the scores file."""
        score_data = {
            "score": self.score,
            "settings": {
                "addition": self.addition_var.get(),
                "subtraction": self.subtraction_var.get(),
                "multiplication": self.multiplication_var.get(),
                "division": self.division_var.get(),
                "add_sub_range1": [int(self.add_sub_min_entry.get()), int(self.add_sub_max_entry.get())],
                "add_sub_range2": [int(self.add_sub_min_entry2.get()), int(self.add_sub_max_entry2.get())],
                "mul_div_range1": [int(self.mul_div_min_entry.get()), int(self.mul_div_max_entry.get())],
                "mul_div_range2": [int(self.mul_div_min_entry2.get()), int(self.mul_div_max_entry2.get())],
                "duration": self.duration
            },
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            if not os.path.exists(self.scores_file):
                with open(self.scores_file, 'w') as f:
                    json.dump([score_data], f, indent=4)
            else:
                with open(self.scores_file, 'r') as f:
                    data = json.load(f)
                data.append(score_data)
                with open(self.scores_file, 'w') as f:
                    json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred while saving the score:\n{e}")

    def calculate_average_score(self):
        """Calculates the average score from all saved scores with the same settings."""
        if not os.path.exists(self.scores_file):
            return 0.0  # No scores yet

        try:
            with open(self.scores_file, 'r') as f:
                data = json.load(f)

            # Current settings for matching
            current_settings = {
                "addition": self.addition_var.get(),
                "subtraction": self.subtraction_var.get(),
                "multiplication": self.multiplication_var.get(),
                "division": self.division_var.get(),
                "add_sub_range1": [int(self.add_sub_min_entry.get()), int(self.add_sub_max_entry.get())],
                "add_sub_range2": [int(self.add_sub_min_entry2.get()), int(self.add_sub_max_entry2.get())],
                "mul_div_range1": [int(self.mul_div_min_entry.get()), int(self.mul_div_max_entry.get())],
                "mul_div_range2": [int(self.mul_div_min_entry2.get()), int(self.mul_div_max_entry2.get())],
                "duration": self.duration
            }

            matching_scores = [
                entry["score"] for entry in data
                if entry["settings"] == current_settings
            ]

            if not matching_scores:
                return 0.0

            return sum(matching_scores) / len(matching_scores)
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred while reading scores:\n{e}")
            return 0.0

    def ask_restart(self):
        """Asks the user if they want to restart the game."""
        if messagebox.askyesno("Restart", "Do you want to play again?"):
            self.reset_game()
        else:
            self.root.destroy()

    def ask_question(self):
        """Presents a question to the user based on enabled operations."""
        if not self.selected_operations:
            return

        operation = random.choice(self.selected_operations)
        ranges = {
            'add_sub': {
                'range1': (int(self.add_sub_min_entry.get()), int(self.add_sub_max_entry.get())),
                'range2': (int(self.add_sub_min_entry2.get()), int(self.add_sub_max_entry2.get()))
            },
            'mul_div': {
                'range1': (int(self.mul_div_min_entry.get()), int(self.mul_div_max_entry.get())),
                'range2': (int(self.mul_div_min_entry2.get()), int(self.mul_div_max_entry2.get()))
            }
        }
        try:
            problem, answer = self.generate_problem(operation, ranges)
            self.current_answer = answer
            self.question_label.config(text=f"{problem} = ")
            self.answer_entry.delete(0, tk.END)
            self.awaiting_next_question = False  # Reset the flag
            self.answer_entry.focus_set()
        except ValueError as ve:
            messagebox.showerror("Problem Generation Error", f"{ve}")
            # Optionally, remove the problematic operation and try again
            self.selected_operations.remove(operation)
            if self.selected_operations:
                self.ask_question()
            else:
                messagebox.showinfo("No Valid Problems", "No valid division problems available with the current settings.")
                self.ask_restart()

    def check_answer(self, event=None):
        """Checks the user's answer and moves to the next question if correct."""
        if self.awaiting_next_question:
            return  # Prevent multiple triggers

        user_input = self.answer_entry.get().strip()
        if not user_input:
            return  # Do nothing for empty input

        # Allow negative numbers and handle non-integer inputs gracefully
        try:
            user_answer = int(user_input)
            if user_answer == self.current_answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.awaiting_next_question = True  # Set flag to prevent re-triggering
                self.ask_question()  # Immediately move to next question
        except ValueError:
            # Non-integer input; ignore or optionally provide feedback
            pass

    def start_game(self, event=None):
        """Starts the game with user-defined settings."""
        try:
            # Read input ranges and duration
            add_sub_min1 = int(self.add_sub_min_entry.get())
            add_sub_max1 = int(self.add_sub_max_entry.get())
            add_sub_min2 = int(self.add_sub_min_entry2.get())
            add_sub_max2 = int(self.add_sub_max_entry2.get())

            mul_div_min1 = int(self.mul_div_min_entry.get())
            mul_div_max1 = int(self.mul_div_max_entry.get())
            mul_div_min2 = int(self.mul_div_min_entry2.get())
            mul_div_max2 = int(self.mul_div_max_entry2.get())

            duration = int(self.duration_entry.get())

            if (add_sub_min1 > add_sub_max1) or (add_sub_min2 > add_sub_max2):
                raise ValueError("Addition/Subtraction: Minimum range cannot exceed maximum range.")
            if (mul_div_min1 > mul_div_max1) or (mul_div_min2 > mul_div_max2):
                raise ValueError("Multiplication/Division: Minimum range cannot exceed maximum range.")
            if duration <= 0:
                raise ValueError("Duration must be a positive integer.")

            # Collect selected operations
            self.selected_operations = []
            if self.addition_var.get():
                self.selected_operations.append("addition")
            if self.subtraction_var.get():
                self.selected_operations.append("subtraction")
            if self.multiplication_var.get():
                self.selected_operations.append("multiplication")
            if self.division_var.get():
                self.selected_operations.append("division")

            if not self.selected_operations:
                messagebox.showerror("Selection Error", "Please select at least one operation.")
                return

            # Hide settings and display game
            self.settings_frame.pack_forget()
            self.game_frame.pack(fill="both", expand=True)

            # Initialize game variables
            self.score = 0
            self.score_label.config(text="Score: 0")
            self.duration = duration
            self.timer_label.config(text=f"Seconds left: {self.duration}")
            self.start_time = time.time()
            self.update_timer()
            self.ask_question()
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Please enter valid numbers for ranges and duration.\n{ve}")

    def reset_game(self):
        """Resets the game to initial settings."""
        self.score = 0
        self.current_answer = None
        self.start_time = None
        self.selected_operations = []
        self.duration = 120
        self.awaiting_next_question = False

        # Reset entries to default values
        # Addition & Subtraction Ranges
        self.add_sub_min_entry.delete(0, tk.END)
        self.add_sub_min_entry.insert(0, "2")
        self.add_sub_max_entry.delete(0, tk.END)
        self.add_sub_max_entry.insert(0, "100")
        self.add_sub_min_entry2.delete(0, tk.END)
        self.add_sub_min_entry2.insert(0, "2")
        self.add_sub_max_entry2.delete(0, tk.END)
        self.add_sub_max_entry2.insert(0, "100")

        # Multiplication & Division Ranges
        self.mul_div_min_entry.delete(0, tk.END)
        self.mul_div_min_entry.insert(0, "2")
        self.mul_div_max_entry.delete(0, tk.END)
        self.mul_div_max_entry.insert(0, "12")
        self.mul_div_min_entry2.delete(0, tk.END)
        self.mul_div_min_entry2.insert(0, "2")
        self.mul_div_max_entry2.delete(0, tk.END)
        self.mul_div_max_entry2.insert(0, "100")

        # Duration
        self.duration_entry.delete(0, tk.END)
        self.duration_entry.insert(0, "120")

        # Reset operation selections
        self.addition_var.set(True)
        self.subtraction_var.set(True)
        self.multiplication_var.set(True)
        self.division_var.set(True)

        # Show settings and hide game
        self.game_frame.pack_forget()
        self.settings_frame.pack(pady=20)

    def plot_progress(self):
        """Plots the user's scores over trials for the current settings."""
        try:
            with open(self.scores_file, 'r') as f:
                data = json.load(f)

            # Extract scores matching current settings
            current_settings = {
                "addition": self.addition_var.get(),
                "subtraction": self.subtraction_var.get(),
                "multiplication": self.multiplication_var.get(),
                "division": self.division_var.get(),
                "add_sub_range1": [int(self.add_sub_min_entry.get()), int(self.add_sub_max_entry.get())],
                "add_sub_range2": [int(self.add_sub_min_entry2.get()), int(self.add_sub_max_entry2.get())],
                "mul_div_range1": [int(self.mul_div_min_entry.get()), int(self.mul_div_max_entry.get())],
                "mul_div_range2": [int(self.mul_div_min_entry2.get()), int(self.mul_div_max_entry2.get())],
                "duration": self.duration
            }

            matching_scores = [
                entry["score"] for entry in data
                if entry["settings"] == current_settings
            ]

            if not matching_scores:
                return  # No matching scores to plot

            trials = list(range(1, len(matching_scores) + 1))
            plt.figure(figsize=(10, 5))
            plt.plot(trials, matching_scores, marker='o', linestyle='-', color='blue')
            plt.title("Score Progress Over Trials")
            plt.xlabel("Trial Number")
            plt.ylabel("Score")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("Plot Error", f"An error occurred while plotting progress:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ArithmeticGame(root)
    root.mainloop()
