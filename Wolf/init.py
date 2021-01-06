import os
import shutil

# dir containing the user profile pic on Windows 10
dir = f'{os.environ["USERPROFILE"]}\\AppData\\Roaming\\Microsoft\\Windows\\AccountPictures'

# dir containing the default user picture icon
dir2 = f'C:\\ProgramData\Microsoft\\User Account Pictures'

# dir containing the file to convert the ms-accountpicture file into bmp
dir3 = f'C:\\Gonpachiro\\images\\convert'

# empty list to store the userimages
userimage = []

# initial variable
final_image = None


def main():
    global final_image
    # try to access the image, if file not exist then goes to exception
    try:
        os.chdir(dir)
        for userimages in os.listdir():
            userimage.append(userimages)
        final_image = userimage[-2]

    # appending the default user profile image to the userimage list
    except:
        os.chdir(dir2)
        for defaultimage in os.listdir():
            if defaultimage == 'user.png':
                final_image = defaultimage
                break

    # if the pic is default profile image then pass the convertion
    if final_image == 'user.png':
        shutil.copy(f'{dir}\\{final_image}', f'{dir3}\\user.png')
        for image in os.listdir():
            if image == 'user.png':
                final_image = image
                break

    # else convert the ms-accountpicture file to bmp. credit to the file
    # will be on the readme.md on Wolf/images/convert
    else:
        os.chdir(dir3)
        shutil.copy(f'{dir}\\{final_image}', f'{dir3}\\user.accountpicture-ms')
        os.system('cmd /c "AccountPicConverter user.accountpicture-ms')
        for image in os.listdir():
            if image == 'user-448.bmp':
                final_image = image
                break
    return final_image


# debugging
print(userimage)
print(final_image)
