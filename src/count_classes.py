import re

with open("../data/cl-full.json") as f:
    text = f.read()

classes = re.findall("CL_[0-9][0-9][0-9][0-9][0-9][0-9][0-9]", text)

print(len(set(classes)))
