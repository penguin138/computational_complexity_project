import random
import string
def overlap(str1, str2):
    for i in range(0, len(str1)):
        if str1[i:] == str2[0:(len(str1) - i)]:
            return str1[i:]
    return ""

def merge(str1, str2):
    overLap = overlap(str1, str2)
    return str1+str2[len(overLap):]

def greedy(strings):
    while (len(strings) > 1):
        maxOverlap,maxI,maxJ,currOverlap= 0,0,1,0
        for i in range(0,len(strings)):
            for j in range(0,len(strings)):
                if i != j:
                    currOverlap = len(overlap(strings[i],strings[j]))
                    if currOverlap > maxOverlap:
                        maxI,maxJ,maxOverlap = i,j,currOverlap
        strings[maxI] = merge(strings[maxI],strings[maxJ])
        strings.pop(maxJ)
    return strings[0]
def generate_string(length):
    str=""
    for i in range(0,length):
        str += random.choice(string.ascii_lowercase)
    return str

def break_string(Str,substrFree=True):
    strings,intervals=[],[]
    for i in range(0,2*len(Str)):
        left = random.randint(0,len(Str)-2)
        right = random.randint(left+1,len(Str))
        inInterval = False
        for interval in intervals :
            if interval[0] <= left and interval[1] >= right :
                inInterval = True
            if interval[0] >= left and interval[1] <= right:
                inInterval = True
        if (not substrFree or not inInterval) :
            intervals.append([left,right])
            strings.append(Str[left:right])
    #print(str(intervals))
    return list(set(strings))


def test(numberOfTests, length):
    resultFile = open("results.txt","w")
    maxApproxRatio = 0
    random.seed()
    for i in range(0,numberOfTests):
        testString = generate_string(length)
        substrings = break_string(testString,True)
        resultFile.write(str(i) + ". " + testString + "\n")
        resultFile.write(str(substrings) + "\n")
        greedyString = greedy(substrings)
        approxRatio=float(len(greedyString))/len(testString)
        if maxApproxRatio < approxRatio:
            maxApproxRatio = approxRatio
        resultFile.write("greedy output: " + greedyString + " " + str(approxRatio) + "\n")
    resultFile.write("maxRatio: " + str(maxApproxRatio))
test(1000,100)
