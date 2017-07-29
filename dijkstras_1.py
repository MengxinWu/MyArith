import pdb


graph = {}

graph['score'] = {}
graph['score']['film'] = 5
graph['score']['poster'] = 0

graph['film'] = {}
graph['film']['guitar'] = 15
graph['film']['drum'] = 20


graph['poster'] = {}
graph['poster']['guitar'] = 30
graph['poster']['drum'] = 35


graph['guitar'] = {}
graph['guitar']['piano'] = 20

graph['drum'] = {}
graph['drum']['piano'] = 10


graph['piano'] = {}

infinity = float('inf')
costs = {}
costs['film'] = 5
costs['poster'] = 0
costs['guitar'] = infinity
costs['drum'] = infinity
costs['piano'] = infinity

parents = {}
parents['film'] = 'score'
parents['poster'] = 'score'
parents['guitar'] = None
parents['drum'] = None
parents['piano'] = None


processed = []



def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

print('The origin data is:')
print(costs, parents)

node = find_lowest_cost_node(costs)

while node is not None:

	print('The now lowest cost node is: %s' %(node))

	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	print(costs, parents)

	node = find_lowest_cost_node(costs)
print('The result is:')
print(costs, parents)