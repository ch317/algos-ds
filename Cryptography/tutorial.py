import hashlib

#Sha 512
word = "hi just testing"
wordEncoded = word.encode('utf-8')

word512 = hashlib.sha512(wordEncoded)
print(word512.hexdigest())

word = "hi just testing"
wordEncoded = word.encode('utf-8')

word512 = hashlib.sha256(wordEncoded)
print(word512.hexdigest())