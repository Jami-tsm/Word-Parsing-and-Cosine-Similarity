"""
Name: Jameson Baker
Date: 11.15.23
Description: utility file for all other programs in project
"""


def readWordFile(fileName: str) -> dict:
    """
    Reads file of word data and creates a dictionary of words and dictionary of number data
    :param fileName: str: file name being read
    :return: dictionary of str dictionary key value pairs
    """
    wordData: dict = {}
    minYear = 9999  # CANT EQUAL ZERO
    maxYear = 0
    currentWord = ""
    with open("data/" + fileName) as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 1:
                currentWord = data[0]
                wordData[currentWord] = {}
            else:
                year = int(data[0])
                count = int(data[1])
                if year > maxYear:
                    maxYear = year
                if year < minYear:
                    minYear = year
                wordData[currentWord][year] = count
    for word in wordData:
        for i in range(minYear,maxYear):
            if i not in wordData[word]:
                wordData[word][i] = 0

    return wordData


def totalOccurrences(word, words):
    """
    Counts the amount of times the word occurs in texts
    :param word: The word for which to calculate the count. Not guaranteed to exist in words.
    :param words: A dictionary mapping words to dictionaries with years and counts.
    :return: The total number of times that a word has appeared in print
    """
    result = 0
    if word not in words:
        return 0
    for value in words[word].values():
        result += value

    return result


def main():
    words = readWordFile(input("Enter file name: "))
    print(totalOccurrences(input("Enter word to count: "), words))


if __name__ == "__main__":
    main()
