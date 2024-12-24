'''
Make a Contact application in Python that allows users to add, search, and remove contacts from a contact book.


The application should use a dictionary to store the contacts, with keys as contact IDs and values as dictionaries containing contact information such as name, email, phone number, and address.
'''
# Main Code
contacts = {}
while True:
  print('\n Contact Book App')
  print('1. Add Contact')
  print('2. View Contact')
  print('3. Update Contact')
  print('4. Delete Contact')
  print('5. Search Contact')
  
  choice  = input('Enter Your Choice: ')
  if choice == '1':
    name = input('Enter Name: ')
    if name in contacts:
      print('Contact Already Exists')
    else:
      age = input('Enter age: ')
      email = input('Enter email: ')
      mobile = input('Enter mobile_number: ')
      contacts[name] = {'age': int(age), 'email': email, 'mobile': int(mobile)}
      print(f'Contact {name} added Successfully')
  elif choice == '2':
    name = input("Enter Your name: ")
    if name in contacts:
      contact = contacts[name]
      print(f"Name: {name},Age:{age},Mobile:{mobile},Email:{email}")
    else:
      print('Contact Not Found')
  elif choice == '3':
    name = input("Enter name: ")
    if name in contacts:
      age = input("Enter age: ")
      email = input("Enter emial: ")
      mobile = input("Enter mobile: ")
      contacts[name] = {'age': int(age), 'email': email, 'mobile': int(mobile)}
    else:
      print("Contact Not Found!")
  elif choice == '4':
    name = input("Enter name: ")
    if name in contacts:
      del contacts[name]
      print("Contact Deleted Successfully!")
    else:
      print("Contact Not Found!")
  elif choice == '5':
    name = input("Enter name: ")
    if name in contacts:
      print(f"Your Contacts is {name}")
    else:
      print("Contact Not Found!")