import string

def get_ones_in_bin_2(n):
    sum = 0
    while (n):
        sum += n & 1
        n >>= 1
    return sum



def get_ones_in_bin(n):
    n = bin(n)[2:]
    sum = 0
    for i in n:
        sum += int(i)
    return sum

print(get_ones_in_bin_2(3))

def is_rotation(word, second_word):
    if len(word) != len(second_word):
        return False
    word = word.lower()
    second_word = second_word.lower()

    ch_indexes = [index for index, letter in enumerate(second_word) if letter == word[0]]
    if not ch_indexes:
        return False

    len_word = len(word)

    for ch_ind in ch_indexes:
        for i in range(len_word):
            if second_word[(ch_ind + i) % len_word] != word[i]:
                break
            elif i == (len_word - 1):
                return True    

    return False

#print(is_rotation("hola", "aohl"))


def compress_string(strin):
    comp_str = ""

    count = 1
    for c in range(len(strin) - 1):
        if strin[c] == strin[c + 1]:
            count += 1
        else:
            comp_str += strin[c] + str(count)
            count = 1
    comp_str += strin[c] + str(count)
    
    if len(comp_str) >= len(strin):
        return strin
    else:
        return comp_str[::-1]

print(compress_string("aabbccddddg"))

def get_matrix_median(mtx):
    if len(mtx) == 1:
        vec = mtx[0]
        return vec[len(vec) // 2]
    else:
        new_list = []
        for row in range(len(mtx)):
            new_list.extend(mtx[row])
            new_list = sorted(new_list)
            print(new_list)
    return new_list[len(new_list)//2]

#print(get_matrix_median([[1,3,9,5],[2,6,4,9],[3,6,12,12,9]]))

def is_anagram(str, str_2):
    str = str.replace(" ", "")
    str_2 = str_2.replace(" ", "")
    if len(str) != len(str_2):
        return False
    str = str.lower()
    str_2 = str_2.lower()

    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for c in range(len(str_2)):
        dict_1[str[c]] += 1
        dict_2[str[c]] += 1
    
    return dict_1 == dict_2

#print(is_anagram("lola", "alols"))






def urlify(str):
    str_len = len(str)
    url = ""
    for c in range(len(str)):
        if str[c] == " ":
            url += "%20"
        else:
            url += str[c]
    return url

#print(urlify("http://www.marioal.com/hola?mario alberto vazquez"))

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

#print(factorial_recursive(10))

def fizz_buzz():
    N = 15
    for i in range(1, N + 1):
        of_three = i % 3 == 0
        of_five = i % 5 == 0
        if (of_five and of_three):
            print("FizzBuzz")
        elif of_three:
            print("Fizz")
        elif of_five:
            print("Buzz")
        else:
            print(i)


def find_unique(arr):
    ans = 0
    for n in range(len(arr)):
        ans ^= arr[n]
    return ans

#print(find_unique([1,2,3,3,2,0,1,0,7]))

        

def two_sum(n, t):
    if (len(n) <= 1):
        return False
    aux_dict = {}
    for i in range(len(n)):
        if n[i] in aux_dict:
            return [aux_dict[n[i]], i]
        else:
            aux_dict[t - n[i]] = i
    return 0

#print(two_sum([1,2,3,4,5],5))

str_1 = "aadriving"
str_2 = "vgindrai"

def is_permutation(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")
    
    if len(str_1) != len(str_2):
        return print(False)
    
    for c in str_1:
        if c in str_2:
            str_2 = str_2.replace(c, "")
    
    return print(len(str_2) == 0)

#is_permutation(str_1, str_2)

def is_palindrome(s):
    s = s.lower()
    s = s.translate(string.punctuation)
    s = s.replace(" ", "")

    return s == s[::-1]

#print(is_palindrome(".Hol  a loH."))