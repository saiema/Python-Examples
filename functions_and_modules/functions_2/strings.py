def is_substring(haystack: str, needle: str) -> bool:
    """
    Search if a string is a substring of another
    :param haystack: the string in where to search
    :param needle: the substring to search
    :return: True iff 'needle' is a substring of 'haystack'
    """
    pass


def is_subsequence(haystack: str, needle: str) -> bool:
    """
    Search if a string is a subsequence of another
    :param haystack: the string in where to search
    :param needle: the subsequence to search
    :return: True iff 'needle' is a subsequence of 'haystack'
    """
    pass


def generate_all_substrings(string: str) -> list[str]:
    """
    Generates all substrings of a given string
    :param string: the given string
    :return: a list of all substrings of 'string'
    """
    pass


def generate_all_subsequences(string: str) -> list[str]:
    """
    Generates all subsequences of a given string
    :param string: the given string
    :return: a list of all subsequences of 'string'
    """
    pass


def to_upper_case(string: str) -> str:
    """
    Returns an upper case version of a string
    :param string: the original string
    :return: an upper case version of 'string'
    """
    upper: str = ""
    for c in string:
        if 'a' <= c <= 'z':
            upper += chr(ord(c) - 32)
        else:
            upper += c
    return upper


def to_lower_case(string: str) -> str:
    """
    Returns a lower case version of a string
    :param string: the original string
    :return: a lower case version of 'string'
    """
    lower: str = ""
    for c in string:
        if 'A' <= c <= 'Z':
            lower += chr(ord(c) + 32)
        else:
            lower += c
    return lower


def reverse(string: str) -> str:
    """
    Reverses a string
    :param string: the string to reverse
    :return: a reversed version of 'string'
    """
    rev: str = ""
    for c in string:
        rev = c + rev
    return rev
    
def count_substrings(string: str, substring: str) -> int:
    """
    Given a string and a substring, counts the occurences of the second in the first
    :param string: the string in which to search
    :param substring: the substring to search
    :return: How many times 'substring' occurs in 'string'
    """    
    if len(substring) == 0:
        return 1
    count: int = 0
    target_index: int = index_of(string, substring)
    while target_index != -1:
        count = count + 1
        string = string[target_index + len(substring):]
        target_index = index_of(string, substring)
    return count
    
    
def index_of(string: str, target: str) -> int:
    assert string is not None
    assert target is not None
    if len(target) == 0:
        return 0
    if len(string) == 0:
        return -1
    if len(target) > len(string):
        return -1
    found: bool = False
    idx: int = 0
    remaining_length: int = len(string)
    # My last index would be at len(string) - 1
    # At the start, the length of available string is len(string) - idx
    while not found and remaining_length >= len(target):
        if starts_with(string[idx:], target):
            found = True
        else:
            idx = idx + 1
            remaining_length = remaining_length - 1
    if not found:
        return -1
    return idx
    
def starts_with(string: str, target: str) -> bool:
    assert string is not None
    assert target is not None
    if len(target) == 0:
        return True
    if len(string) == 0:
        return False
    for i in range(len(target)):
        if string[i] != target[i]:
            return False
    return True
   
            
        
    
    
    
    
    
    

