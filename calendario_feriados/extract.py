import json

# Read JSON file
with open("holidays.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)

# Extract date and save to txt
with open("dates.txt", "w", encoding="utf8") as txt_file:
    for item in data["items"]:
        txt_file.write(item["start"]["date"] + "\t" + item["summary"] + "\n")
        print(item["start"]["date"] + " " + item["summary"])
