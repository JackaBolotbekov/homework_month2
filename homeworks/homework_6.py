class Contact:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number: str):
        return phone_number.isdigit() and len(phone_number) == 10

    def __str__(self):
        return f"{self.name} — {self.phone_number}"


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name: str, phone_number: str):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр.")
        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)


ContactList.add_contact("Alice", "1234567890")
ContactList.add_contact("Bob", "3546789098")

for c in ContactList.all_contacts:
    print(c)
