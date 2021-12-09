import re
import os
import json

class_count = {}
for i in range(1, 89):
    print(i)
    url = f"https://data.bioontology.org/ontologies/CL/submissions/{i}/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb"

    print(url)
    os.system(f"wget {url} --output-document=../data/current_cl_file.txt")

    with open("../data/current_cl_file.txt", encoding="ISO-8859-1") as f:
        text = f.read()

    classes = re.findall("CL[_:][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", text)

    classes = [entry.replace(":", "_") for entry in classes]

    class_count[i] = len(set(classes))
    print(len(set(classes)))

with open("../results/result.json", "w") as fp:
    json.dump(class_count, fp)
