"""
Name: Jameson Baker
Date: 11/17.23
Description: program which can compute the relative frequency of English
characters occurring in print.
"""
from wordData import *
import matplotlib.pyplot as plt


def letterFreq(words):
    """
    Counts letter frequency
    :param words: A dictionary mapping words to dictionaries with years and counts
    :return: A string containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character.
    """
    letterCount = {}
    letterFreqStr = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    letterList = []
    letterCounts = []
    for word in words:
        for let in word:
            if let not in letterCount:
                letterCount[let] = 0
            letterCount[let] += totalOccurrences(word, words)

    letterFreqList = [(word, freq) for word, freq in letterCount.items()]
    if len(letterFreqList) != 26:
        for letter in alphabet:
            if letter not in [x[0] for x in letterFreqList]:
                letterFreqList.append((letter, 0))
    letterFreqList = sorted(letterFreqList, key=lambda x: x[1], reverse=True)
    for i in range(len(letterFreqList)):
        letterFreqStr += letterFreqList[i][0]
    letterFreqList = sorted(letterFreqList, key=lambda x: x[0])
    for i in range(len(letterFreqList)):
        letterList.append(letterFreqList[i][0])
        letterCounts.append(letterFreqList[i][1])
    plt.bar(letterList, letterCounts, color="skyblue")
    plt.show()

    return letterFreqStr


def main():
    fileName = input("Enter file name: ")
    words = readWordFile(fileName)
    print(letterFreq(words))


if __name__ == "__main__":
    main()
