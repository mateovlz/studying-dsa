# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
def solution(number):
    counter = 0
    if(number > 0):
        for num in range(1,number):
            if( num % 3 == 0 or num % 5 == 0 ):
                counter += num
    else:
        return 0
    return counter
"""
def solution(number):
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0) if number > 0 else 0
"""
def twoSum(nums, target):
    num_list = []
    for i, num in enumerate(nums):
        complement = target - num
        if (complement in num_list):
            return [num_list.index(complement), i]
        num_list.append(num)
    return []
print(f' Number {num} Complement {complement} Target {target} List {num_list}')"""

def twoSum(nums, target):
    return [[i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target][0]


def matrix_vowel(strArray):
    def is_vowel(char):
        return char.lower() in ['a','e','i','o','u']
        
    for column in range(len(strArray)):
        for row in range(len(strArray[column])):
            print(strArray[column][row])


def deordered_phrase_(str):
    str_pre = str[0].lower() + str[1:-1]
    lst_words = str_pre.split(' ')
    dict_word = {}
    for word in lst_words:
        if len(word) in dict_word:
            dict_word[len(word)].append(word)
        else:
            dict_word[len(word)] = [word]
    lst_ordered = sorted(dict_word, reverse=True)

    str_return = ''
    for key in lst_ordered:
        print(key)
        print(dict_word[key])
        str_return += ' '.join(dict_word[key])
        str_return += ' ' 

    print(str_return)
        

def deordered_phrase(input_str):
    # Convert the first character to lowercase
    str_pre = input_str[0].lower() + input_str[1:-1]

    # Split the string into a list of words
    lst_words = str_pre.split()

    # Create a dictionary to store words based on their lengths
    dict_word = {}
    for word in lst_words:
        length = len(word)
        if length in dict_word:
            dict_word[length].append(word)
        else:
            dict_word[length] = [word]

    # Sort the dictionary based on key (word length) in descending order
    sorted_dict = dict(sorted(dict_word.items(), key=lambda x: x[0], reverse=True))

    # Concatenate the words in the sorted order
    str_return = ' '.join([' '.join(words) for length, words in sorted_dict.items()])

    print(str_return)        



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deordered_phrase("There are no way to make this thing faster.")
    #matrix_vowel(['abcd','eikr','oufj'])
    #print_hi('PyCharm')
    #print(f'Here is the result: {solution(-1)}')
    #print(twoSum([2,7,11,15], 9))


