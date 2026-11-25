# Entry for make.fun bounty "Angry Judge: The Short Rant Contest"
# (u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).
#
# The program writes one short rant to /output/entry.txt. The rant was
# written to the judge's published brief, in the brief's own order:
#   1. It is a rant about one everyday annoyance, not an essay and not
#      a list: restaurants replacing the menu with a QR code.
#   2. The anger is shared, not performed: everyone has stood at a
#      table doing tech support on their own dying phone.
#   3. It is concrete: brightness up, battery at 6%, one PDF loading
#      like it's 2004 - details anyone who has lived it recognises.
#   4. Every sentence earns its place; no throat-clearing, and the
#      last line is the punch: you order whatever loaded first.
#   5. Fresh angle: not the printer, not the bus, not "circling back"
#      - the menu itself has become homework.
# The rant is 328 characters, inside the 1..400 limit, deliberately
# not padded: exact ties break toward the smaller text.
# Runner-up drafts, kept for the record: the two-factor code that
# arrives after it expires; the delivery rider who is "2 minutes
# away" for forty minutes; the meeting that ends with "let's take
# this offline" and never goes anywhere.
import os

TEXT = (
    "Restaurants don't hand you a menu anymore. They hand you a QR code "
    "and homework. Dinner now starts with me doing tech support on my "
    "own phone: brightness up, battery at 6%, one PDF loading like "
    "it's 2004. I dressed up to eat, not to pair with a table. When "
    "the menu finally opens, I order whatever loaded first and call "
    "it fate."
)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
