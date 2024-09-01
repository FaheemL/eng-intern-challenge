import sys


braille_chars = {


    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',
    
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    
    
    ' ': '......',        
    'capital': '.....O',  
    'number': '.O.OOO'    

}

english_chars = {

    v: k for k, v in braille_chars.items()
}

def check_if_braille(s):
    return all(char in 'O.' for char in s)


def eng_to_braille(s):
    braille_text = ''
    num = False

    for char in s:
        if char.isdigit():
            if not num:
                braille_text += braille_chars['number']
                num = True
            braille_text += braille_chars[char]
        elif char.isalpha():
            if char.isupper():
                braille_text += braille_chars['capital']
                char = char.lower()
            braille_text += braille_chars[char]
            num = False
        elif char == ' ':
            braille_text += braille_chars[' ']
            num = False

    return braille_text

def braille_to_eng(s):
    eng_text = ''
    i = 0
    capital = False
    num = False

    while i < len(s):
        braille_char = s[i:i+6]

        if braille_char == braille_chars['capital']:
            capital = True
            i += 6
            continue

        elif braille_char == braille_chars['number']:
            num = True
            i += 6
            continue

        elif braille_char == braille_chars[' ']:
            eng_text += ' '
            num = False
            i += 6
            continue

        if braille_char in english_chars:
            char = english_chars[braille_char]

            if capital:
                char = char.upper()
                capital = False


            if num and char.isdigit():
                eng_text += char

            elif not num:
                eng_text += char

            else:
                num = False
        

        i += 6

    return eng_text


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    input_string = sys.argv[1]

    if check_if_braille(input_string):
        print(braille_to_eng(input_string))
    else:
        print(eng_to_braille(input_string))


if __name__ == "__main__":
    main()







    