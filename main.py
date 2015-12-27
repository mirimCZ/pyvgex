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


            avg = lineSum / 3
            # fuck it
            if (avg < 10):
                mySum = "0:0" + str(avg)
            else:
                mySum = "0:" + str(avg)

            outputFile.write(mySum + "\n")
            print mySum
    outputFile.close()
