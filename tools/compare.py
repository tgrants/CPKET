#! /usr/bin/env python3
"""
This script compares answers to the same questions across multiple tests.
It is useful for finding and eliminating inconsistencies.

(c) Toms Grants, MIT License
https://github.com/tgrants/CPKET

Command-line Arguments:
	-h, --help: Displays a list of all commands
	-c, --compare-correct: Compares correct answers for questions with the same text
	-i, --compare-ids: Compares IDs for questions with the same text
"""

import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from enum import Enum
from pathlib import Path


class DiffType(Enum):
	ID = "id"
	CORRECT = "correct"


def hyperlink(label: str, path: str, line: int = None) -> str:
	if line:
		url = f"file://{path}:{line}"
	else:
		url = f"file://{path}"
	return f"\033]8;;{url}\a{label}\033]8;;\a"


# Parse and validate arguments
parser = ArgumentParser(
	formatter_class = RawDescriptionHelpFormatter
)
parser.add_argument(
	"files",
	nargs = "+",
	help = "Paths to the input files",
)
me_group = parser.add_mutually_exclusive_group(required = False)
me_group.add_argument(
	'-c', '--compare-correct',
	action='store_true',
	help = "Compare correct answers for questions with the same text",
)
me_group.add_argument(
	'-i', '--compare-ids',
	action='store_true',
	help = "Compare IDs for questions with the same text",
)
args = parser.parse_args()
if len(args.files) < 2:
	parser.error("At least two file paths are required.")
# If no comparison flags are passed, choose a default
if not any([
	args.compare_correct,
	args.compare_ids,
]):
	print("No comparison flags specified. Defaulting to correct answer comparison.")
	args.compare_correct = True

# Load all files, find differences
questions = {} # Dict, questions are grouped by their text
for filepath in args.files:
	with open(filepath, "r") as json_file:
		for x in json.load(json_file):
			key = x["question"]
			if key in questions:
				existing_question = questions[key][0][1]
				if existing_question != x:
					diff = None # Difference type for alt question
					if (args.compare_ids and existing_question["id"] != x["id"]):
						diff = DiffType.ID
					elif (args.compare_correct and existing_question["correct"] != x["correct"]):
						diff = DiffType.CORRECT
					questions[key].append((filepath, x, diff))
			else:
				questions[key] = [(filepath, x, None)]

# Print results
for key, value in questions.items():
	if len(value) <= 1: continue # Skip questions without differences
	print(f"Q '{str(key).replace("\n", " ")}'")
	match value:
		case DiffType.ID:
			pass
		case DiffType.CORRECT:
			pass
	print()
