def calculatenewgrade(grade):
    if grade < 38:
        return grade
    remain = grade % 5
    if 5 - remain < 3:
        return grade + (5 - remain)
    else:
        return grade


numberOfGrades = int(input())
for i in range(numberOfGrades):
    print(calculatenewgrade(int(input())))
