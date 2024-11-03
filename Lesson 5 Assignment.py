import random


def main():
    grades_list = []

    while True:
        grade = int(input('Enter Your Grades then Enter -1 to Stop: '))
        if grade == -1:
            break
        else:
            grades_list.append(grade)
    print('Grades:', grades_list)

    print('-----Removing the Lowest Grade-----')

    lowest_grade = min(grades_list) 
    index_lowest = grades_list.index(lowest_grade)
    grades_list.pop(index_lowest)
    print(grades_list)

    print('------Removing a Random Grade-----')

    random_grade = random.choice(grades_list)
    grades_list.remove(random_grade)
    print(grades_list)

    print('-----Edit a Grade-----')

    for i, grade in enumerate(grades_list, start=1):
        print(f'{i}.{grade}')
    edit_grade = int(input('Which Grade Do You Want To Edit: '))
    if edit_grade < 0 or edit_grade > i:
        print('Please Enter a Valid Grade!')
    edit_grade = int(input(f'Which Grade Do You Want To Edit? Enter Number Between 1 and {len(grades_list)}: '))
    
    print('-----Sorting and Reversing the List-----')
    grades_list.sort()
    grades_list.reverse()
    print(grades_list)

    print('-----Getting Grade Total and Average-----')

    total = sum(grades_list)
    average = total/len(grades_list)
    print(f'Total: {total}')
    print(f'Average: {average}')

if __name__ == '__main__':
    main()

print()
print('Completed by, Cody Hobbs')






