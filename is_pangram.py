import string

def is_pangram(phrase, alphabet=string.ascii_lowercase):
    test = set()
    phrase = phrase.lower()
    for char in phrase:
        if char in alphabet:
            test.add(char)
    return set(alphabet) <= test

print(is_pangram('the quick brown fox jumps over the lazy dog'))
print(is_pangram('Sphinx of Black Quartz, Hear my vow.'))
print(is_pangram('Sphinx of Black Quartz, Judge my vow.'))        
print(is_pangram('The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men'))