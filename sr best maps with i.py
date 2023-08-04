import tkinter as tk
from itertools import combinations
import random

def generate_word_combinations(words):
    return list(combinations(words, 2))

def on_button_click():
    selected_favorites = [pair_var.get() for pair_var in pair_vars if pair_var.get() != ""]
    print("Selected Favorites:", selected_favorites)

# List of words
word_list = ["Reflection", "Magma Cavern", "Cavern of Darkness", "Legacy", "Skyscrapers", "Acid Realm", "Snowy Slopes", "Heights", "Dunes", "Frozen", "Tropical Dash", "Laser Tag", "Crystal Mine", "Canyon", "Grassy Mountain", "Tropical Islands", "Dragons Lair", "Island Route", "Mystic Alps", "River of Ice", "The Orion Disaster", "Swamp", "Pastel Valley", "Enchanted Forest", "Ancient Tomb", "Floatroads", "Fuyu Village", "Candyland", "Ravine", "Northern Cliffs", "Honeycomb Run", "Heist", "Mystical Gorge", "Twilight Lagoon", "Autumn Woodlands", "Western Bluffs", "Winter Cove", "The Emerald Isle", "Melodical Fantasy", "Taiga", "Jurassic Coast", "Clockwork Colloseum", "Night Terrors", "Frosted Fortress", "Disaster Valley", "The Realm Between", "Cosmic Cliffside", "Shipwrecked"]

# Generate all possible combinations of two-word pairs
all_combinations = generate_word_combinations(word_list)

# Randomly select 50 pairs
selected_combinations = random.sample(all_combinations, 50)

# Create a Tkinter window
root = tk.Tk()
root.title("Select Favorite Words from Pairs")

# Create variable to store selected favorites
pair_vars = []

# Create radio buttons for each word pair
for pair in selected_combinations:
    pair_text = f"{pair[0]} or {pair[1]}"
    pair_var = tk.StringVar(value="")
    pair_label = tk.Label(root, text=pair_text)
    pair_label.pack(anchor='w')
    pair_radio1 = tk.Radiobutton(root, text=pair[0], variable=pair_var, value=pair[0])
    pair_radio1.pack(anchor='w')
    pair_radio2 = tk.Radiobutton(root, text=pair[1], variable=pair_var, value=pair[1])
    pair_radio2.pack(anchor='w')
    pair_vars.append(pair_var)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_button_click)
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
