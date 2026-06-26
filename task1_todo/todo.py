import json
import os

# File jisme tasks save honge
TASKS_FILE = "tasks.json"

# ─────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────

def load_tasks():
    """File se tasks load karo"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Tasks ko file mein save karo"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ─────────────────────────────
# MAIN FEATURES
# ─────────────────────────────

def add_task(tasks):
    task_name = input("\n📝 Task ka naam likho: ").strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print(f"✅ '{task_name}' add ho gaya!")
    else:
        print("⚠️  Kuch toh likho bhai!")

def view_tasks(tasks):
    print("\n📋 Tumhari To-Do List:")
    print("─" * 35)
    if not tasks:
        print("  Koi task nahi hai abhi.")
    else:
        for i, t in enumerate(tasks, 1):
            status = "✅" if t["done"] else "⬜"
            print(f"  {i}. {status} {t['task']}")
    print("─" * 35)

def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nKaunsa task complete hua? (number daalo): "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"🎉 '{tasks[num-1]['task']}' complete mark ho gaya!")
        else:
            print("⚠️  Galat number!")
    except ValueError:
        print("⚠️  Sirf number daalo!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nKaunsa task delete karna hai? (number daalo): "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️  '{removed['task']}' delete ho gaya!")
        else:
            print("⚠️  Galat number!")
    except ValueError:
        print("⚠️  Sirf number daalo!")

# ─────────────────────────────
# MENU
# ─────────────────────────────

def main():
    print("\n🌟 Welcome to To-Do List App!")
    tasks = load_tasks()

    while True:
        print("\n📌 Kya karna chahte ho?")
        print("  1. Task add karo")
        print("  2. Tasks dekho")
        print("  3. Task complete karo")
        print("  4. Task delete karo")
        print("  5. Exit")

        choice = input("\nOption chuno (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Bye! Kaam karte raho!")
            break
        else:
            print("⚠️   1 se 5 ke beech option chuno!")

if __name__ == "__main__":
    main()