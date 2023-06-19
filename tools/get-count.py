# Counts how many questions already have an answer
# Option -s shows questions with no answers

import json
import sys


def get_count(show_no_answer):
	f = open("data/progr_tehn_2023_CPKE.json")
	data = json.load(f)

	answers = 0
	questions = 0

	for i in data:
		questions += 1
		if i["correct"] != None:
			answers += 1
		elif show_no_answer:
			print("{} {}".format(i["id"], i["question"]))

	print("{} / {}".format(answers, questions))

	f.close()

if __name__ == '__main__':
	get_count('-s' in sys.argv)