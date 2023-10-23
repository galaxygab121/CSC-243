#gabrielle boyer-baker
#csc 243 assignment 5

#problem 1
def makeCitiesDict(file_path='continent_cities.csv'):
    cities_dict = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into continent and cities
                data = line.strip().split(',')
                
                # The first item is the continent
                continent = data[0]

                # The rest of the items are cities
                cities = data[1:]

                # Update the dictionary
                cities_dict[continent] = cities

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.csv.rtf")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cities_dict

# Example usage:
cities_dict = makeCitiesDict()
print(cities_dict)

#problem 2
def findStates(file_path='transactions.csv'):
    unique_states_set = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into fields
                fields = line.strip().split(',')

                # Extract the state field (assuming 2-letter state acronyms)
                state = fields[5]

                # Check if the state is 2 characters in length
                if len(state) == 2:
                    unique_states_set.add(state)

    except FileNotFoundError:
        print("Unable to open the file.")
        return []

    # Convert the set to a sorted list
    unique_states_list = sorted(list(unique_states_set))

    return unique_states_list

# Example usage:
print(findStates())

