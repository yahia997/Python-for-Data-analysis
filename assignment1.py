# يحيى محمود زكريا عبدالله
# Yahya Mahmoud Zakaria Abdallah

#first method to chiper text 
def transpositionChipher(plainText, key):

  cipherText = ""

  for col in range(key):

    # every iteration increase row by key
    for row in range(col, len(plainText), key):
      cipherText += plainText[row]

  return cipherText


#second method to decipher text
def transpositionDeCipher(cipherText, key):

  result = [" "]*len(cipherText)

  i = 0
  # to get number of columns
  r = float.__ceil__(len(cipherText)/key)

  for row in range(key):

    for col in range(r):

      index = row+(col*key)

      # check if index is in range
      if index < len(result):
        result[index] = cipherText[i]
        i += 1

  return "".join(result)



cipher = transpositionChipher('Common sense is not so common.',8)
deciphered = transpositionDeCipher(cipher,8)
print(cipher)
print(deciphered)