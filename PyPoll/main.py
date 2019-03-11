import csv
import os

polling_csv = os.path.join("..", "Resources", "election_data.csv")

election_output = os.path.join(".", "election_output.txt")



def isNewCandidate(candidates, candidateName):
    for candidate in candidates:
        if candidateName == candidate["name"]:
            return False

    return True

def findCandidateIndex(candidates, candidateName):
    for candidate in candidates:
        if candidateName == candidate["name"]:
            return candidates.index(candidate)

def printResults(orderedCandidates):
	print("Election Results \n------------------")
	print(f"Total Votes:\t{totalVotes} \n------------------")
	for candidate in orderedCandidates:
		candidatePct = round(candidate['votes'] / totalVotes * 100,3)
		print(f"{candidate['name']}: \t{candidatePct}% ({candidate['votes']}) ")
	print("------------------")
	print(f"WINNER: {orderedCandidates[0]['name']}")
	print("------------------")

def printResultsToFile(orderedCandidates, election_output):
	with open(election_output, 'w', newline='') as txtfile:
		print("Election Results \n------------------", file=txtfile)
		print(f"Total Votes:\t{totalVotes} \n------------------", file=txtfile)
		for candidate in orderedCandidates:
			candidatePct = round(candidate['votes'] / totalVotes * 100,3)
			print(f"{candidate['name']}: \t{candidatePct}% ({candidate['votes']}) ", file=txtfile)
		print("------------------", file=txtfile)
		print(f"WINNER: {orderedCandidates[0]['name']}", file=txtfile)
		print("------------------", file=txtfile)
	
with open(polling_csv,newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_headers = next(csvreader)

    totalVotes = 0
    candidates = []
    for row in csvreader:
        totalVotes += 1

        if isNewCandidate(candidates,row[2]):
            candidates.append({
                "name": row[2],
                "votes": 0
            })
        
        idx = findCandidateIndex(candidates,row[2])
        candidates[idx]["votes"] += 1



orderedCandidates = sorted(candidates, key=lambda k: k['votes'], reverse=True)
printResults(orderedCandidates)
printResultsToFile(orderedCandidates, election_output)
