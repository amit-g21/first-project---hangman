# functions
def choose_word(word_list, word_num):
    list_word = word_list.split(" ")
    return list_word[word_num-1]

HANGMAN_PHOTOS={"picture 1":r"""x-------x""" , "picture 2" :
    r"""x-------x
        |
        |
        |
        |
        |
""" ,

       "picture 3":r"""  
       x-------x
       |       |
       |       0
       |
       |
       |""" ,
        
        "picture 4" : r"""     
        x-------x
        |       |
        |       0
        |       |
        |
        |
""",
       
        "picture 5":r"""      
        x-------x
        |       |
        |       0
        |      /|\
        |
        | 
""" ,

        "picture 6":r"""     
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |          
""" ,

        "picture 7":r"""      
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        | 
"""}

def print_hangman(num_of_tries):

    if num_of_tries == 1:
        print(HANGMAN_PHOTOS["picture 1"])

    elif num_of_tries == 2:
        print(HANGMAN_PHOTOS["picture 2"])

    elif num_of_tries == 3:
        print(HANGMAN_PHOTOS["picture 3"])

    elif num_of_tries == 4:
        print(HANGMAN_PHOTOS["picture 4"])

    elif num_of_tries == 5:
        print(HANGMAN_PHOTOS["picture 5"])

    elif num_of_tries == 6:
        print(HANGMAN_PHOTOS["picture 6"])

    elif num_of_tries == 7:
        print(HANGMAN_PHOTOS["picture 7"])

def try_update_letter_guessed(letter_guessed,old_letters):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters:
            print("x")
            print("->".join(old_letters[0::1]))
            return False      
    else:
        old_letters.append(letter_guessed)
        print(old_letters)
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    new = ""
    for char in secret_word:
        if char in old_letters_guessed:
            new += char
        else:
            new += " _ "
    return new

def check_win(word_guessued, old_letters_guessed):
    for letter in word_guessued:
        if letter not in old_letters_guessed:
            return False
    return True


# main
if __name__ == '__main__':
    HANGMAN_ASCII_ART=r"""
    Welcome to the game Hangman
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/"""
    MAX_TRIES=6

    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


    words_input_list=open(r"C:\Users\עמית\OneDrive\שולחן העבודה\python\hangman\words_name(hangman).txt","r")
    word_list=words_input_list.read()

    word_num =int(input("enter a number:"))

    chosen_word = choose_word(word_list, word_num)

    print_hangman(1)

    print("_ " * len(chosen_word))

    old_letters=[]
    
    mistakes = 0

    while mistakes < MAX_TRIES:
        letter_guessed=input("enter letter:")

        correct = try_update_letter_guessed(letter_guessed,old_letters)
        if correct == True:
            if letter_guessed in chosen_word:
                print(show_hidden_word(chosen_word, old_letters))
            else:
                print(":(")
                mistakes += 1
                print_hangman(mistakes)
        if check_win(chosen_word, old_letters) == True:
            break

    if check_win(chosen_word, old_letters)== True:
        print("WIN")

    else:
        print("lose")





  

    



