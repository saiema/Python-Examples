#print(is_palindrome("Hello"));

def is_palindrome(string: str) -> bool:
    assert string is not None
    middle_idx: int = len(str) / 2
    for i in range(middle_idx):
        comp_idx: int = len(str) - 1 - i
        if string[i] != string[comp_idx]:
            return False
    return True
    
#print(is_palindrome("Hello"))
    
def is_palindrome_using_reverse(string: str) -> bool:
    assert string is not None
    return string == reverse(string)
    
#print(is_palindrome_using_reverse("Hello"))
    
def reverse(string: str) -> str:
    assert string is not None
    reverse: str = ""
    for i in range(len(string)):
        j: int = -1 - i
        reverse += string[j]
    return reverse
    
#print(is_palindrome_using_reverse("Hello"))
    
def test_reverse(string: str) -> None:
    assert string is not None
    reverse: str = ""
    for i in range(len(string)):
        j: int = -1 - i
        reverse += string[j]
        print("{} at {} is {}\n".format(string, j, string[j]))
        
        
#test_reverse("Hello")

