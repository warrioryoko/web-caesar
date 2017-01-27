def alphabet_position(letter):
    if not letter.isalpha():
        return letter
    elif letter.islower():
        scrubbed_letter = letter.upper()
    else:
        scrubbed_letter = letter
    charlist= map(chr, range(65, 91))
    chardict = {x:y for (y,x) in enumerate(charlist)}
    charvalue = chardict[scrubbed_letter]
    return charvalue

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    elif char.isupper():
        charlist = map(chr, range(65, 91))
        chardict = {x:y for (x, y) in enumerate(charlist)}
        rot_value = ((alphabet_position(char) + rot) % 26)
        rot_char = chardict[rot_value]
        return rot_char
    else:
        charlist_lower = map(chr, range(97, 123))
        chardict_lower = {x:y for (x, y) in enumerate(charlist_lower)}
        rotlower_value = ((alphabet_position(char) + rot) % 26)
        rotlower_char = chardict_lower[rotlower_value]
        return rotlower_char


def encrypt(text, rot):
    new_sentence = []
    for char in text:
        new_sentence.append(rotate_character(char, rot))
    sentence_out = "".join(new_sentence)
    return sentence_out

def main():
    return encrypt(sentence, rotation)

if __name__ == '__main__':
    main()
