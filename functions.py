
students = [{'name': 'Andrea', 'scores': [90, 73, 43, 100]},
            {'name': 'Astrid', 'scores': [76, 44, 66, 73]},
            {'name': 'Ben', 'scores': [64, 74, 91, 78]},
            {'name': 'Diana', 'scores': [96, 82, 76, 100]}]
# Q: add an average score and passed (True/False) to each dictionary if the average > 70
def get_average(scores_list):
    _avg = sum(scores_list)/len(scores_list)
    return _avg

def did_pass(score_avg):
    return True if score_avg > 70 else False

for student in students:
    score_avg = get_average(student.get('scores'))
    student['average'] = score_avg
    student['passed'] = did_pass(score_avg)

# Positional vs Keyword
# Q: define a function that formats a name from 'Mary Anderson' to 'Anderson, Mary'
def reverse_name(first, last):
    return '{}, {}'.format(last, first)
# print(reverse_name('Mary','Anderson')) # positional
# # Anderson, Mary 
# print(reverse_name(first='Mary',last='Anderson')) # keyword

# Lambdas
numbers = [10, 2, 4, 12, 13, 1, 712, 23, 2, 192]
# it's anonymous function
#lambda x: x ** 3
# great for doing one thing in one place
print(list(map(lambda x: x ** 3, numbers)))