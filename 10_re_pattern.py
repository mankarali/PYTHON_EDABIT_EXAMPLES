import re
txt = "586Edabit4589can7895be3254324addictive!"
pattern = '[a-zA-Z]\D'
print(" ".join(re.split('\d+', txt)[1:]))