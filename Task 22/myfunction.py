
#function to list the days of the weeks
#print the days of the week using print statement
def functionWeekdays():
    print("Monday")

    print("Tuesday")
    
    print("Wednesday")

    print("Thursday")

    print("Friday")

    print("Saturday")

    print("Sunday")
functionWeekdays()

sentence = input("Please type out a sentence:")

def replaceHello(sentence):
    sentenceHello = " "
    i = 0
    for word in sentence.split():
        # if the index is 2 hello will be added in place
        if i % 2 == 1:
            sentenceHello += "Hello"
        #otherwise the word of the sentence
        else:
            sentenceHello += word + " "
        i = i + 1
    sentenceHello = sentenceHello[ :-1]
    return sentenceHello
print(replaceHello(sentence))       
