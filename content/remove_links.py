import re
from pathlib import Path

# [[group-1#group-2|group-3]]
link_pattern = r"\[\[([^\]\|#]*)(#[^\|\]]*)?(\|[^\]]*)?\]\]"

def remove_link(match):
    if match.group(3) is not None:
        return match.group(3)[1:]
    elif match.group(2) is not None:
        return match.group(2)[1:]
    else:
        return match.group(1).replace(".", " ")

for f in Path(".").rglob("*.md"):
    with open(str(f), "r+") as fl:
        new = re.sub(link_pattern, remove_link, fl.read())
        fl.seek(0)
        fl.write(new)
