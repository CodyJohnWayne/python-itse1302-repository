def main():
    students = {}
    students = {'Jose': {'ID': 1, 'GPA': 3.25, 'Credits Completed': 95, 'Grades': [100, 90, 80, 70]}, 
    'Malachi':{'ID': 2, 'GPA': 3.25, 'Credits Completed': 97, 'Grades': [90, 100, 70, 100]}}
    print(students)

    print('\nList of All Students:') 
    for student in students:
        print(student)

    print('\nStudent Information:')
    print('Student ID\t\t GPA\t Credits Completed\t     Grades')
    for name, info in students.items():
        print(f'{name}\t{info['ID']}\t\t{info['GPA']}\t\t{info['Credits Completed']}\t\t{info['Grades']}')

    print('\nAccessing Student Info Using the Key in a Loop:')
    for student in students:
        print(f'{student}: {students[student]}')
    
    print()
    print('Jose Has Dropped Out, Removing From Student Info Registry')
    students.pop('Jose')
    print(students)

    print()
    print("Getting Malachi's GPA:")
    mal_gpa = students.get('Malachi', {}).get('GPA')
    print(mal_gpa)

    print()
    print('Clearing the Student Regisrty:')
    students.clear()
    print(students)
    print()
    print('Completed by, Cody Hobbs')

if __name__ == "__main__":
    main()
    