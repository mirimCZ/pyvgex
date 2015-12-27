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

            mySum = lineSum / 3
            outputFile.write(str(mySum) + "\n")
            print mySum
    outputFile.close()
