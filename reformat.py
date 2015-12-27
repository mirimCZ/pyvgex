import sys

if __name__ == "__main__":
    outputFile = open('output.txt','w')
    with open("input.txt", "r") as ins:
        for line in ins:
            times = "0:" + line.replace('.', ',')
            outputFile.write(times)
            print times
    outputFile.close()
