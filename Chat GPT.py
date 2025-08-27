import random

wvFam = ["pappy", "ninny"]
ohFam = ["mark", "becky", "matt", "alex"]
paFam = ["chris", "tawnya", "eric"]
allFam = wvFam + ohFam + paFam
lastYear = [['pappy', 'eric'], ['ninny', 'becky'], ['mark', 'pappy'], ['becky', 'ninny'],
            ['matt', 'tawnya'], ['alex', 'chris'], ['chris', 'mark'], ['tawnya', 'matt'], ['eric', 'alex']]

# Build last year recipient mapping
lastYearDict = {giver: receiver for giver, receiver in lastYear}

# Build same household lookup
households = [wvFam, ohFam, paFam]
householdMap = {}
for group in households:
    for person in group:
        householdMap[person] = set(group) - {person}  # everyone else in same household

# Try to generate a valid derangement
def generate_secret_santa(allFam, lastYearDict, householdMap, max_attempts=10000):
    for attempt in range(max_attempts):
        recipients = allFam[:]
        random.shuffle(recipients)
        santaDict = dict(zip(allFam, recipients))

        valid = True
        for giver, receiver in santaDict.items():
            if receiver == giver:
                valid = False  # no self-gifting
                break
            if receiver in householdMap.get(giver, set()):
                valid = False  # no same-household
                break
            if lastYearDict.get(giver) == receiver:
                valid = False  # not last year's recipient
                break

        if valid:
            return santaDict, attempt

    return None  # failed to find valid assignment

santaDict, num = generate_secret_santa(allFam, lastYearDict, householdMap)

# Output results
if santaDict:
    print("🎅 Secret Santa Assignments 🎁")
    for giver, receiver in santaDict.items():
        print(f"{giver} → {receiver}")
else:
    print("Could not find a valid Secret Santa assignment. Try relaxing constraints or increasing attempts.")