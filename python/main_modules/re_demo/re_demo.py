import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
alexmarkin.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then bring it to an end"

# pattern = re.compile(r"alexmarkin\.com")
# pattern = re.compile(r"\BHa")
# pattern = re.compile(r"^Start.*end$")
pattern = re.compile(r"^start.*end$", re.IGNORECASE)

# inside character sets . and * don't need to be escaped
# pattern = re.compile(r"\d{3}[-*.]\d{3}[-\*\.]\d{4}")
# pattern = re.compile(r"[89]00[-*.]\d{3}[-\*\.]\d{4}")

# pattern = re.compile(r"[^a-zA-Z]")
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)

# matches = pattern.finditer(sentence)

# match string from the beginning
# matches = pattern.match(sentence)


for match in matches:
    print(match)

# with open("data.txt", "r") as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)
