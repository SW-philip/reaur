#!/usr/bin/env python3
print('reaur-add.py active')
#!/usr/bin/env python3

import csv
import sys
import random

catalog = "museum-catalog.csv"

def load_catalog():
    try:
        with open(catalog, newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print("❌ museum-catalog.csv not found. Are you inside the reaur root?")
        sys.exit(1)

def print_entry(entry, label="🎲 Random Exhibit"):
    print(f"\n{label}:\n")
    print(f"📦 {entry['package_name']}")
    print(f"🕒  {entry['date_added']}")
    print(f"⚙️  {entry['status']}")
    print(f"🧠 {entry['curator_note']}")
    print(f"🧙 {entry['quirk_1']}")
    print(f"🧙 {entry['quirk_2']}")
    print(f"🔗 web/packages/{entry['package_name']}.html\n")

def main():
    entries = load_catalog()
    if len(sys.argv) < 2:
        entry = random.choice(entries)
        print_entry(entry)
    else:
        term = sys.argv[1].lower()
        matches = [e for e in entries if any(term in str(v).lower() for v in e.values())]
        if not matches:
            print("🔍 No match found. Here's something else instead:")
            print_entry(random.choice(entries))
        else:
            for m in matches:
                print_entry(m, label="🔎 Match")

if __name__ == "__main__":
    main()
