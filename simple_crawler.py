#### Simple crawler at depth of two links
import dryscrape

session = dryscrape.Session(base_url="http://tomblomfield.com")
print "Starting web crawler bot"

# set up toVisit array and visited dictionary
toVisit = ["/"]
visited = {}

# loop over toVisit at long as it is not empty
while toVisit:

	# get the next url to visit
	currentPage = toVisit.pop(0)
	visited[currentPage] = True

	print ""
	print "Now visiting url: " + currentPage
	print ""

	# sent crawler to new page
	session.visit(currentPage)

	# get all of the links on the page
	all_links = session.css("a")

	# find all urls and add to toVisit array
	for i in range(len(all_links)):
		link = all_links[i].get_attr("href")

		# check if relative and check if not already visited
		if link[0] == "/" and not visited.has_key(link):
			toVisit.append(link)
			print str(i) + ":\t" + all_links[i].get_attr("href")

print "Finished crawling site"