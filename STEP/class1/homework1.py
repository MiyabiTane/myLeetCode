import numpy as np
def get_dictionary():
    new_dictionary = []
    dict_file = open(
        "/Users/tanemoto/Desktop/myLeetCode_/STEP/class1/dictionary.txt", "r", encoding="utf_8")
    while True:
        word = dict_file.readline()
        if word:
            new_dictionary.append((sorted(word[:-1]), word[:-1]))
        else:
            break
    new_dictionary = sorted(new_dictionary)
    #print(new_dictionary[:5])
    return new_dictionary

def BinarySearch(target_word, dictionary):
    left = 0; right = len(dictionary) - 1
    while left <= right:
        mid = (left+right) // 2
        if dictionary[mid][0] == target_word:
            return dictionary[mid][1]
        elif target_word < dictionary[mid][0]:
            right = mid - 1
        else:
            left = mid + 1
    print("cannnot make anagram")
    return False

def find_anagram(random_word, dictionary):
    dict_copy = np.array(dictionary)
    #anagramとして自分自身が返ってこないように
    if random_word in dict_copy[:,1]:
        rem_index = np.where(dict_copy[:,1]==random_word)[0][0]
        dictionary.pop(rem_index)
    anagram = BinarySearch(sorted(random_word), dictionary)
    if anagram:
        return anagram

dictionary = get_dictionary()  
ans = find_anagram("eat", dictionary)
ans2 = find_anagram("peach", dictionary)
print(ans)
print(ans2)

