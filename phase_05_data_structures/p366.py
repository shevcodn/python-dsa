from collections import Counter

def can_construct(ransom_note, magazine):
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True
    
print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))