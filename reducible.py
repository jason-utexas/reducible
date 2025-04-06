"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Jason Li and Skyler Nguyen, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: jxl237
UT EID 2: sn28523
"""

# the constant used to calculate the step size
STEP_SIZE_CONSTANT = 3


# DO NOT modify this function.
def is_prime(n):
    """
    Determines if a number is prime.

    pre: n is a positive integer.
    post: Returns True if n is prime, otherwise returns False.
    """
    if n == 1:
        return False

    limit = int(n**0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# DO NOT modify this function.
def hash_word(s, size):
    """
    Hashes a lowercase string to an index in a hash table.

    pre: s is a lowercase string, and size is a positive integer representing either
         hash table size or the constant for double hashing.
    post: Returns an integer index in the range [0, size - 1] where the string hashes to.
    """
    hash_idx = 0
    for c in s:
        letter = ord(c) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# TODO: Modify this function. You may delete this comment when you are done.
def step_size(s):
    """
    Calculates step size for double hashing using STEP_SIZE_CONSTANT.

    pre: s is a lowercase string.
    post: Returns the calculated step size as an integer based on the provided string.
    """
    base = hash_word(s, STEP_SIZE_CONSTANT)
    # The step size is computed based on the provided constant.
    return STEP_SIZE_CONSTANT - (base % STEP_SIZE_CONSTANT)

# TODO: Modify this function. You may delete this comment when you are done.
def insert_word(s, hash_table):
    """
    Inserts a string into the hash table using double hashing for collision resolution.
    No duplicates are allowed.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Inserts s into hash_table at the correct index; resolves any collisions
          by double hashing.
    """
    table_len = len(hash_table)
    index = hash_word(s, table_len)
    step = step_size(s)
    while hash_table[index] != "":
        if hash_table[index] == s:
            return

        index = (index + step)% table_len
    hash_table[index] = s



# TODO: Modify this function. You may delete this comment when you are done.
def find_word(s, hash_table):
    """
    Searches for a string in the hash table.
    Note: using the `in` operator is incorrect as that will be O(N). We want
          an O(1) time average time complexity using hashing.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Returns True if s is found in hash_table, otherwise returns False.
    """
    size = len(hash_table)
    i = hash_word(s, size)
    step = step_size(s)
    while hash_table[i] != "":
        if hash_table[i] == s:
            return True

        i = (i + step)% size

    return False


# TODO: Modify this function. You may delete this comment when you are done.
def is_reducible(s, hash_table, hash_memo):
    """
    Determines if a string is reducible using a recursive check.

    pre: s is a lowercase string, hash_table is a list representing the hash table,
         and hash_memo is a list representing the hash table
         for memoization.
    post: Returns True if s is reducible (also updates hash_memo by
          inserting s if reducible), otherwise returns False.
    """
    if find_word(s, hash_memo):
        return True
    if len(s) == 1 and s in {"a", "i", "o"}:
        insert_word(s, hash_memo)
        return True

    for pos in range(len(s)):
        subword = s[:pos] + s[pos+1:]
        if find_word(subword, hash_table) and is_reducible(subword,hash_table, hash_memo):
            insert_word(s, hash_memo)
            return True

    return False


# TODO: Modify this function. You may delete this comment when you are done.
def get_longest_words(string_list):
    """
    Finds longest words from a list.

    pre: string_list is a list of lowercase strings.
    post: Returns a list of words in string_list that have the maximum length.
    """
    if not string_list:
        return []

    max_length = max(len(word) for word in string_list)
    return [word for word in string_list if len(word) == max_length]


# TODO: Modify this function. You may delete this comment when you are done.
def main():
    """The main function that calculates the longest reducible words"""
    # create an empty word_list

    # read words using input redirection
    # where each line read from input()
    # should be a single word. Append to word_list
    # ensure each word has no trailing white space.

    # find length of word_list

    # determine prime number N that is greater than twice
    # the length of the word_list

    # create an empty hash_list

    # populate the hash_list with N blank strings

    # hash each word in word_list into hash_list
    # for collisions use double hashing

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list

    # populate the hash_memo with M blank strings

    # create an empty list reducible_words

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.

    # find the largest reducible words in reducible_words

    # print the reducible words in alphabetical order
    # one word per line
    word_list = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            word_list.append(stripped)

    n = len(word_list)

    table_size = 2 * n
    while not is_prime(table_size):
        table_size += 1
    hash_table = ["" for _ in range(table_size)]
    for word in word_list:
        insert_word(word, hash_table)

    memo_size = int(0.2 * n)
    while not is_prime(memo_size):
        memo_size += 1
    hash_memo = ["" for _ in range(memo_size)]
    for letter in "aio":
        insert_word(letter, hash_memo)

    reducible = [word for word in word_list if is_reducible(word, hash_table, hash_memo)]
    longest = sorted(get_longest_words(reducible))
    for word in longest:
        print(word)

if __name__ == "__main__":
    main()
