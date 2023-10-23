#GABRIELLE BOYER-BAKER -CSC 243 ASSIGNMENT 3

#PROBLEM 1
def searchGrades(grades, low, high):
    """
    Find grades between the specified low and high values.

    Parameters:
    - grades (list): A list of numbers representing exam grades.
    - low (int): The low grade threshold.
    - high (int): The high grade threshold.

    Returns:
    - list: A list of grades between low and high.
    """
    # List comprehension to filter grades between low and high
    filtered_grades = [grade for grade in grades if low < grade < high]
    return filtered_grades

# Example usage:
lstExamGrades = [88, 77, 92, 49, 91, 18, 25, 99, 100, 77, 69, 82, 85, 95, 71, 89, 93]
result = searchGrades(lstExamGrades, 90, 99)
print(result)


# Example usage:
lstExamGrades = [88, 77, 92, 49, 91, 18, 25, 99, 100, 77, 69, 82, 85, 95, 71, 89, 93]
result = searchGrades(lstExamGrades, 90, 99)
print(result)

#PRORBLEM 2
import string

def findLongerWords(filename, length):
    """
    Find and print words from a file with a length greater than or equal to the specified value.

    Parameters:
    - filename (str): The name of the file to open.
    - length (int): The minimum length of words to search for.

    Returns:
    - None
    """
    # Open the file and read its content
    with open(filename, 'r') as file:
        text = file.read().lower()
        # Remove punctuation from the text
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Split the text into words
        words = text.split()
        # List comprehension to filter words based on length
        long_words = [word for word in words if len(word) >= length]
        # Print the result with words separated by tabs
        print('\t'.join(long_words))

# Example usage:
findLongerWords('example.txt', 5)


#PROBLEM 3 PART 1
def countNumberAs(grades, threshold=90):
    """
    Count the number of A grades in a list of grades and print the result.

    Parameters:
    - grades (list): A list of exam grades.
    - threshold (int): The percentage grade constituting an A. Default is 90.

    Returns:
    - None
    """
    # List comprehension to filter A grades based on the threshold
    a_grades = [grade for grade in grades if grade >= threshold]
    # Print the result using a formatted string
    print(f'There are {len(a_grades)} grades greater or equal to {threshold}.')

# Example usage:
countNumberAs(lstExamGrades)
countNumberAs(lstExamGrades, 93)


#PROBELM 3 PART 2
def outputAsToFile(grades, threshold=90):
    """
    Write A grades to a file called a_grades.txt.

    Parameters:
    - grades (list): A list of exam grades.
    - threshold (int): The percentage grade constituting an A. Default is 90.

    Returns:
    - None
    """
    # List comprehension to filter A grades based on the threshold
    a_grades = [str(grade) for grade in grades if grade >= threshold]
    # Write A grades to a file, each grade on a separate line
    with open('a_grades.txt', 'w') as file:
        file.write('\n'.join(a_grades))

# Example usage:
outputAsToFile(lstExamGrades)
outputAsToFile(lstExamGrades, 93)


