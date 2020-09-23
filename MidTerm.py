'''
1)  define a function vowelCount that
takes in a string and counts how many
vowels are in the string. The function
should return a dictionary with each
vowel and the count for each vowel.
'''

def vowelCount(string):
    dictionary = {}
    vowels = "aeiou"


    for i in string:
        x = i.lower()
        if x in vowels:
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] += 1



    return dictionary

print(vowelCount("this is one long string"))

'''
2) Define a function wordsWithVowel that
takes in a string and returns a dictionary
where the key is each vowel, and the value
is a list of all words that contain that vowel
'''
def wordsWithVowel(string):
    '''
    d = {"a": [], "e": [], "i": [], "o": [], "u": []}

    words = string.split()
    for word in words:
        for vowel in d:
            if vowel in word:
                d[vowel].append(word)
    return d
    '''
    d = {}
    vowels = "aeiou"
    words = string.split()
    for word in words:
        for vowel in vowels:
            if vowel in word:
                if vowel in d:
                    d[vowel].append(word)
                else:
                    d[vowel] = [word]
    return d


print(wordsWithVowel("this is one long string"))

'''
3) Define a function wordCount that
takes in a file and returns a dictionary
where the key is a word and the value is the
number of occurrences of the word
'''

def wordCount(infile):

    iFile = open(infile, "r")
    d = {}

    content = iFile.read
    lines = content.split("\n")

    for line in iFile:
        print(line, end = "")
        words = line.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1


    
    iFile.close()

    return d

print(wordCount("test.txt"))