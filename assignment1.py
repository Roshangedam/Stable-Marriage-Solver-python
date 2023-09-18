def read_input(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        men_preferences = []
        women_preferences = []
        
        for _ in range(n):
            preferences = file.readline().strip().split()[1:]
            men_preferences.append(preferences)
        
        for _ in range(n):
            preferences = file.readline().strip().split()[1:]
            women_preferences.append(preferences)
    
    return n, men_preferences, women_preferences

def gale_shapley(n, men_preferences, women_preferences):
    engaged = [-1] * n  # Initialize an array to store the engagements of men (-1 means unengaged)
    women_engaged = [-1] * n  # Initialize an array to store the engagements of women (-1 means unengaged)
    men_rank = [0] * n  # Initialize the rank of each man's current choice

    # Create a dictionary to map woman names to their indices
    woman_indices = {f'WOMAN_{i + 1}': i for i in range(n)}

    while -1 in engaged:
        for man in range(n):
            if engaged[man] == -1:
                woman_name = men_preferences[man][men_rank[man]]
                men_rank[man] += 1
                woman_index = woman_indices[woman_name]  # Convert woman's name to an index

                if women_engaged[woman_index] == -1:
                    engaged[man] = woman_index
                    women_engaged[woman_index] = man
                else:
                    current_husband = women_engaged[woman_index]
                    if women_preferences[woman_index].index(man) < women_preferences[woman_index].index(current_husband):
                        engaged[man] = woman_index
                        women_engaged[woman_index] = man
                        engaged[current_husband] = -1

    return engaged



def write_output(output_file, engagements):
    with open(output_file, 'w') as file:
        for man, woman in enumerate(engagements):
            file.write(f'MAN_{man + 1} WOMAN_{woman + 1}\n')

if __name__ == "__main__":
    input_file = "test/Input.txt"
    output_file = "test/Output.txt"

    n, men_preferences, women_preferences = read_input(input_file)
    engagements = gale_shapley(n, men_preferences, women_preferences)
    write_output(output_file, engagements)
