def print_values_of(dictionary, *keys):# *keys to indicate it accepts any number os arguments
    for key in keys: #remove ()
        print(dictionary[key]) # add key for current key

simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", #Parenthesis incorrect ""
                         "maggie": " (Pacifier Suck)"}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

