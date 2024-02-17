#Co-Authors: Devin Fan & Sophia Chen

import random
import sys

if len(sys.argv) != 4:
	print("Usage: python3 56birthday.py <trials> <days> <people>")
	sys.exit(1)

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared_birthday_count = 0

for i in range(trials):
	all_birthdays = []

	for j in range(people):
		day = random.randint(1, days)
		all_birthdays.append(day)

	all_birthdays.sort()

	for k in range(len(all_birthdays) - 1):
		if all_birthdays[k] == all_birthdays[k + 1]:
			shared_birthday_count += 1
			break

probability = shared_birthday_count / trials
print(f"Probability of shared birthday is approx: {probability * 100:.2f}%")
