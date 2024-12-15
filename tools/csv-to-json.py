# This script converts csv files to json

import csv
import json
import sys


def csv_to_json(csvFilePath, jsonFilePath):
	jsonArray = []

	with open(csvFilePath, encoding='utf-8-sig') as csvf:
		csvReader = csv.DictReader(csvf)
		for row in csvReader:
			row = {key: value for key, value in row.items() if key != "" and key != None} # Remove empty keys
			if row["Uzdevuma numurs"] != "" and row["Atbilžu variants"] != "":
				row["id"] = row.pop("Uzdevuma numurs")
				row["question"] = row.pop("Uzdevums")
				row["correct"] = None
				row["answers"] = [row.pop("Atbilžu variants")]
				jsonArray.append(row)
			else:
				if len(jsonArray) == 0: continue
				jsonArray[-1]["answers"].append(row["Atbilžu variants"])

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonString = json.dumps(jsonArray, indent='\t', ensure_ascii=False)
		jsonf.write(jsonString)


if __name__ == '__main__':
	csv_to_json(sys.argv[1], sys.argv[2])
