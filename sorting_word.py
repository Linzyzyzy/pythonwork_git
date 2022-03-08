while 1 == 1:
	w = input()
	x = 0
	nw = ""
	while x <= len(w) - 1:
		if w[x] == "/":
			w = w[x + 1:len(w) + 1]
			x = 0
			nw = nw + "/"
		if x == 0:
			nw = nw + w[x]
		else:
			q = 0
			while q <= x - 1:
				if w[x] >= nw[x - 1 - q]:
					nw = nw[0:x - q] + w[x] + nw[x - q:x]
					break
				else:
					q = q + 1
			if q > x - 1:
				nw = w[x] + nw
		x = x + 1
	print(nw)
