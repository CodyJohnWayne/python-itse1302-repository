
def find_substring(main_string, substring):
    index = main_string.find(substring)
    if index !=-1:
        print(f"'{substring}' was found in the main string at index {index}.")
    else:
        print(f"'{substring}' was not found!")
    return index

def main():
    print('Welcome to the String Replacement Program!')
    print ('-'*44)
    main_string = input('Enter the string to search through: ')
    substring = input('Enter ther string to search for: ')
    print()
    print('Searching for substring within the main string content, please wait!')
    print('-'*70)
    index = find_substring(main_string, substring)
    if index != -1:
        print()
        print('Initiating the string replacement process!')
        print('-'*44)
        replace_choice = input(f"Do you want to replace '{substring}' with something else? (y/n):").strip().lower()
        if replace_choice == 'y':
            new_substring = input('Enter the replacement string: ')
            main_string = main_string[:index] + new_substring + main_string [index + len(substring):]
            print('New String: ', main_string)
            print()
        else:
            print('No changes were made to the string.')
    print('Thank you for using our program!')
    print()
    print('Competed by, Cody Hobbs')                                    

if __name__ == '__main__':  
    main()