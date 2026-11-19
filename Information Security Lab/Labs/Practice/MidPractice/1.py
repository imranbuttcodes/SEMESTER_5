# # def ceasercipher(plain_text, key):
    
# #     cipher_text = ""
    
# #     for p in plain_text:
# #         cipher_text += chr(((ord(p) - ord('A')) + key) % 26  + ord('A'))
    
# #     return cipher_text

# # def ceasercipher_d(cipher_text, key):
    
# #     plain_text = ""
    
# #     for p in cipher_text:
# #         plain_text += chr(((ord(p) - ord('A')) - key) % 26  + ord('A'))
    
# #     return plain_text

# # print(ceasercipher("HELLO", 3))
# # print(ceasercipher_d("KHOOR", 3))


# def vigenere_cipher(plain_text, key):

#     new_key = key

#     for i in range(len(plain_text) - len(key)):
#         new_key += key[i % len(key)]
    
#     # print("new_key", new_key)

#     # print()

#     cipher_text = ""

#     for p, k in zip(plain_text, new_key):
#         p_ = ord(p) - ord('A')
#         k_ = ord(k) - ord('A')

#         cipher_text += chr((p_ + k_ ) % 26 + ord('A'))
        

    
#     return cipher_text

# print(vigenere_cipher("HELLO", "KEY"))



# def vigenere_cipher_d(cipher, key):

#     new_key = key

#     for i in range(len(cipher) - len(key)):
#         new_key += key[i % len(key)]
    

#     plain_text = ""

#     for p, k in zip(cipher, new_key):
#         p_ = ord(p) - ord('A')
#         k_ = ord(k) - ord('A')

#         plain_text += chr((p_ - k_ ) % 26 + ord('A'))
        

    
#     return plain_text

# print(vigenere_cipher_d("RIJVS", "KEY"))






# def autokey_cipher(plain_text, key):

#     new_key = key + plain_text[:len(plain_text) - len(key)]
    

#     cipher_text = ""

#     for p, k in zip(plain_text, new_key):
#         p_ = ord(p) - ord('A')
#         k_ = ord(k) - ord('A')

#         cipher_text += chr((p_ + k_ ) % 26 + ord('A'))
        

    
#     return cipher_text



def count_freq(plan_text):
    alpha_dict = dict()
    for ch in plan_text:
        if ch.isalpha():
            ch = ch.upper()
            if ch in alpha_dict:
                alpha_dict[ch] +=1
            else:
                alpha_dict[ch] = 1
    
    from functools import reduce
    freqs = list(alpha_dict.values())
    total = reduce(lambda x, y: x + y, freqs)
    percentage = list(map(lambda x: round(((x/total) * 100), 2), freqs))
    new_alpha_dict = dict()
    t_len = len(percentage)
    i = 0
    for key, value in alpha_dict.items():
        new_alpha_dict[key] = {
            "freq": value,
            "percentage": percentage[i] 
        }
        i += 1
    return new_alpha_dict
alpha_dict = count_freq("IMRANIMRANBUTT")

print("Frequency Table:\n")
for key, value in alpha_dict.items():
    print(f"Letter: {key} | freq: {value['freq']} | percentage: {value['percentage']} %")


def decrypt(cipher):
    decrypted_text = ""
    freqs = count_freq(cipher)
    print(freqs)
    most_frequent = max(freqs, key= lambda letter: freqs[letter]['freq'])
    print(most_frequent)
    est_key = (ord(most_frequent) - ord('E')) % 26
    print(est_key)
    for ch in cipher:
        decrypted_text += chr((((ord(ch) - ord('A')) - est_key) % 26) + ord('A'))
        #decrypted_text += (ch - 'E') % 26

    return decrypted_text

print(decrypt("SOJZKXS KDGS OY ZUU KGYE"))