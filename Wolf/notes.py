import os
import socket
import re

# destination folder containing the user info
destination_path = f'C:\\Wolf\\users\\{socket.gethostname()}'

# list of predictions
prediction = ['create', 'make', 'new', 'note', 'view', 'delete', 'remove', 'preview', 'see', 'open', 'edit', 'change', 'my',
              'a', 'the', 'notes']
prediction_voice = ['create', 'make', 'new', 'note', 'a', 'notes']


# function to check whether a note exist or not
def catatan_exist():
    os.chdir(destination_path)
    for note in os.listdir():
        if note == 'usernote.notes':
            return True
        else:
            pass
    return False


# function to delete note
def delete_note():
    os.chdir(destination_path)
    ada_catatan = catatan_exist()
    if ada_catatan:
        os.remove('usernote.notes')
        return None, 'Note successfully deleted'
    else:
        return None, 'No notes found, You can create one by saying "make a new note" when Wolf prompts the command or ' \
                     f'by typing it.'


# function to make and view note
def note(input_check_result, input='non'):
    # regex to find the note wrapped in double quote marks
    catatan_note = re.findall(r'\s*(".+")\s*', input)

    # replace the double quote marks with nothing since they're included in the search
    try:
        catatan_note = catatan_note[0].replace('"', '')

    # if doesn't find any double quote marks then pass
    except:
        pass

    # removing things in prediction if it's in input. __ne__ is to delete all occurring
    # things that are present in the list if it's present in the prediction list,
    # this is why the for loop is necessary
    for prediction in input:
        if prediction in prediction:
            input = list(filter(prediction.__ne__, input))
        else:
            pass
    print(catatan_note)
    os.chdir(destination_path)
    ada_catatan = catatan_exist()
    print(f'{ada_catatan} aaaaa')

    # if the check result is view then it views the note
    if input_check_result[-1] == 'view':
        try:
            with open('usernote.notes', 'r', encoding='utf-8') as user_note:
                user_note = user_note.read()
            return None, f'Here is your note:\n\n{user_note}'
        except:
            return None, f'No notes yet, you can create it by saying \'make a new note\' when Wolf prompts' \
                         f' the command or by typing it in the command bar followed by the note wrapped in double' \
                         f' quotation marks -> Make a new note "Hello World!"'

    # if the check result is make then it'll make a new note and overwrites the already existing one
    elif input_check_result[-1] == 'make':
        user_note = open('usernote.notes', 'w', encoding='utf-8')
        if catatan_note == []:
            return None, f'Please specify your note by using double quotation marks.' \
                         f' example: Make a new note "Hello World!"'
        else:
            pass
        user_note.write(catatan_note)
        user_note.close()
        return None, f'Done! Your note has been saved.\nYou can view it by saying \'view my note\' when Wolf ' \
                     f'prompts the command or by typing it, or delete it by saying \'delete my note\' when Wolf ' \
                     f'prompts the command or by typing it. Note that you can only make one note as of now.'


# checking the user input
def check_userinput(input):
    command = None
    user_input = input.split()
    counter = 0

    for userinput in user_input:
        if userinput in prediction:
            counter += 1
        else:
            pass

    for perintah in user_input:
        print(perintah)
        if perintah == 'view' or perintah == 'preview' or perintah == 'see' or perintah == 'open':
            command = 'view'
            break
        if perintah == 'new' or perintah == 'make' or perintah == 'create':
            command = 'make'
            break
        if perintah == 'delete' or perintah == 'remove':
            command = 'delete'
            break
        if perintah == 'edit' or perintah == 'change':
            command = 'edit'
            break

    return counter, command

# debugging
"""
while True:
    usrinput = input('enter ur search query: ')
    check_note = check_userinput(usrinput)
    print(check_note)
    print(check_note[-1])
    if check_note[0] >= 3:
        if check_note[-1] == 'view':
            print(note(input_check_result=check_note, input=usrinput))
        elif check_note[-1] == 'make':
            print(note(input_check_result=check_note, input=usrinput))
        elif check_note[-1] == 'edit':
            print('Not supported yet.')
        elif check_note[-1] == 'delete':
            print(delete_note())
        else:
            pass
    else:
        pass
# """