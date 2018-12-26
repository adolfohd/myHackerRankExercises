import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    newGrades = []
    for grade in grades:
        if (grade>=38):
            modulo = grade % 5
            if modulo >= 3:
                grade += ( 5 - modulo)
        newGrades.append(grade)
    return(newGrades)

print(gradingStudents([45,33,89,76,12,51]))