from contact import Contact
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