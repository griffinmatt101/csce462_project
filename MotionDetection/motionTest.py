from DetectMotion import DetectMotion

dm = DetectMotion()

print "Running"

for i in range(1, 101):
    g = dm.detectMotion()
    if g is not None:
        print(g)
