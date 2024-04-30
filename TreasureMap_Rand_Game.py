import random

line1 = ["▩", "▩", "▩"]
line2 = ["▩", "▩", "▩"]
line3 = ["▩", "▩", "▩"]

map = [line1, line2, line3]

# Randomly select a row and column index for the 'X'
treasure_row = random.randint(0, 2)
treasure_col = random.randint(0, 2)

# Mark the position with 'X' in the map
map[treasure_row][treasure_col] = 'X'

# Print the map with 'X'
for line in map:
    print(" ".join(line))

# Get user input for position
position = input("Enter your guess (e.g., B2): ")

# Convert the position to row and column indices
row = int(position[1]) - 1
col = ord(position[0].upper()) - ord('A')

# Check if the user's guess matches the 'X' position
if row == treasure_row and col == treasure_col:
    print("Congratulations! You found the treasure!")
else:
    print("Oops! Try again next time.")

