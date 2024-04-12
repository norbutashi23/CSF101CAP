#######################################
# Tashi Norbu
# First Year Electronics and Communication Engineering
# 02230108
#######################################
# Reference 
# https://www.w3schools.com/
# https://www.programiz.com/
# https://youtube.com/playlist?list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&si=hqH5NEnCcYRi5nYx
# https://youtu.be/GqBoZZ6ZJxk

 
 
#######################################
# Solution Score: 51010
#######################################

# Function to read game outcome from a file
def read_input(file_path):
    # Initialize an empty list to store game outcome
    game_outcomes = []
    # Open the file specified by file_path in read mode
    with open(file_path, 'r') as r:
        # Iterate over each line in the file
        for line in r:
            figure,result = line.strip().split()
            
            # Append the tuple (figure, outcome) to game round
            game_outcomes.append((figure, result))
    return game_outcomes



# Calculate the total score based on the game outcome
def calculate_score(game_outcomes):
    score = 0
    # Loop through each game outcome
    for figure, result in game_outcomes:
        # Assigns scores based on the figure(shape) and the result(outcome)
        if figure == "A":
            if result == "X":
                figure_score = 3 # Score for Figure A with result X
            elif result == "Y":
                figure_score == 4 # Score for figure A with result B
            else:
                figure_score = 8  # Score for figure A with any other result
        elif figure == "B":
            if result == "X":
                figure_score = 1 # Score for Figure B with result X
            elif result == "Y":
                figure_score = 5 # Score for Figure B with result Y
            else:
                figure_score = 9 # Score for figure B with any other result
        else:
            if result == "X":
                figure_score = 2 # Score for any Figure with result X
            elif result == "Y":
                figure_score = 6 # Score for any Figure with result Y
            else:
                figure_score = 7 # Score for any Figure with any other result
        score += figure_score  # Gives total score
    return score

# Specify the file path for the input data
file_path = "input_8_cap1.txt" 

# Read game outcomes from the specified file
game_outcomes = read_input(file_path)
total_score = calculate_score(game_outcomes)
print("Total Score:", total_score)