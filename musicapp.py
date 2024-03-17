import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

print("Current Working Directory:", os.getcwd())

# Global variables to track correct and incorrect answers
correct_count = 0
incorrect_count = 0

# Start game function
def start_game():
    global correct_count, incorrect_count  # Use global keyword to access and modify global variables

    selected_clef = clef_var.get()
    print(f"Starting game with {selected_clef} clef.")
    
    game_window = tk.Toplevel(mainwindow)
    game_window.title("Game Window")

    # Function to generate a new note
    def generate_new_note():
        nonlocal selected_note_img, correct_answer  # Use nonlocal to access and modify variables in the parent function
        if selected_clef == "Treble":
            selected_note_img, correct_answer = random.choice(treble_notes_with_answers)
        elif selected_clef == "Bass":
            selected_note_img, correct_answer = random.choice(bass_notes_with_answers)
        elif selected_clef == "Alto":
            selected_note_img, correct_answer = random.choice(alto_notes_with_answers)
        
        # Load image
        try:
            absolute_path = os.path.abspath(selected_note_img)
            print(f"Attempting to open image: {absolute_path}")
            image = Image.open(absolute_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)

            # Update the image on the label
            image_label.config(image=photo)
            image_label.image = photo  # Keeps reference to the photo

        except FileNotFoundError:
            print(f"File not found: {absolute_path}")

    # Choose a random note and its correct answer
    if selected_clef == "Treble":
        selected_note_img, correct_answer = random.choice(treble_notes_with_answers)
    elif selected_clef == "Bass":
        selected_note_img, correct_answer = random.choice(bass_notes_with_answers)
    elif selected_clef == "Alto":
        selected_note_img, correct_answer = random.choice(alto_notes_with_answers)
    
    # Load image
    try:
        absolute_path = os.path.abspath(selected_note_img)
        print(f"Attempting to open image: {absolute_path}")
        image = Image.open(absolute_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        
        # Display image
        image_label = tk.Label(game_window, image=photo)
        image_label.image = photo  # Keeps reference to the photo
        image_label.pack(pady=20)
        
        # Input entry
        user_input = tk.Entry(game_window, width=5)
        user_input.pack(pady=10)

        # Button to check the answer
        check_answer_button = tk.Button(game_window, text="Check Answer", command=lambda: check_answer(user_input.get(), correct_answer, game_window))
        check_answer_button.pack(pady=10)

        # Button to generate a new note
        new_note_button = tk.Button(game_window, text="Generate New Note", command=generate_new_note)
        new_note_button.pack(pady=10)

        # Button to go back to the main menu
        back_to_menu_button = tk.Button(game_window, text="Back to Main Menu", command=game_window.destroy)
        back_to_menu_button.pack(pady=10)

    except FileNotFoundError:
        print(f"File not found: {absolute_path}")

def check_answer(user_input, correct_answer, game_window):
    global correct_count, incorrect_count  # Use global keyword to access and modify global variables
    
    # Create a label to display the result
    result_label = tk.Label(game_window, text="")
    result_label.pack(pady=10)
    
    # Create a label to display the result
    result_label = tk.Label(game_window, text="")
    result_label.pack(pady=10)

    # Compare user_input with the correct answer
    if user_input.upper() == correct_answer.upper():
        result_label.config(text="Correct choice!", fg="green")
        correct_count += 1  # Increment correct count
    else:
        result_label.config(text=f"Incorrect choice! It was actually {correct_answer}", fg="red")
        incorrect_count += 1  # Increment incorrect count
    
    # Update the count label
    count_label.config(text=f"Correct: {correct_count}, Incorrect: {incorrect_count}") 

# Lists of notes for each clef with their file names and correct answers
treble_notes_with_answers = [
    ("MUSIC-APP.py/MIDDLE-C.png", "C"),
    ("MUSIC-APP.py/TREBLE-HIGH-D.png", "D"),
    ("MUSIC-APP.py/TREBLE-B.jpg", "B"),
    ("MUSIC-APP.py/TREBLE-HIGH-E.jpg", "E"),
    ("MUSIC-APP.py/TREBLE-A.jpg", "A"),
    ("MUSIC-APP.py/TREBLE-E.jpg", "E")
]

bass_notes_with_answers = [
    ("MUSIC-APP.py/BASS-A.jpg", "A"),
    ("MUSIC-APP.py/BASS-B.jpg", "B"),
    ("MUSIC-APP.py/BASS-C.jpg", "C"),
    ("MUSIC-APP.py/BASS-D.jpg", "D"),
    ("MUSIC-APP.py/BASS-E.jpg", "E"),
    ("MUSIC-APP.py/BASS-F.jpg", "F"),
    ("MUSIC-APP.py/BASS-G.jpg", "G")
]

alto_notes_with_answers = [
   ("MUSIC-APP.py/ALTO-A.jpg", "A"),
   ("MUSIC-APP.py/ALTO-B.jpg", "B"),
   ("MUSIC-APP.py/ALTO-C.jpg", "C"),
   ("MUSIC-APP.py/ALTO-D.jpg", "D"),
   ("MUSIC-APP.py/ALTO-E.jpg", "E"),
   ("MUSIC-APP.py/ALTO-F.jpg", "F"),
   ("MUSIC-APP.py/ALTO-G.jpg", "G")
]

# Creates selection menu
mainwindow = tk.Tk()
mainwindow.title("Selection Screen")
mainwindow.geometry("500x500")

label = tk.Label(mainwindow, text="Select a clef:")
label.pack(pady=10)

# Dropdown menu
clefs = ["Treble", "Bass", "Alto"]
clef_var = tk.StringVar()
clef_var.set(clefs[0])

clef_menu = ttk.Combobox(mainwindow, textvariable=clef_var, values=clefs, state="readonly")
clef_menu.pack(pady=10)

# Button that starts the game
start_button = tk.Button(mainwindow, text="Start Game", command=start_game)
start_button.pack(pady=20)

# Label to display count of correct and incorrect answers
count_label = tk.Label(mainwindow, text="Correct: 0, Incorrect: 0")
count_label.pack(pady=10)

mainwindow.mainloop()
