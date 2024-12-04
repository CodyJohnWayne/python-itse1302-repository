import csv

def main():
    print('Welcome to the Contact Manager App')
    print('------------------------------------')
    print('Choose the Following Option to Perform the Correspinding Action:')
    while True:

        print('1 - Create a new contact CSV file\n2 - Add New Contact\n3 - View All Contacts\n4 - Modify an Existing Contact\n5 - Save and Exit')
        print()
        choice = int(input('Enter Your Selection: '))
        print()
        if choice == 1:
            create_csv()
        elif choice == 2:
            add_contact()
        elif choice == 3:
            view_contact()
        elif choice == 4:
            modify_contact()
        elif choice == 5:
            print('Exiting the Program')
            print('----------------------')
            print('Completed by, Cody Hobbs')
            break
        else:
            print()
            print('----------------------------------')
            print('Invalid Option, Try Again')
            print('-----------------------------------')
            print()
            

def create_csv():
    with open('contacts.csv', 'w') as file:
        file.write('Name:, Phone:, Email:')
    print('Contact File Created Successfully!')
    print('----------------------------------')

def add_contact():
    name = input('Enter Contact Name: ')
    phone = input('Enter Contact Phone Number: ')
    email = input('Enter Contact Email Address: ')
    with open('contacts.csv', 'a') as file:
        file.write(f'\n{name}, {phone}, {email}')
    print()
    print('Contact Added Successfully')
    print('----------------------------------')

#I tried a new method to learn this weeks assignment, I didn't read the chapter, instead I used external sources to learn it. I'm not sure if I need to explain .strip() but incase I do. 
#When reading lines from a file, each line ends with a new line character, so the .strip() makes the spacing look better when the view_contacts() function is executed. 

def view_contact():
    print()
    print('Contact Information:')
    print('----------------------------------')
    with open('contacts.csv', 'r') as file:
        contacts = file.readlines()
        if contacts:
            for contact in contacts:
                print(contact.strip().replace(',', '\t'))
            print()
  
        
            




def modify_contact():
    view_contact()
    contact_name = input('Enter the name of the contact you want to modify: ')
    print()
    contacts_list = []
    with open('contacts.csv', 'r') as file:
        # contacts_list = file.readlines()
        reader = csv.reader(file)
        header = next(reader)
        contacts_list.append(header)
        for row in reader:
            contacts_list.append(row)
    for i, row in enumerate(contacts_list):
        if row[0].lower() == contact_name.lower():
               
            print(f'Current details: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}')
            print()
            new_phone = input('Enter the new phone number or leave blank to keep the same: ')
            new_email = input('Enter the new email address or leave blank to keep the same: ')
                
            if new_phone:row[1] = new_phone
            if new_email:row[2] = new_email
            break
    else:
        print('Contact Not Found!')
        contact_name = input('Enter the name of the contact you want to modify: ')
        print() 
        new_phone = input('Enter the new phone number or leave blank to keep the same: ')
        new_email = input('Enter the new email address or leave blank to keep the same: ')
                
        if new_phone:row[1] = new_phone
        if new_email:row[2] = new_email
   
    
        
        
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts_list)
        print()
        print('Contact Updated Successfully!')




if __name__ == "__main__":
    main()