import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

print("Contact Book")

name = input("Enter contact name: ")
number = input("Enter contact number: ")

contacts[name] = number
save_contacts(contacts)

loaded = load_contacts()

print("\nContact saved successfully!")
print(f"You now have {len(loaded)} contact(s):")
for name, number in loaded.items():
    print(f"{name} : {number}")