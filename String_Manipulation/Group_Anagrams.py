from typing import DefaultDict


strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = DefaultDict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)

print(anagrams.values())