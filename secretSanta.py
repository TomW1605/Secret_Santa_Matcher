import random

def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        if x.strip() != "":
            output.append(x.strip().lower())
    return output


names = readFile("names.txt")
unorderedBadMatchesText = readFile("unorderedBadMatches.txt")
orderedBadMatchText = readFile("orderedBadMatches.txt")

givers = names.copy()
receivers = names.copy()

badMatches = []
for badMatch in orderedBadMatchText:
    badMatches.append(badMatch.split("#")[0].strip().split(", ")[0:2])

for badMatch in unorderedBadMatchesText:
    badMatches.append(badMatch.split("#")[0].strip().split(", ")[0:2])
    badMatches.append(badMatch.split("#")[0].strip().split(", ")[0:2][::-1])

#print(badMatches)

pairs = []
for giver in givers:
    receiver = random.choice(receivers)
    while giver == receiver or [giver, receiver] in badMatches or [receiver, giver] in pairs:
        receiver = random.choice(receivers)
    receivers.remove(receiver)
    pairs.append([giver, receiver])

#print(pairs)

with open("matches.txt", 'w') as matchFile:
    matchFile.write("Giver, Receiver\n")
    print("Giver, Receiver")
    for pair in pairs:
        matchFile.write(pair[0].capitalize()+", "+pair[1].capitalize()+"\n")
        print(pair[0].capitalize()+", "+pair[1].capitalize())
