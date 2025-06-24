#! /usr/bin/env python3
"""
This script counts how many questions already have an answer.

(c) Toms Grants, MIT License
https://github.com/tgrants/CPKET

Command-line Arguments:
	-h, --help: Displays a list of all commands
	-s, --show-no-answer: Shows questions with no answers
"""

import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter


# Parse and validate arguments
parser = ArgumentParser(
	formatter_class = RawDescriptionHelpFormatter
)
parser.add_argument(
	"file",
	help = "Path to the input file",
)
parser.add_argument(
	'-s', '--show-no-answer',
	action='store_true',
	help = "Show questions with no answers",
)
args = parser.parse_args()


# Count questions with answers
f = open(args.file)
data = json.load(f)

answers = 0
questions = 0

for i in data:
	questions += 1
	if i["correct"] != None:
		answers += 1
	elif args.show_no_answer:
		print("{} {}".format(i["id"], i["question"]))

print("{} / {}".format(answers, questions))

f.close()
