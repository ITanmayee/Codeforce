"""

Eleven wants to choose a new name for herself. As a bunch of geeks, her friends suggested an algorithm to choose a name for her. Eleven wants her name to have exactly n characters.


Her friend suggested that her name should only consist of uppercase and lowercase letters 'O'. More precisely, they suggested that the i-th letter of her name should be 'O' (uppercase) if i is a member of Fibonacci sequence, and 'o' (lowercase) otherwise. The letters in the name are numbered from 1 to n. Fibonacci sequence is the sequence f where

f1 = 1,
f2 = 1,
fn = fn - 2 + fn - 1 (n > 2).

As her friends are too young to know what Fibonacci sequence is, they asked you to help Eleven determine her new name.

"""

def frameName(no_of_chars):
    if no_of_chars < 2:
        return 'O' * no_of_chars
    name = ['O'] + ['O'] + ['o'] * (no_of_chars - 2)
    f1, f2 = 1, 1
    
    
    while f1 + f2 <= no_of_chars:
        f3 = f1 + f2
        name[f3 - 1] = 'O'
        f2, f1 = f3, f2

    return ''.join(name)


no_of_chars = int(input())

print(frameName(no_of_chars))
