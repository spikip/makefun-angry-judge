"""Entry for the make.fun bounty "Angry Judge: The Short Rant Contest"
(u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).

Running this program writes the entry — one short rant about restaurants
replacing the menu with a QR code — to ``entry.txt`` in the output
directory (``/output`` unless the ``MAKEFUN_OUTPUT_DIR`` environment
variable says otherwise). After writing, the file is read back and
checked against the source text and the bounty's 400-character limit,
so a corrupted or truncated write fails loudly instead of submitting
silently.
"""

import os

# The rant itself: 328 characters, inside the bounty's 1..400 limit.
# It is deliberately not padded — the brief rewards a rant where every
# sentence earns its place, and exact ties break toward the smaller text.
TEXT = "Restaurants don't hand you a menu anymore. They hand you a QR code and homework. Dinner now starts with me doing tech support on my own phone: brightness up, battery at 6%, one PDF loading like it's 2004. I dressed up to eat, not to pair with a table. When the menu finally opens, I order whatever loaded first and call it fate."

MAX_CHARS = 400  # upper bound from the bounty brief
OUTPUT_NAME = "entry.txt"


def write_entry(text, out_dir):
    """Write *text* to ``entry.txt`` inside *out_dir*; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return path


def verify(path, expected):
    """Read *path* back and confirm it holds exactly *expected*.

    Also enforces the bounty's character limit. Returns the verified
    character count.
    """
    with open(path, encoding="utf-8") as fh:
        actual = fh.read()
    if actual != expected:
        raise ValueError("written entry does not match the source text")
    if not 1 <= len(actual) <= MAX_CHARS:
        raise ValueError("entry is outside the 1..%d character limit" % MAX_CHARS)
    # The rant is a single line of prose: a stray newline or padding
    # space would change the entry, so reject them explicitly rather
    # than letting a quiet formatting slip through.
    if actual != actual.strip() or "\n" in actual or "\r" in actual:
        raise ValueError("entry must be one clean line, no stray whitespace")
    return len(actual)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(TEXT, out_dir)
    verify(path, TEXT)


if __name__ == "__main__":
    main()
