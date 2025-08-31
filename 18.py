# code 18
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count
