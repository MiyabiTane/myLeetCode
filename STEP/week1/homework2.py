from collections import Counter
import numpy as np

def get_dictionary():
    new_dictionary = []
    dict_file = open(
        "/Users/tanemoto/Desktop/myLeetCode_/STEP/class1/dictionary.txt", "r", encoding="utf_8")
    while True:
        word = dict_file.readline()
        if word:
            #全て小文字に
            word = word[:-1].lower()
            word_dict = Counter(word)
            if 'q' in word_dict:
                word_dict['u'] -= 1
                if word_dict['u'] == 0:
                    del word_dict['u']
            new_dictionary.append((word_dict, word))
        else:
            break
    return new_dictionary


def get_candidate(target_word, dictionary):  
    candidates = []
    for word in dictionary:
        flag = 0
        #まず使われている単語を見る
        if word[0].keys() <= target_word.keys():
            #次に各文字の文字数に注目する
            for key in word[0].keys():
                if target_word.get(key) < word[0].get(key):
                    flag = 1
                    break
            if flag == 0:
                candidates.append(word[1])
    return candidates


def calculate_and_decide(candidates, input_words):
    point_dict = {"u": 0, "c": 2, "f": 2, "h": 2, "l": 2, "m": 2, "p": 2,
                  "v": 2, "w": 2, "y": 2, "j": 3, "k": 3, "q": 3, "x": 3, "z": 3}
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates
    max_point = 0
    for candidate in candidates:
        score = 0
        for s in candidate:
            if s in point_dict:
                score += point_dict[s]
            else:
                score += 1
        if (score+1)**2 > max_point:
            max_point = (score+1)**2
            ans = candidate
    print(max_point)
    return ans


def make_str_for_game(input_words, dictionary):
    target_words = Counter(input_words)
    candidates = get_candidate(target_words, dictionary)
    ans = calculate_and_decide(candidates, input_words)
    return ans


dictionary = get_dictionary()

#Qu -> q
input_words = "nunkdbgvskpuqarz"
#example pf testcase
#"wdosnbvbxaescinn"
#"rozhkdibvuwtcwqm"
#"uepaeihfooeyyugl"

ans = make_str_for_game(input_words, dictionary)
if ans:
    #output the answer as upper case letters
    print(ans.upper())
