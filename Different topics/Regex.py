"""
Regex
Commonly used to search for and match specific patterns of text.
IMPORTANT!
In regex, the characters below NEED to be escaped:
. ^ $ * + ? { } [ ] \ | ( )
e.g. r"google\.com"
. - any character, except NL
\d - Digit
\D - NOT a digit
\w - word character (a-z, A-Z, 0-9, _)
\W - NOT a word character
\s - whitespace
\S - NOT a whitespace

"""
import re
from pathlib import Path
text = Path('Regex_text').read_text()

# It's important to know the difference between raw string and a normal string e.g.

t1 = r"\tMy name is Kuba"
t2 = "\tMy name is Kuba"
print(t1, " =/= ",  t2)
print(t1 == t2)

# Pattern - we will search for this chain in our text
pattern = re.compile(r"Kuba")

# Matches - our storage for the matches of pattern in our text
matches = re.finditer(pattern, text)

for match in matches:
    print(match)
