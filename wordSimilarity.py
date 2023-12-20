"""
Name: Jameson Baker
Date: 11.20.23
Description: Computes the word similarity of words
"""

from wordData import *
from math import *


def topSimilar(words, testWord):
    """
    Computes the similarity of all the words in a dictionary to a word passed in
    :param testWord: a word, for which we are looking for similar words.
    :param words: A dictionary mapping words to dictionaries with years and counts.
    :return: A list of the top five words including the input word in the descending order of
    similarity. If there are less than five words in the file, then return as many words as you
    have. If there is no such a word in the words dictionary, return just one word, itself.
    """
    divisor: float = 0
    normalData = {}
    dotProducts = {}
    similarWords = []

    if testWord not in words:
        return testWord

    for word in words:
        yearCounts = [(year, count) for year, count in words[word].items()]
        yearCounts = sorted(yearCounts, key=lambda x: x[0], reverse=False)
        # print(yearCounts)
        for i in range(len(yearCounts)):
            divisor += yearCounts[i][1]**2
        divisor = sqrt(divisor)
        for i in range(len(yearCounts)):
            if word not in normalData:
                normalData[word] = []
            normalData[word].append(yearCounts[i][1]/divisor)
    # print(normalData)
    for word in normalData:
        for i in range(len(normalData[word])):
            if word not in dotProducts:
                dotProducts[word] = 0
            elif word == testWord:
                dotProducts[word] = 1
            else:
                dotProducts[word] += normalData[word][i] * normalData[testWord][i]

    similarities = [(word, dot) for word, dot in dotProducts.items()]
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    for i in range(len(similarities)):
        similarWords.append(similarities[i][0])
    return similarWords[:5]


def main():
    fileName = input("Enter File name: ")
    words = readWordFile(fileName)
    word = input("Enter word to be used for comparison: ")
    similarities = topSimilar(words, word)
    print(similarities)


if __name__ == "__main__":
    main()



