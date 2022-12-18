# Counts how many questions already have an answer

import json

f = open("data/progr_tehn_2023_CPKE.json")
data = json.load(f)

answers = 0
questions = 0

for i in data:
	questions += 1
	if i["correct"] != None:
		answers += 1

print("{} / {}".format(answers, questions))

f.close()