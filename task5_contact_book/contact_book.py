import json
import os

CONTACTS_FILE = "contacts.json"

# ─────────────────────────────
# LOAD / SAVE
# ─────────────────────────────

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# ─────────────────────────────
# FEATURES
# ─────────────────────────────

def add_contact(contacts):
    print("\n➕ Naya Contact Add Karo")
    name   = input("  Naam: ").strip()
    if not name:
        print("⚠️  Naam toh daalo!")
        return
    if name in contacts:
        print(f"⚠️  '{name}' pehle se exist karta hai!")
        return

    phone   = input("  Phone number: ").strip()
    email   = input("  Email: ").strip()
    address = input("  Address: ").strip()

    contacts[name] = {
        "phone":   phone,
        "email":   email,
        "address": address
    }
    save_contacts(contacts)
    print(f"✅ '{name}' add ho gaya!")

def view_contacts(contacts):
    print("\n📋 Sare Contacts:")
    print("─" * 40)
    if not contacts:
        print("  Koi contact nahi hai abhi.")
    else:
        for i, (name, info) in enumerate(contacts.items(), 1):
            print(f"  {i}. {name} — 📞 {info['phone']}")
    print("─" * 40)

def search_contact(contacts):
    query = input("\n🔍 Naam ya phone se search karo: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query in info["phone"]:
            print(f"\n👤 Naam:    {name}")
            print(f"   📞 Phone:   {info['phone']}")
            print(f"   📧 Email:   {info['email']}")
            print(f"   🏠 Address: {info['address']}")
            found = True
    if not found:
        print("❌ Koi contact nahi mila!")

def update_contact(contacts):
    view_contacts(contacts)
    name = input("\nKis contact ko update karna hai? (naam likho): ").strip()
    if name not in contacts:
        print("❌ Contact nahi mila!")
        return

    print("(Kuch nahi likhoge toh purani value rahegi)")
    phone   = input(f"  Naya phone [{contacts[name]['phone']}]: ").strip()
    email   = input(f"  Naya email [{contacts[name]['email']}]: ").strip()
    address = input(f"  Naya address [{contacts[name]['address']}]: ").strip()

    if phone:   contacts[name]["phone"]   = phone
    if email:   contacts[name]["email"]   = email
    if address: contacts[name]["address"] = address

    save_contacts(contacts)
    print(f"✅ '{name}' update ho gaya!")

def delete_contact(contacts):
    view_contacts(contacts)
    name = input("\nKis contact ko delete karna hai? (naam likho): ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️  '{name}' delete ho gaya!")
    else:
        print("❌ Contact nahi mila!")

# ─────────────────────────────
# MENU
# ─────────────────────────────

def main():
    print("\n📒 Welcome to Contact Book!")
    contacts = load_contacts()

    while True:
        print("\n📌 Kya karna chahte ho?")
        print("  1. Contact add karo")
        print("  2. Sare contacts dekho")
        print("  3. Contact search karo")
        print("  4. Contact update karo")
        print("  5. Contact delete karo")
        print("  6. Exit")

        choice = input("\nOption chuno (1-6): ").strip()

        if choice == "1":   add_contact(contacts)
        elif choice == "2": view_contacts(contacts)
        elif choice == "3": search_contact(contacts)
        elif choice == "4": update_contact(contacts)
        elif choice == "5": delete_contact(contacts)
        elif choice == "6":
            print("\n👋 Bye! Contacts safe hain!")
            break
        else:
            print("⚠️  1 se 6 ke beech option chuno!")

if __name__ == "__main__":
    main()