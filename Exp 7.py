from collections import Counter

ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83*
*(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

frequency = Counter(ciphertext)

print("Character Frequency:")
for char, count in frequency.most_common():
    print(repr(char), ":", count)

key = {
    '‡': 'e',
    '8': 't',
    '4': 'h'
}

plaintext = ""

for char in ciphertext:
    if char in key:
        plaintext += key[char]
    else:
        plaintext += char

print("\nDecrypted Message:")
print(plaintext)
