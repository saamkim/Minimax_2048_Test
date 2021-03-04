a = [0, 2, 2, 0]
# right(2020) --> 0004
# right(2204) --> 0044

def right(self):
    w = 0
    k = 0
    for i in range(4):
        if self[i] == 0:
            continue
        if k == 0:
            k = self[i]
        elif k == self[i]:
            self[w] = 2*k
            w += 1
            k = 0
        else:
            self[w] = k
            w += 1
            k = self[i]
    if k != 0:
        self[w] = k
        w += 1
    for i in range(w, 4):
        self[i] = 0