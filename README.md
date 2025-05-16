# reaur

> A user-hostile archive of user-hostile packages.

reaur is a static museum of cursed, abandoned, or unnecessary AUR packages, preserved entirely for cultural and archaeological reasons.

Packages added to reaur are not required to build. Or run. Or make sense. Their inclusion is based on a combination of historical significance, operational obscurity, and vibes.

This repository is managed manually by one curator, and contains the following components:

* `museum-catalog.csv` — the canonical list of archived packages, including notes and quirks
* `scripts/` — utilities for adding, searching, and processing exhibits
* `PKGBUILDS/` — folders of collected package fragments (README, PKGBUILD, logs)
* `web/` — HTML output for GitHub Pages or local viewing

---

## Usage

* Run `scripts/reaur-add.py` to add a new cursed package
* Run `./build-museum.sh` to regenerate the static HTML index and placards
* Run `scripts/reaur-search.py` to browse the archive via terminal

All scripts are self-contained. If anything breaks, you're expected to fix it the way the original author would've: reluctantly, and with increasingly baroque solutions.

---

## Philosophy

reaur is not a tool. It’s a warning. And a dare.

Software should not disappear just because it's inconvenient. This repo does not exist to revive broken packages—it exists to remember them. Like taxidermy, but with `PKGBUILD`s.

---

## License

Creative Commons [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Use it. Fork it. Cite it in your research paper about digital ruins. Just don’t try to monetize it.

---

## Contributing

You can't. Not yet. This is a solo archive. You may email cursed packages to the curator, who will ignore most and reluctantly add a few.

---

## See Also

* [aur.archlinux.org](https://aur.archlinux.org) — The original and still-mostly-functional archive
* [archive.org](https://archive.org) — The spiritual parent of this effort
* Any GitHub repo with less than 3 stars and more than 5 years since last commit
