import json
class Contact:
    contact_list = []
    def create_new(self,name,phone):
        self.new_contact = {}
        self.new_contact[name] = phone
        self.contact_list.append(self.new_contact)
    def show_list(self):
        for contact in self.contact_list:
            for name ,phone in contact.items():
                print(name.upper(), phone)
    def __repr__(self) -> str:
        return f"{self.contact_list}"


make_contact = Contact()

try:
    file = open('contacts.json')
    make_contact.contact_list = json.load(file)
    file.close()
    print("Successfully Loaded contacts from database..")
except:
    print("No contacts data found in database")

while True:
    print("1. Create a new contact.\n2. Show contact list.\n3. Exit.")
    option = input("Enter your Choice : ")
    if option == '1':
        name = input("Enter name : ")
        phone = input("Enter phone number : ")
        make_contact.create_new(name, phone)
        print("Contact created successfully.")

        with open("contacts.json", "w") as file:
            json.dump(make_contact.contact_list, file)

    elif option == '2':
        make_contact.show_list()
    else:
        break

