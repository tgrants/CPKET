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

# Load all files
questions = []
for filepath in args.files:
	with open(filepath, "r") as json_file:
		questions.extend(x for x in json.load(json_file) if x not in questions)
print(questions)
