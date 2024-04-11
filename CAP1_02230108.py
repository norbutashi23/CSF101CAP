#######################################
# Tashi Norbu
# First Year Electronics and Communication Engineering
# 02230108
#######################################
# Reference 
# W3 School
# https://www.programiz.com/
 
 
#######################################
# Solution
# Solution Score: 49960
#######################################

# Funstion to read game results from a file
def read_input(file_path):
    # Initialize an empty list to store game results
    game_results = []
    # Open the file specified by file_path in read mode
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            shape,outcome = line.strip().split()
            game_results.append((shape, outcome))      # Append the tuple (shape, outcome) to game_result
    return game_results

def calculate_score(game_results):
    """
    Calculates the total score based on round results.
    """
    shape_score = {'A': 1, 'B': 2, 'C': 3}  # Dictionary mapping each shape to  its respective score
    outcome_scores = {'X': 0, 'Y': 3, 'Z': 6} # Dictionary mapping each outcome to its respective score
    
    score = sum(shape_score[shape] + outcome_scores[outcome] for shape, outcome in game_results)   # Calculates the total score by summing up the scores for each round
    return score


file_path = "input_8_cap1.txt"      # Specify the path to the input file
results = read_input(file_path)        # Read the game_results from the file
total_score = calculate_score(results)     # Calculates the total score based on the game_results
print("Total Score:", total_score)


            