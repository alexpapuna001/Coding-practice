def gradingStudents(x):
    final_grade=[]
    for i in x:
        if i<38:
            final_grade.append(i)
        else:
            if i % 5 > 2:
                final_grade.append(i + 5- i % 5)
            else:
                final_grade.append(i)
    return final_grade

# my solution to https://www.hackerrank.com/challenges/grading/problem
# difficulty: Easy
