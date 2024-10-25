###
# Calculates the final grade for a test based
# on the number of points obtained

test_result = int(input('enter your points'))
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >=14 :
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    elif points < 10 :
        grade = 'Fail'
    return grade


final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')