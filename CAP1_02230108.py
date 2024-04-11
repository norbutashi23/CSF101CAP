#######################################
# Tashi Norbu
# First Year Electronics and Communication Engineering
# 02230108
#######################################
# Reference 
 
 
#######################################
# Solution
# Your Solution Score:
# Put your number here
#######################################

def read_input_file(file_path):
    """
    Reads the input file, the function coverts its content into a list of pairs. Two pieces of information are contained in each pair:
    the player's chosen shape and the round's outcome. The information from ever game round is contained in this pairwise collection.
    """
    game_results = []
    with open(file_path, 'r') as file:
        for line in file:
            shape,outcome = line.strip().split()
            game_results.append((shape, outcome))
    return game_results

def calculate_score(game_results):
    """
    Calculates the total score based on round results.
    """
    shape_score = {'A': 1, 'B': 2, 'C': 3}  # Mapping of shape to score
    outcome_scores = {'X': 0, 'Y': 3, 'Z': 6} # Mapping of outcome to score
    
    score = sum(shape_score[shape] + outcome_scores[outcome] for shape, outcome in game_results)
    return score

# Example usage:
file_path = "input_8_cap1.txt" 
results = read_input_file(file_path)
total_score = calculate_score(results)
print("Total Score:", total_score)


            