from collections import defaultdict

def winTeamPower(kidsStr, teamPair):
	# Write your code here
	adj_list = defaultdict(set)
	for source, destination in teamPair:
		adj_list[source].add(destination)
		adj_list[destination].add(source)
	visited = {}

	def dfs(kid):
		stack = [kid]
		visited[kid] = -1
		answer = 0

		while len(stack) != 0:
			curr_kid = stack.pop()
			answer += kidsStr[curr_kid - 1]
			neighbours = adj_list[curr_kid]

			for neighbour in neighbours:
				if neighbour in visited:
					continue

				visited[neighbour] = curr_kid
				stack.append(neighbour)

		return answer

	answer = float('-inf')
	for kid in range(len(kidsStr)):
		answer = max(answer, dfs(kid))

	return answer



kids_str = [11, 2, 3, 5]
team_pair = [[3, 2], [1, 2], [2, 3], [3, 1]]
print(winTeamPower(kids_str, team_pair))