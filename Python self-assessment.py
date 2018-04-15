# 1) We want a function that takes a list of numbers and returns that list where 10 was added to each number.
# Organize the following code into function:
list_num = [1, 2, 3]
list_add_10 = []
for num in list_num:
    list_add_10.append(num + 10)
print(list_add_10)
# Function format of the code above:
list_num = [1, 2, 3]
def add_10(list_num):
    list_add_10 = []
    for num in list_num:
        list_add_10.append(num + 10)
    return(list_add_10)
print(add_10(list_num))


# 2) We want a function that takes in a list of strings and returns the list with length of words.
# Organize the following code into function:
list_words = ['great', 'job', 'so', 'far']
list_length_words = []
for word in list_words:
    list_length_words.append(len(word))
print(list_length_words)
# Function format of the code above:
list_words = ['great', 'job', 'so', 'far']
def length_word(list_words):
    list_length_words = []
    for word in list_words:
        list_length_words.append(len(word))
    return(list_length_words)
print(length_word(list_words))


# Challenge 1
# Write a function that looks at the number of times given letters appear in a document. The output should be in a dictionary.
letters_to_count = 'It is a sunny day'
def letter_counter(letters_to_count):
    count = {}
    for character in letters_to_count.lower():
        count.setdefault(character, 0)
        count[character] += 1
    return(count)
print(letter_counter(letters_to_count))


# Challenge 2
# Write a function that removes first occurence of a given item from a list. Do not use the methods .pop() or .remove().
# If the item is not present in the list, output should be "The item is not in the list."

# Method 1
x = [1,3,7,8,0]
def remove_item(list_item, item_to_remove):
        while item_to_remove in list_item:
            list_item.remove(item_to_remove)
print(remove_item(x, 7))
print(x)
# Method 2
x = [1,3,7,8,0]
def remove_item(list_item, item_to_remove):
    return[item for item in list_item if item != item_to_remove]
remove_item(x, 7)


# Challenge 3
# The simple substitution cipher basically consists of substituting every plaintext character for a different ciphertext character.

# Method 1: Encryption or Decryption separately (key can be changed)
'''
encyption only
'''
plaintext = input('Enger message: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
k = -1
cipher = ''
for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c) + k) % (len(alphabet))]
print('Your encrypted message is: ' + cipher)
'''
decryption only
'''
plaintext = input('Enger message: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
k = -1
cipher = ''
for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c) - k) % (len(alphabet))]
print('Your encrypted message is: ' + cipher)

# Method 2: Return both encryption and decryption (key can be changed)
from string import ascii_uppercase as up
from string import ascii_lowercase as low
plain_text = str(input("Enter text: "))
key = int(input('Enter key (1-26): '))
def caesar(plain_text, key):
    cipher_text = ''
 
    for char in plain_text:
        if not char.isalpha():
            cipher_text += char
        else:
            if char.isupper():
                cipher_text += up[(up.find(char) + key) % 26]
            else:
                cipher_text += low[(low.find(char) - key) % 26]
    return cipher_text
print(plain_text)
 
def encrypt(plain_text, key):
    return caesar(plain_text, key)
print(encrypt(plain_text, key))
 
def decrypt(cipher_text, key):
    return caesar(cipher_text, -key)
print(decrypt(plain_text, key))

# Method 3: encryption and decryption (Best of the three methods)
Plain_alphabet = 'abcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(Plain_alphabet)

def getMode():
    while True:
        print('Do you want to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return(mode)
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
            
def getMessage():
    print('Enter your message: ')
    message = input()
    message = message.lower()
    return(message) 

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return(key)

def getTranlatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    
    for symbol in message:
        symbolIndex = Plain_alphabet.find(symbol)
        if symbolIndex == -1: 
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(Plain_alphabet):
                symbolIndex -= len(Plain_alphabet)
            elif symbolIndex < 0:
                symbolIndex += len(Plain_alphabet)
            translated += Plain_alphabet[symbolIndex]
    return(translated)

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranlatedMessage(mode, message, key))


# Challenge 4
# Implement a function that counts the number of isograms in a list of strings.

# Method 1
list_or_words =['conduct', 'letter', 'contract', 'hours', 'interview']
def count_isograms(list_or_words):
    return [len(set(x)) == len(x) for x in list_or_words].count(True)   
print(count_isograms(list_or_words))

# Method 2
list_or_words =['conduct', 'letter', 'contract', 'hours', 'interview']
def count_isograms(list_or_words):
    return (sum((len(set(x)) == len(x)) for x in list_or_words))
print(count_isograms(list_or_words))

# Method 3
list_or_words =['conduct', 'letter', 'contract', 'hours', 'interview']
def count_isograms(list_or_words):
    return(len([x for x in list_or_words if len(x) == len(set(x))]))
print(count_isograms(list_or_words))


# Challenge 5 
#Write a function that manually sorts a list of integers. Do not use the built-in sorted() function or the .sort() string method.    

# Method 1 (simpler than Method 2)
numbers = [4, 6, 9, 1, 2, 6]
def manual_sort(num):
    output = []
    while num:
        smallest = min(num)
        index = num.index(smallest)
        output.append(num.pop(index))
    return(output)
print(manual_sort(numbers))

# Method 2
numbers = [4, 6, 9, 1, 2, 6]
def manual_sort(num):
    manually_sorts = []
    lowest = num[0]
    i = 0
    while len(num) > 0:
        if num[i] < lowest:
            lowest = num[i]
        i += 1
        if i == len(num):
           manually_sorts.append(lowest)
           num.remove(lowest)
           if num:
               lowest = num[0]
           i = 0
    return(manually_sorts)
print(manual_sort(numbers))