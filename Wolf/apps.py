import checking


def check_userinput(input):
    app_name = None
    counter = 0
    user_input = input.split()
    prediction = ['open', 'start']
    for apps in user_input:
        if apps in checking.applications.keys():
            app_name = apps
            counter += 1
        elif apps in prediction:
            counter += 1

    return counter, app_name
