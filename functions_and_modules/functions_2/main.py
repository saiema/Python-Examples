from strings import count_substrings, index_of

my_string: str = "the brown fox jumped over the fence and landed on a mine"
my_target: str = "the"
print("string `{}` contains `{}` a total of `{}` times".format(
        my_string,
        my_target,
        count_substrings(my_string, my_target)
    )
)
