#Gabrielle Boyer-Baker Assignment 1
'''Friday September 15 2023
   CSC 243 professor Joseph Mendelsohn
'''

# Function to perform math operations
def doMath(num1, num2, num3):
    # Calculate the result by adding num1 and num2, then dividing by num3
    result = (num1 + num2) / num3
    return result

# Function to create initials from first and last names
def makeInitials(first_name, last_name):
    # Combine the first character of first_name and last_name to create initials
    initials = first_name[0] + last_name[0]
    return initials

# Function to extract a substring from a string
def stringPractice(input_string):
    # Use slicing to extract the substring from the 2nd to the 5th character
    substring = input_string[1:5]
    return substring

# Function to create a list from three strings
def makeList(str1, str2, str3):
    # Create a list containing the three input strings
    my_list = [str1, str2, str3]
    return my_list

# Function to get the sum of the first and last elements of a list
def getFirstLast(num_list):
    # Calculate the sum of the first (index 0) and last (index -1) elements in the list
    total = num_list[0] + num_list[-1]
    return total

# Example usage of the functions
result1 = doMath(1, 5, 5)
print(result1)  # Output: 1.2

result2 = makeInitials('Gabrielle', 'Xavier')
print(result2)  # Output: 'GX'

result3 = stringPractice('I LOVE DEPAUL')
print(result3)  # Output: 'LOV'

result4 = makeList('LOVE', 'LIVE', 'LAUGH')
print(result4)  # Output: ['LOVE', 'LIVE', 'LAUGH']

result5 = getFirstLast([3, 2, 5, 6])
print(result5)  # Output: 9

 
