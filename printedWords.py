"""
Name: Jameson Baker
Date: 11.17.23
Description: Programs which can compute the total number of printed words for each year
"""

import matplotlib.pyplot as plt
from wordData import *


def printedWords(words):
    """
    Computes the total number of printed for each year
    :param words:  A dictionary mapping words to dictionaries with years and counts.
    :return: A list containing tuples (year, count total words) for each year for which data
    exists. The list must be sorted in ascending order of year.
    """
    yearlyTotals: dict = {}
    for word in words:
        for year in words[word]:
            if year not in yearlyTotals:
                yearlyTotals[year] = 0
            yearlyTotals[year] += words[word][year]
    yearlyTotalsList = [(y, c) for y, c in yearlyTotals.items()]
    yearlyTotalsList = sorted(yearlyTotalsList, key=lambda x: x[0], reverse=False)
    return yearlyTotalsList


def wordsForYear(year, yearList):
    """
    Returns the total number of words for a specified year
    :param year: an integer representing the year being queried.
    :param yearList:  A list of tuples (year, count total words), as defined in the previous
    function. The list must be sorted in ascending order of year.
    :return: An integer count representing the total number of printed words for that year.
    If there is no entry in yearList for the requested year, the function returns 0.
    """
    if year not in [x[0] for x in yearList]:
        return 0
    else:
        for pair in yearList:
            if year == pair[0]:
                return pair[1]


def main():
    words = readWordFile(input("Enter file name: "))
    year = int(input("Enter Year: "))
    yearList = printedWords(words)
    listOfCounts = [x[1] for x in yearList]
    listOfYears = [x[0] for x in yearList]
    totalWords = wordsForYear(year, yearList)
    print("Total printed words in", year, ":", totalWords)
    plt.plot(listOfYears, listOfCounts)
    plt.show()


if __name__ == "__main__":
    main()
