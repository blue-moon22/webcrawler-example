#### Complex crawler at depth of 3 links
import dryscrape

start_page = "https://en.wikipedia.org/"
sess = dryscrape.Session(base_url=start_page)
print "Starting"

visited = {}
levels = ["/wiki/Earth"]
names = []

cNames = 0

cDepth = 0
maxDepth = 2

while levels and cDepth < maxDepth:
	print ""
	# print "Current Depth:\t" + cDepth
	print ""
	
	nextLevel = []
	while levels:

		if cNames % 100 == 0:
			print "Done 100"

		current_url = levels.pop(0)
		sess.visit(current_url)

		print "Visiting:\t", current_url

		all_links = [node.get_attr("href") for node in sess.css("a[href^='/wiki/']")]

		for link in all_links:
			if visited.has_key(link):
				continue
			else:
				visited[current_url] = cNames
				names.append(link)
				cNames += 1
				nextLevel.append(link)

	levels = nextLevel
	cDepth += 1

adjacencyMatrix = [[0 for i in range(cNames)] for j in range(cNames)]

cCurrent = 0

while cCurrent <= cNames:
	sess.visit(names[cCurrent])
	all_links = [node.get_attr("href") for node in sess.css("a[href*='/wiki/']")]
	for link in all_links:
		if visited.has_key(link):
			adjacencyMatrix[cCurrent][visited[cCurrent]] = 1

print adjacencyMatrix
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(adjacencyMatrix)

