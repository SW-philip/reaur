#!/usr/bin/env python3

import requests
import csv
import random
import sys
from datetime import datetime

# Define parameters
criteria = {
    "important": ["network", "boot", "kernel", "wifi", "bluetooth", "login"],
    "once-functional": ["legacy", "abandoned", "beta", "old", "deprecated"],
    "mundane": ["cli", "tool", "simple", "basic", "wrapper", "helper"]
}

quirks = [
    "used in a forgotten distro",
    "builds with bash 2.05 only",
    "requires X11 even if headless",
    "makes systemd cry",
    "depends on a font no one uses",
    "leaves files in /tmp forever",
    "logs everything to stderr... encrypted",
    "was last updated via dial-up",
    "installs but prints ASCII art first",
    "has no uninstall option by design"
]

def classify(description):
    desc_lower = description.lower()
    if any(keyword in desc_lower for keyword in criteria["important"]):
        return "was critical, once"
    elif any(keyword in desc_lower for keyword in criteria["once-functional"]):
        return "ran exactly once, gloriously"
    elif any(keyword in desc_lower for keyword in criteria["mundane"]):
        return "does its job too well to notice"
    else:
        return "mystery utility; origin unknown"

def get_aur_results(term):
    url = f"https://aur.archlinux.org/rpc/?v=5&type=search&arg={term}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch AUR results.")
        sys.exit(1)
    return response.json().get("results", [])

def main():
    if len(sys.argv) < 2:
        print("Usage: generate_museum_catalog.py <search-term>")
        sys.exit(1)

    term = sys.argv[1]
    packages = get_aur_results(term)

    if not packages:
        print("No results found.")
        sys.exit(0)

    with open("museum-catalog.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["package_name", "date_added", "status", "curator_note", "quirk_1", "quirk_2"])

        for pkg in packages[:50]:  # Limit to 50 for sanity
            name = pkg["Name"]
            desc = pkg.get("Description", "No description.")
            tag = classify(desc)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            q1, q2 = random.sample(quirks, 2)

            writer.writerow([name, now, tag, desc, q1, q2])

    print(f"🧾 museum-catalog.csv generated with {min(len(packages), 50)} packages.")

if __name__ == "__main__":
    main()
