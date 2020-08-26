  """
RegEx VII-A: Negative Lookbehind
Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx negative lookbehind.

Example
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "yourregularexpressionhere"

len(re.findall(pattern, ", ".join(lst))) ➞ 2
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
Find more info on RegEx and negative lookbehind in Resources.
You can find all the challenges of this series in my Basic RegEx collection.
"""

import re

pattern = '(?<!good )cookie'

lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']

print(len(re.findall(pattern, ', '.join(lst))))
