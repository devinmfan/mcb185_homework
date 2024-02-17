import random
import sys

if len(sys.argv) != 4:
    print("Usage: python3 57birthday.py <trials> <days> <people>")
    sys.exit(1)

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared_birthday_count = 0

for i in range(trials):
    unique_birthdays = []
    for j in range(people):
        birthday = random.randint(1, days)
        if birthday in unique_birthdays:
            shared_birthday_count += 1
            break
        unique_birthdays.append(birthday)

probability = shared_birthday_count / trials
print(f"Probability of shared birthdays with {people} people in {trials} trials is approx: {probability * 100:.2f}%")
