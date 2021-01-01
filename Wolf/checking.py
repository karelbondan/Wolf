import random
import os
import string

# this dictionary below was gonna be used as the text to integer or float conversion until I found the
# wolfram module. I repurposed below dictionary as a checker for the user input on the final assistant.
# if the input has number on it and it has an operand(s), it will then go to the wolfram calculation query.
international_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'point': '.',
}

# these are the things that will be used on the assistant as predictions. As I'm not using
# machine learning to make this, I use predictions which I've made below. The international_operands
# is made to check the user input, as explained above.
international_operands = ['plus', 'divided', 'times', 'minus', '+', '-', '/', '*', 'x', 'power', '^', 'modulo']
preposition = ['in', 'on', 'at']
misc = ['a', 'the', 'define', 'what', 'is', 'wikipedia', 'wiki']
predictions = ['search', 'for', 'what', 'is', 'define', 'who', 'in', 'on', 'at', 'google', 'bing', 'yahoo', 'youtube',
               'open', 'and', 'duckduckgo', 'play', 'stack', 'overflow', 'stackoverflow', 'reddit']
prediction_2 = ['play', 'search']
yt_case = ['youtube', 'yt', 'music', 'stack', 'overflow', 'stackoverflow', 'reddit']
websites = ['youtube', 'yt', 'music', 'stack', 'overflow', 'stackoverflow', 'reddit', 'bing', 'google', 'yahoo',
            'duckduckgo']
searches = {'youtube': {'music': 'https://music.youtube.com/search?q=', 'youtube': 'https://www.youtube.com/search?q='},
            'bing': 'https://www.bing.com/search?q=', 'yahoo': 'https://search.yahoo.com/search?q=',
            'google': 'https://www.google.com/search?q=', 'duckduckgo': 'https://duckduckgo.com/?q=',
            'stackoverflow':'https://www.stackoverflow.com/search?q=', 'reddit':'https://www.reddit.com/search/?q='}

after_search = {'youtube': 'Enjoy watching!', 'youtube music': 'Enjoy listening to the rythm!',
                'google': 'Here are the results from Google.', 'bing': 'Here are the results from Bing.',
                'yahoo': 'Here are the results from Yahoo.',
                'duckduckgo': 'Here are the results from DuckDuckGo.',
                'stackoverflow': 'Here are the result from Stack Overflow.',
                'reddit':'Here are the result from Reddit.'}

predictions_doing_tasks = ['assist', 'what', 'can', 'you', 'do', 'wat', 'u', 'me', 'how']
predictions_telling_name = ['wat', 'what', 'ur', 'your', 'name']
predictions_telling_username = ['wat', 'what', 'my', 'name']
predictions_telling_jokes = ['tell', 'joke', 'jokes', 'entertain', 'me', 'amuse', 'make', 'laugh']

# dictionary containing the path of the commonly used applications on Windows.
applications = {'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
                'powerpoint': "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE",
                'chrome': "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe",
                'firefox': "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
                'photoshop': "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2018\\Photoshop.exe",
                'pycharm': "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe",
                'notepad': 'C:\\Windows\\system32\\notepad.exe',
                'edge': "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
                'explorer': 'C:\\Windows\\explorer.exe',
                'youtube': 'https://www.youtube.com',
                'google': 'https://www.google.com',
                'bing': 'https://www.bing.com',
                'yahoo': 'https://www.yahoo.com',
                'reddit': 'https://www.reddit.com',
                'duckduckgo': 'https://www.duckduckgo.com'}

# the sentence the assistant will say after it has found a result.
final_words = ['You can read more on the results I\'ve shown', 'Here are the results from the web',
               'You can read more on the web', 'Feel free reading more from the web results',
               'Here are more explanations from your question', 'I hope you\'re satisfied with my answer']

# the 'randomize' variable below is made to randomize the final_words so the user doesn't get bored
# of the same thing the assistant says after finding the result. This variable will then
# be passed onto the gTTS parameter which is the text the assistant going to say.
randomize = random.choice(final_words)

