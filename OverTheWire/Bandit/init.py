#!/usr/bin/env python3
# Bandit Solutions template initializer.

import re
import sys
import requests
from bs4 import BeautifulSoup


def write_level(f, level):
    ssh_id = 0 if (level == 0) else (level-1)
    url = f"https://overthewire.org/wargames/bandit/bandit{level}.html"
    f.write(f"## [Bandit{level}]({url})\n")

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find("h2", {"id": "level-goal"})
    if content:
        f.write("**Level Goal**<br/>\n")
    else:
        f.write("\n")
        content = soup.find("div", {"id": "title"})
    content = content.find_next("p").get_text()
    content = re.sub("email.*protected", f"bandit{ssh_id}-git@localhost", content)
    f.write(f"``\n{content}\n``\n")
    f.write("\n")
    f.write("**Solution**\n")
    f.write("```bash\n")
    f.write(f"$ ssh bandit{ssh_id}@bandit.labs.overthewire.org -p 2220\n")
    f.write(" "*54 + f"# bandit{level}'s password.\n")
    f.write("```\n<br />\n\n\n")
    print(f"[*] Level {level} written.")


def write_template(fname, title, levels):
    """ Write Bandit Solutions template at given filename. """
    with open("TEMPLATE.MD", "w") as f:
        print(f"[*] Writing Solution Template @ File {fname}.")
        f.write(f"{title}\n\n")
        for i in range(levels):
            try:
                write_level(f, i)
            except Exception as e:
                print(f"[!] {e}")
                continue
        print("[*] Done.")


if __name__ == "__main__":
    TITLE         = "# OverTheWire - Bandit - Solutions"
    BANDIT_LEVELS = 35
    filename      = "TEMPLATE.MD"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    try:
        write_template(filename, TITLE, BANDIT_LEVELS)
    except Exception as e:
        print(f"[!] {e}")

            