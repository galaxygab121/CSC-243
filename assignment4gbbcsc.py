#Gabrielle Boyer-Baker
#CSC 243 - assignment 4 

# PROBLEM 1
def outputStudentInfo(name, age, full_time):
    # Open the file in append mode ('a') if the file already exists, the new data you write to the file will be appended to the end of the file. If the file does not exist, a new file will be created.
    with open('student_info.txt', 'a') as file:
        # Write student information using a format string with a blank line between each student
        file.write(f"Name: {name}\nAge: {age}\nFull Time? {full_time}\n\n")

# TEST ONLY
#outputStudentInfo('Colin Creevey', 14, True)
#outputStudentInfo('Angelina Johnson', 15, True)
#outputStudentInfo('Vincent Crabbe', 13, False)

# PROBLEM 2
def createEmployeeDict():
    employee_dict = {}

    # Open the file in read mode ('r')// you are opening the file for reading, and you cannot write or modify the contents of the file
    with open('employee_list.csv', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Replace newline character with an empty string, then split the line into parts using a comma as a separator
            parts = line.replace('\n', '').split(',')
            
            # Extract employee ID and name
            employee_id, employee_name = parts[0], parts[1]
            
            # Add entry to the dictionary
            employee_dict[employee_id] = employee_name

    return employee_dict

# TEST ONLY
#result = createEmployeeDict()
#print(result)

# PROBLEM 3
import string
import os

def wordListSearch(filename, search_letters):
    # Validate the length of the search_letters
    while len(search_letters) not in (1, 2):
        search_letters = input("Please enter a search string with 1 or 2 characters: ").lower()

    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Remove punctuation and make it case-insensitive
        translator = str.maketrans('', '', string.punctuation)
        content = content.translate(translator).lower()

        # Split the content into words
        words = content.split()

        # Count the occurrences of words starting with the specified letters
        word_counts = {}
        for word in words:
            if word.startswith(search_letters):
                word_counts[word] = word_counts.get(word, 0) + 1

    # Generate the output filename
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    output_filename = f"{search_letters}_in_{base_filename}.txt"
# the file is properly closed after the indented block is executed.  after being opened in write mode 
    with open(output_filename, 'w') as output_file:
        # Write the word counts to the file
        for word, count in word_counts.items():
            output_file.write(f'The word "{word}" appears {count} times.\n')

    print(f"Results written to {output_filename}")

#TEST ONLY
#wordListSearch('shakespeare.txt', 'ro')

