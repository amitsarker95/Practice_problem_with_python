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

    def isExist(self,nameX,phoneX):
        isFound = False
        for contact in make_contact.contact_list:
            for name, phone in contact.items():
                if name.upper() == nameX.upper() or phone == phoneX:
                    isFound = True
        return isFound

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
        get_res = make_contact.isExist(name,phone)
        if get_res == True:
            print("This name or phone is already exist..\nEnter (Y) for add anyway..")
            option = input("Enter choice : ").upper()
            if option == 'Y':
                make_contact.create_new(name, phone)
                print("Contact created successfully.")
                with open("contacts.json", "w") as file:
                    json.dump(make_contact.contact_list, file)
            else:
                pass
        else :
            make_contact.create_new(name, phone)
            print("Contact created successfully.")

            with open("contacts.json", "w") as file:
                json.dump(make_contact.contact_list, file)
    elif option == '2':
        make_contact.show_list()
    else:
        break