# randomize the response when user asks Wolf how's it feeling today.
def randomize_response():
    response_sequence = ['I\'m feeling very fine today! Thank you for asking.',
                         'I\'m feeling really generous today. Gotta find some sheeps to play with!',
                         'You know, sometimes I feel down. Sheeps are my best friend to vent out.',
                         'Woof woof woof woof woof!', 'I\'m feeling eager to help you. How can I help?',
                         'I really wish I could play outside with you.',
                         'Woof to the left, woof to the right! Oh... sorry.. I\'m feeling excited today!']

    response = random.choice(response_sequence)
    return response

# from this point on, ignore what has been written below. I was gonna make a text to integer or float to act as a
# simple calculator, but then I found the wolfram module which helps reducing the time of making this a lot.
# I just wanna keep this here as a remembrance of my attempt making it :')
"""
def word_to_int(input):
    angka = ['one','two','three','four','five','six','seven','eight','nine']
    puluhan = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', #twenty twenty one
               'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    ratusan = ['hundred','thousand','million','billion']
    test = ''
    counter = 0
    if 'and' in input:
        input.remove('and')
    if len(input) == 1:
        calc = 0
        for num in input:
            calc += international_number[num]
        print(calc)
    elif len(input) == 2 and input[1] in angka:
        calc = 0
        for num in input:
            calc += international_number[num]
        print(calc)
    elif input[0] in puluhan or input[0] in angka and input[1] not in ratusan:
        try:
            for num in input:
                if counter == 1:
                    counter -= 1
                    break
                else:
                    test += f'{international_number[num]}'
                    counter += 1
                calculation = international_number.get(input[1])+international_number.get(input[2])
                test += f'{calculation}'
        except IndexError:
            test = ''
            for num in input:
                test += f'{international_number[num]}'
        print(test)
    elif input[1] == 'hundred':
        calc1 = international_number.get(input[0])*international_number.get(input[1])
        calc2 = 0
        for num in input:
            if counter < 2:
                counter += 1
                pass
            else:
                try:
                    if counter != 3:
                        counter += 1
                        calc2 = international_number[num]
                    else: calc2 += international_number[num]
                except IndexError: break
        calculation = calc1 + calc2
        print(calculation)
    elif input[1] == 'thousand':
        calc1 = international_number.get(input[0])*international_number.get(input[1])
        calc2 = 0
        calc3 = 0
        for num in input:
            if counter < 2:
                counter += 1
                pass
            else:
                try:
                    if counter < 3:
                        counter += 1
                        calc2 = international_number[num]
                    elif num == 'hundred':
                        counter += 1
                        calc2 = calc2 * international_number[num]
                    else:
                        calc3 += international_number[num]
                except IndexError: break
        calculation = calc1 + calc2 + calc3
        print(calculation)
    elif input[1] == 'million':
        temp = [international_number.get(input[0])*international_number.get(input[1])]
        calc2 = 0
        for num in range(len(input)):
            if input[num] in angka:
                if counter >= 1:
                    calc2 += international_number.get(input[num])
                else:
                    counter+=1
                    pass
            elif input[num] == 'thousand' or input[num] == 'hundred':
                calc2 = calc2*international_number.get(input[num])
                temp.append(calc2)
                calc2 = calc2*0
            elif input[num] == 'million': pass
            else:
                calc2 += international_number.get(input[num])
            if num == len(input)-1:
                temp.append(calc2)
                calc2 = calc2*0
        for i in temp:
            calc2 += i
        print(calc2)
    elif input[1] == 'billion':
        temp = [international_number.get(input[0])*international_number.get(input[1])] #five billion nine million six thousand four hundred and fifty five
        calc2 = 0
        for num in range(len(input)):
            if input[num] in angka:
                if counter >= 1:
                    calc2 += international_number.get(input[num])
                else:
                    counter+=1
                    pass
            elif input[num] == 'thousand' or input[num] == 'hundred' or input[num] == 'million':
                calc2 = calc2*international_number.get(input[num])
                temp.append(calc2)
                calc2 = calc2*0
            elif input[num] == 'billion': pass
            else:
                calc2 += international_number.get(input[num])
            if num == len(input)-1:
                temp.append(calc2)
                calc2 = calc2*0
        for i in temp:
            calc2 += i
        print(calc2)



def main():
    a = input(f'Enter a number on word: ').strip().split(' ')
    return word_to_int(a)

main()
"""