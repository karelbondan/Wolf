# predictions
predictions = ['shutdown', 'restart', 'reboot', 'the', 'my', 'computer', 'pc', 'laptop', 'notebook']


def check_input(input):
    # if user types 'shut down' instead of 'shutdown' it'll replace.
    if 'shut down' in input:
        input = input.replace('shut down', 'shutdown')

    # splitting the user input to make it easier
    user_input = input.split()

    # initial variables
    counter = 0
    state = None

    # checking the input
    for prediction in user_input:
        if prediction in predictions:
            if prediction == 'shutdown':
                state = 'shutdown'
                counter += 1
            elif prediction == 'restart' or prediction == 'reboot':
                state = 'restart'
                counter += 1
            counter += 1

    return counter, state
