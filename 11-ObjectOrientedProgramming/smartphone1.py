class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"Name : {self.name}, Email : {self.email}, Telephone : {self.telephone}"
    
class ContactList:
    def __init__(self):
        contact_list = []
         
    def add_contact(self, name, email, telephone):
        if not name or not email or not telephone:
            print('Not enough data')
            return
        new_contact = Contact(name, email, telephone)
        self.contact_list.append(new_contact)

        return f'Contact {name} added '
    
    def display_contacts(self):
        if not self.contacts:
            return "No contacts"
        return "\n".join(str(contact) for contact in self.contacts)
    
def main():
    contact_list = ContactList()

    contact_list.add_contact("John Brown", "brown@onet.pl", "555234000")

    print('Contact List:')
    print(contact_list.display_contacts())

if __name__ =="__main__":
    main()