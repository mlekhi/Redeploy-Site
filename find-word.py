#!/usr/bin/env python3

import sys

dictionary_path = "/usr/share/dict/words"

def find_matching_words(word, dictionary_path):
    word = word.lower()
    matching_words = []

    with open(dictionary_path, 'r') as file:
        for line in file:
            line = line.strip().lower()
            if len(line) == 5:
                is_match = True
                for i, char in enumerate(line):
                    if word[i] != '_' and word[i] != char:
                        is_match = False
                        break
                if is_match:
                    matching_words.append(line)

    return matching_words

if len(sys.argv) > 1:
        input_word = sys.argv[1]
if len(sys.argv) > 2:
        dictionary_path = sys.argv[2]

matching_words = find_matching_words(input_word, dictionary_path)

for word in matching_words:
    print(word)
