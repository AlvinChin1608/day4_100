# Define the initial map with empty squares
line1 = ["▩", "▩", "▩"]
line2 = ["▩", "▩", "▩"]
line3 = ["▩", "▩", "▩"]
map = [line1, line2, line3]

# Get user input for the position (e.g., B2)
position = input("Enter the position (e.g., B2): ")

# Convert the letter part of the position to lowercase
# to make it uniform
letter = position[0].lower()
abc = ["a", "b", "c"]

# Get the index of the letter in the alphabet list
letter_index = abc.index(letter)

# Get the number part of the position
# Subtract 1 to convert from user input (1 to 3) to list index (0 to 2)
number_index = int(position[1]) - 1

# Change the corresponding square in the map to "X"
map[letter_index][number_index] = "X"

# Print the updated map
for line in map:
    print(" ".join(line))
