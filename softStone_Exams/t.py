
import re
key = r"mat cat hat pat"
p1 = r"[^c|p]at"
pattern1 = re.compile(p1)
print( pattern1.findall(key))