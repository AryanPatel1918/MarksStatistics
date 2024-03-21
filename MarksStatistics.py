#Student name: Aryan Patel
#Student number: 501029026z
#Section: 1
#Program description:
# Asks user to enter marks (out of 100) as integers until user enters 'done'. Program uses improved bubble
# sort to sort/order the marks from lowest to highest, calculates the mean(average) and the median of the
# marks entered. Outputs vary on various inputs.

def marksStats(marks):  # takes in a list as a parameter
    swap = True
    j = 0
    sum = 0

    # Sorts marks from lowest to highest
    while swap:  # runs while loop while swap is True
        swap = False
        for i in range(len(marks) - j - 1):
            if marks[i] > marks[i + 1]:  # checks if initial element is larger than the next element
                temp = marks[i]   # stores the initial element in a variable
                marks[i] = marks[i + 1]  # initial element gets value of next element
                marks[i + 1] = temp  # next element gets value of variable
                swap = True    # while loop will run again after at least 1 swap is made
        j += 1    # reduces number of iterations since last element in list is always sorted

    if len(marks) != 0:  # checks if the list is empty or not
        #Calculates mean
        for i in marks:
            sum += i  # adds each element to sum
        mean = round(sum / len(marks))  # calculates average to nearest whole number

        # Calculates median
        if len(marks) % 2 == 0:  # checks if there are an even number of elements in the list
            middle1 = marks[(len(marks) // 2) - 1]  # value of the first element in the middle is stored
            middle2 = marks[len(marks) // 2]  # value of the second element in the middle is stored
            median = (middle1 + middle2) / 2  # averages the first and second middle elements
        else:
            median = marks[len(marks) // 2]  # gets the middle element if number of elements is odd

        # Finds grade such as 'A','B','C', etc.
        if 80 <= mean <= 100:  # checks if the mean is between 80 and 100(inclusive)
            if 90 <= mean <= 100:
                grade = 'A+'
            elif 85 <= mean <= 89:
                grade = 'A'
            else:
                grade = 'A-'
        elif 70 <= mean <= 79:  # checks if the mean is between 70 and 79(inclusive)
            if 77 <= mean <= 79:
                grade = 'B+'
            elif 73 <= mean <= 76:
                grade = 'B'
            else:
                grade = 'B-'
        elif 60 <= mean <= 69:  # checks if the mean is between 60 and 69(inclusive)
            if 67 <= mean <= 69:
                grade = 'C+'
            elif 63 <= mean <= 66:
                grade = 'C'
            else:
                grade = 'C-'
        elif 50 <= mean <= 59:  # checks if the mean is between 50 and 59(inclusive)
            if 57 <= mean <= 59:
                grade = 'D+'
            elif 53 <= mean <= 56:
                grade = 'D'
            else:
                grade = 'D-'
        else:
            grade = 'F'

        print('Sorted marks:', marks)
        print('Mean is', mean)
        print('Median is', median)
        print('Letter Grade:', grade)

    else:
        print('No marks were entered')


print('Welcome to the mark statistics calculator')
n = input("Enter marks out of 100 as integers, enter 'done' to stop taking input: ") # asks user to enter an integer or to stop
marks = []  # list is initially defined as empty

while n != 'done':  # runs while loop until user enters 'done'
    marks.append(n)  # adds the user entered value into the list
    n = input('Enter a mark out of 100 as an integer: ')  # continues to ask user for an integer

marks = list(map(int, marks))  # converts list of strings to list of integers
marksStats(marks)  # calls the function with the list as a parameter
