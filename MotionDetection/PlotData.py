

def plotData(minData=None, maxData=None):
    if minData is None or maxData is None:
        return

    minFile = open("minData.csv", "w")
    maxFile = open("maxData.csv", "w")

    for i in range(0, len(minData)):
        minFile.write(str(i) + ", " + str(minData[i]) + "\n")
    minFile.close()
    
    for i in range(0, len(maxData)):
        maxFile.write(str(i) + ", " + str(maxData[i]) + "\n")
    maxFile.close()

