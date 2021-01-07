import checking


# custom exception if the process is not found
class AppNotFoundError(Exception):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def __str__(self):
        return f'Process not found: {self.app}'


# checking user input
def check_userinput(input):
    # initial variables
    app_name = None
    state = None
    counter = 0

    user_input = input.split()  # splitting the input to make it easier to check
    prediction = ['open', 'start', 'close', 'terminate']  # prediction list

    # for loop to check the input
    for apps in user_input:
        if apps in checking.applications.keys():  # search for the app user's trying to open in input
            app_name = apps
            counter += 1

        elif apps in prediction:  # search for the command input
            if apps == 'open' or apps == 'start':
                state = 'open'
                counter += 1
            elif apps == 'close' or apps == 'terminate':
                state = 'close'
                counter += 1
            counter += 1

    return counter, app_name, state
