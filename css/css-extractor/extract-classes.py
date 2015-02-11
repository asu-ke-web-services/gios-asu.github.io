# Download the Bootstrap CSS before running this
# https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.css

import re

with open('../bootstrap.css', 'r',encoding="utf8") as f:
	cssBootstrap = f.read()
with open('../bootstrap-asu.css', 'r', encoding="utf8") as f:
	cssASU = f.read()

# Matches a class name or comma-separated list of class names
# matches = re.findall("(?:(\.[a-zA-Z0-9\-]+)\s*,?\s*)+\{",css)
matchesBootstrap = re.findall("(?:(\.[a-zA-Z0-9\-]+)[\s,]*)+\{",cssBootstrap)
matchesASU = re.findall("(?:(\.[a-zA-Z0-9\-]+)[\s,]*)+\{",cssASU)
uniques = set(matchesBootstrap + matchesASU)

with open('bootstrap-full-class-list.txt', 'w+') as f:
	for m in sorted(uniques):
		f.write("%s\n" % m)
