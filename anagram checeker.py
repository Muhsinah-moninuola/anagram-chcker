print('This is an angram checker')
word1 = input('Enter the first word: ')
word2 = input('Enter thesecond word: ')
w1 = word1.lower()
w2 = word2.lower()

def anagram_checker(str1, str2):
    if sorted(str1) == sorted(str2):
        print ('True')
    else:
        print('False')
anagram_checker(w1, w2)