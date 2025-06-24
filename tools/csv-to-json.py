#! /usr/bin/env python3
"""
This script converts test question csv files to json.

(c) Toms Grants, MIT License
https://github.com/tgrants/CPKET

Command-line Arguments:
	-h, --help: Displays a list of all commands
"""

import csv
import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter


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


# Parse and validate arguments
parser = ArgumentParser(
	formatter_class = RawDescriptionHelpFormatter
)
parser.add_argument(
	"files",
	nargs = "+",
	help = "Paths to the input files",
)
args = parser.parse_args()
if len(args.files) != 2:
	parser.error("Exactly two file paths are required.")

# Convert test question csv to json
csv_to_json(args.files[0], args.files[1])
