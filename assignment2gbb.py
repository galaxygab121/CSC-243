#gabrielle boyer-baker - CSC 243
#assignment 2 - september 22nd 2023

#PROBLEM 1
def printRange():
    # Get input from the user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    # Check if the numbers are the same
    if num1 == num2:
        print("You entered the same number. I cannot print a range.")
    else:
        # Determine the lower and higher numbers
        lower = min(num1, num2)
        higher = max(num1, num2)
        
        # Print the range of numbers separated by tabs
        for i in range(lower, higher + 1):
            print(i, end='\t')
        print()  # Print a newline at the end

# Example use ONLY
#printRange()

#PROBLEM 2
def getLongerStrings(lst, length=5):
    result = []
    for string in lst:
        if len(string) > length:
            result.append(string)
    return result

# Example use ONLY
#lstGreetings = ['hi', 'hello', 'heya', 'how you doing?', 'sup', 'wuzzup']
#longer_strings = getLongerStrings(lstGreetings, 4)
#print(longer_strings)
# Default usage: getLongerStrings(lstGreetings)

#PROBLEM 3
def checkStringsLengths(lst, to_lower=True):
    for string in lst:
        if to_lower:
            string = string.lower()
        else:
            string = string.upper()
        
        length = len(string)
        
        if length >= 10:
            print(f"{string} {length} Long string")
        elif 5 <= length < 10:
            print(f"{string} {length} Medium string")
        else:
            print(f"{string} {length} Short string")

# Example use: ONLY
#lstRandomStrings = ['Electrical', 'For', 'Absolute', 'Album', 'Tin', 'Easy', 'Jeopardizing', 'Agree']
#checkStringsLengths(lstRandomStrings, True)
#Default usage: checkStringsLengths(lstRandomStrings)
# To print in upper case: checkStringsLengths(lstRandomStrings, False)
