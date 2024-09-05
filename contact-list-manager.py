from prettytable import PrettyTable

def get_contact_details():
  print("Contact details:")
  name = input("Enter the contact's name: ")

  phone = input("Enter the contact's phone: ")

  email = input("Enter the contact's email: ")

  favoriteBoolean = False

  while True:
    favorite = input("Do you want to favorite the contact? Type 'y' for yes or 'n' for no: ")

    if favorite.lower() == "y":
      favoriteBoolean = True
      break
    elif favorite.lower() == "n":
      break
    
  return {"name": name, "phone": phone, "email": email, "favorite": favoriteBoolean}

def add_contact(contacts, contact):
  contacts.append(contact)
  print(f"Contact {contact['name']} has been added successfully!")
  return

def view_contacts(contacts):
    table = PrettyTable()
    
    table.field_names = ["Index", "Favorite", "Name", "Phone", "Email"]
    
    for index, contact in enumerate(contacts, start=1):
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        favorite = "✓" if contact["favorite"] else " "
        table.add_row([index, favorite, name, phone, email])
    
    print("\nContacts List:")
    print(table)

def update_contact(contacts, index_contact, new_contact):
  index_contact_fixed = int(index_contact) - 1
  if index_contact_fixed >= 0 and index_contact_fixed < len(contacts):
    contacts[index_contact_fixed] = new_contact
    print(f"Contact {index_contact} update for {new_contact['name']}")
  else:
    print("Invalid contact index.")
  return

def favorite_or_unfavorite_contact(contacts, index_contact):
  index_contact_fixed = int(index_contact) - 1
  if contacts[index_contact_fixed]["favorite"]:
    contacts[index_contact_fixed]["favorite"] = False
    print(f"Contact {index_contact} unfavorited")
  else:
    contacts[index_contact_fixed]["favorite"] = True
    print(f"Contact {index_contact} favorited")
  return

def view_favorite_contacts(contacts):
  table = PrettyTable()
  
  table.field_names = ["Index", "Favorite", "Name", "Phone", "Email"]
  
  for index, contact in enumerate(contacts, start=1):
      if contact["favorite"]:
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        favorite = "✓" if contact["favorite"] else " "
        table.add_row([index, favorite, name, phone, email])
  
  print("\nContacts List:")
  print(table)

def delete_contact(contacts, index_contact):
  index_contact_fixed = int(index_contact) - 1
  contact_deleted =  contacts.pop(index_contact_fixed)
  print(f"Contact {contact_deleted['name']} was deleted.")
  return

contacts = []

while True:
  print("\nContact List Manager Menu:")
  print("1. Add contact.")
  print("2. View contacts")
  print("3. Edit contacts")
  print("4. Favorite or unfavorite contacts")
  print("5. View list of favorite contacts")
  print("6. Delete contact")
  print("7. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    new_contact = get_contact_details()
    add_contact(contacts, new_contact)
  elif choice == "2":
    view_contacts(contacts)
  elif choice == "3":
    view_contacts(contacts)
    index_contact = input("Enter the number of the contact you want to update: ")
    new_contact = get_contact_details()
    update_contact(contacts, index_contact, new_contact)
  elif choice =="4":
    view_contacts(contacts)
    index_contact = input("Enter the number of the contact you want to favorite or unfavorite: ")
    favorite_or_unfavorite_contact(contacts, index_contact)
  elif choice == "5":
    view_favorite_contacts(contacts)
  elif choice == "6":
    view_contacts(contacts)
    index_contact = input("Enter the number of the contact you want to delete: ")
    delete_contact(contacts, index_contact)
  elif choice == "7":
    break

print("Application finished")