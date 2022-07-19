f = open("README.md", "r")
w = open("README.md.good", "w")
i = 1
for x in f:
	w.write(str(i) + ". " + x)
	i = i + 1
