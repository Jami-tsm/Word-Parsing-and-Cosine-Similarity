"""
Name: Jameson Baker
Date: 11.17.23
Description: Program which can computes the top and bottom trending words between a given starting and ending year
"""

from wordData import *
from printedWords import *
from dataclasses import dataclass


def trending(words, startYear, endYear):
    """
    Calculates the top and bottom 10 trending words between given years
    :param words: A dictionary mapping words to dictionaries with years and counts
    :param startYear: An integer, the starting year for the computation of the trending words.
    :param endYear: An integer, the ending year for the computation of the trending words
    :return: A list containing a tuple (word, trend) entry for each word for which qualifying data
    exists. The list is sorted in decreasing trend value.
    """
    trendList = []
    for word in words:
        if words[word][startYear] >= 1000 and words[word][endYear] >= 1000:
            # AUDI TOLD ME NOT TO MAKE OBJECT WordTrend
            trend = words[word][endYear]/words[word][startYear]
            a = (word, trend)
            trendList.append(a)
    trendList = sorted(trendList, key=lambda x: x[1], reverse=True)
    return trendList


def main():
    fileName = input("Enter text file name: ")
    words = readWordFile(fileName)
    startingYear = int(input("Enter starting year: "))
    endingYear = int(input("Enter ending year: "))
    trendingList = trending(words, startingYear, endingYear)
    topTrend = trendingList[:10]
    bottomTrend = trendingList[len(trendingList)-10:]
    bottomTrend = sorted(bottomTrend, key=lambda x: x[1], reverse=False)
    print("The top trending words from " + str(startingYear) + " to " + str(endingYear) + ":")
    for i in topTrend:
        print(i[0])
    print("The bottom trending words from " + str(startingYear) + " to " + str(endingYear) + ":")
    for i in bottomTrend:
        print(i[0])


if __name__ == "__main__":
    main()
