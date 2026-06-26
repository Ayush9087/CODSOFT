import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    """
    Password generate karo user ki choice ke hisaab se
    """
    # Character pool banao
    characters = string.ascii_lowercase  # a-z hamesha

    if use_upper:
        characters += string.ascii_uppercase   # A-Z
    if use_digits:
        characters += string.digits            # 0-9
    if use_symbols:
        characters += string.punctuation       # !@#$...

    # Password banao
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    """Password kitna strong hai batao"""
    score = 0
    if len(password) >= 8:   score += 1
    if len(password) >= 12:  score += 1
    if any(c.isupper() for c in password):   score += 1
    if any(c.isdigit() for c in password):   score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2:   return "🔴 Weak"
    elif score <= 4: return "🟡 Medium"
    else:            return "🟢 Strong"

def main():
    print("\n🔐 Password Generator App")
    print("─" * 30)

    # Length input
    while True:
        try:
            length = int(input("\nPassword ki length kitni chahiye? (min 4): "))
            if length >= 4:
                break
            print("⚠️  Kam se kam 4 characters rakhna!")
        except ValueError:
            print("⚠️  Sirf number daalo!")

    # Options
    print("\nKya include karna hai? (y/n)")
    use_upper   = input("  Uppercase letters (A-Z)? ").lower() == 'y'
    use_digits  = input("  Numbers (0-9)? ").lower() == 'y'
    use_symbols = input("  Symbols (!@#$)? ").lower() == 'y'

    # Generate
    password = generate_password(length, use_upper, use_digits, use_symbols)
    strength = check_strength(password)

    print("\n" + "─" * 30)
    print(f"🎉 Tumhara Password: {password}")
    print(f"💪 Strength: {strength}")
    print("─" * 30)

    # Ek aur banana hai?
    again = input("\nEk aur password banana hai? (y/n): ").lower()
    if again == 'y':
        main()
    else:
        print("\n👋 Password save kar lo safely!")

if __name__ == "__main__":
    main()