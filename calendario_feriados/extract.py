import json
import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
HOLIDAYS_JSON = CURR_DIR + "holidays.json"
DATES_FILE = CURR_DIR + "dates.txt"

# Read JSON file
with open(HOLIDAYS_JSON, "r", encoding="utf8") as json_file:
    data = json.load(json_file)

# Extract date and save to txt
with open(DATES_FILE, "w", encoding="utf8") as txt_file:
    for item in data["items"]:
        txt_file.write(item["start"]["date"] + "\t" + item["summary"] + "\n")
        print(item["start"]["date"] + " " + item["summary"])
