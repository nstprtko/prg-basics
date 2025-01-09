# smartphone.py

class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Telephone: {self.telephone}"


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, telephone):
        # Basic validation
        if not name or not email or not telephone:
            print("All fields are required to add a contact.")
            return
        new_contact = Contact(name, email, telephone)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            return "No contacts available."
        return "\n".join(str(contact) for contact in self.contacts)


def main():
    # Create a contact list
    contact_list = ContactList()

    # Add contacts
    contact_list.add_contact("John Brown", "brown@onet.pl", "555234000")
    contact_list.add_contact("Anna May", "am@o2.pl", "232000199")
    contact_list.add_contact("George Small", "smallg@google.pl", "222999100")
    contact_list.add_contact("Paola Big", "bigpaola@poczta.pl", "100200300")

    # Display the contact list
    print("Contact List:")
    print(contact_list.display_contacts())


if __name__ == "__main__":
    main()