def minRewards(scores):
    # Write your code here.
	reward = [1] * len(scores)
	for index in range(1, len(scores)):
		if scores[index] > scores[index-1]:
			reward[index] = reward[index-1] + 1
	
	for index in range(len(scores)-2, 0, -1):
		if scores[index-1] < scores[index] > scores[index+1]:
			print(index, scores[index], scores[index+1])
			reward[index] = max(reward[index+1], reward[index-1]) + 1
		elif scores[index] > scores[index+1]:
			reward[index] = reward[index+1] + 1
			
			
	
	if len(scores) >=2 and scores[0] > scores[1]:
		reward[0] = reward[1] + 1
	return sum(reward)
