#!/usr/bin/env python3

import os
from datetime import datetime
import random
import csv

quirks_list = [
    "writing metadata using 'ed' (just kidding, using nano)",
    "finding README with 'find | xargs cat' instead of grep",
    "storing dates in ISO-8601 because RFC 822 is too modern",
    "simulating tarball extraction by unzipping a .docx",
    "verifying build logs with 'more' because 'less' is too helpful",
    "renaming files with 'mv' in a loop instead of 'rename'",
    "checking errors by reading /var/log/messages in vi",
    "checking for package updates via a fortune cookie parser",
    "fixing permissions with chmod 777 like a menace",
    "cleaning build folders by hitting Ctrl+C until it stops"
]

def reaur_add():
    print("🧬 reaur-add: Begin curation sequence")

    pkg_name = input("Package name (no spaces): ").strip()
    description = input("One-line description: ").strip()
    status = input("Build status summary: ").strip()
    curator_note = input("Curator’s note (your voice): ").strip()

    base_path = f"reaur/PKGBUILDS/{pkg_name}"
    os.makedirs(base_path, exist_ok=True)

    readme = f"""# {pkg_name}

_{description}_

- **Status**: {status}
- **Curator Note**:  
  "{curator_note}"
"""
    with open(f"{base_path}/README.md", "w") as f:
        f.write(readme)

    with open(f"{base_path}/PKGBUILD", "w") as f:
        f.write("# Maintainer: The Archivist\n# This package is not meant to be understood.\n")

    quirks = random.sample(quirks_list, k=2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    build_log = f"""# {pkg_name}
Built on {timestamp}
Dependencies: ancient libraries, a misconfigured udev rule, and faith.
Quirks:
- {quirks[0]}
- {quirks[1]}
"""
    with open(f"{base_path}/verified_builds.log", "w") as f:
        f.write(build_log)

    catalog_path = "reaur/museum-catalog.csv"
    os.makedirs("reaur", exist_ok=True)
    header = ["package_name", "date_added", "status", "curator_note", "quirk_1", "quirk_2"]
    new_entry = [pkg_name, timestamp, status, curator_note, quirks[0], quirks[1]]

    write_header = not os.path.exists(catalog_path)
    with open(catalog_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(header)
        writer.writerow(new_entry)

    print(f"\n✅ Package '{pkg_name}' added to reaur with historical embellishments.\n")

if __name__ == "__main__":
    reaur_add()
