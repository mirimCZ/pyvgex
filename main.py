import sys

if __name__ == "__main__":
    outputFile = open('output.txt','w')
    with open("input.txt", "r") as ins:
        for line in ins:
            times = line.replace("\n", "").split("\t")
            lineSum = 0

            for time in times:
                clean = float(time.replace("0:", ""))
                lineSum = lineSum + clean

            avg = "0:" + str("%.2f" % (lineSum / 3)).zfill(5)

            outputFile.write(avg + "\n")
            print avg
    outputFile.close()
