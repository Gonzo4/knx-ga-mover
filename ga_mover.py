import os
import re
from tkinter import filedialog

patt = re.compile(r'.*Address="\d+/\d+/(?P<ug>\d+[=]?\d*)".*')

xml_file = filedialog.askopenfilename()
with open(xml_file, 'r') as f:
    lines = f.readlines()

offset = 0
new_lines = []
for line in lines:
    match = patt.match(line)
    if match:
        parts = match.group("ug").split('=')
        ug = int(parts[0])
        if len(parts) > 1:
            offset = int(parts[1]) - ug
        ug = ug + offset
        new_line = re.sub(r'Address="(\d+)/(\d+)/(\d+[=]?\d*)"', rf'Address="\1/\2/{ug}"', line)
    else:
        new_line = line
    new_lines.append(new_line)


with open(xml_file, 'w') as f:
    f.writelines(new_lines)