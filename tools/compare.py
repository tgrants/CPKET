#! /usr/bin/env python3
"""
This script compares answers to the same questions across multiple tests.
It is useful for finding and eliminating inconsistencies.

(c) Toms Grants, MIT License
https://github.com/tgrants/CET

Command-line Arguments:
	-h, --help: Displays a list of all commands
"""

import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter


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
if len(args.files) < 2:
	parser.error("At least two file paths are required.")

# Load all files, find differences
questions = {} # Dict, questions are grouped by their text
q_diff_ids = [] # Questions with different IDs
q_diff_text = [] # Questions with different text
q_diff_cansw = [] # Questions with different correct answer
for filepath in args.files:
	with open(filepath, "r") as json_file:
		for x in json.load(json_file):
			key = x["question"]
			if key in questions:
				if questions[key] != [x]:
					questions[key].append(x)
					if (questions[key][0]["id"] != x["id"]):
						q_diff_ids.append(f"{questions[key][0]["id"]} {x["id"]}")
					if (questions[key][0]["correct"] != x["correct"]):
						q_diff_cansw.append(f"{questions[key][0]["id"]} {questions[key][0]["correct"]} | {x["id"]} {x["correct"]}")
			else:
				questions[key] = [x]

# Print results
# for q in q_diff_ids:
#	print(q)
for q in q_diff_cansw:
	print(q)
