import os
import shutil

dir = f'{os.environ["USERPROFILE"]}\\AppData\\Roaming\\Microsoft\\Windows\\AccountPictures'
dir2 = f'C:\\ProgramData\Microsoft\\User Account Pictures'
dir3 = f'C:\\Gonpachiro\\images\\convert'

userimage = []
final_image = None


def main():
    global final_image
    try:
        os.chdir(dir)
        for userimages in os.listdir():
            userimage.append(userimages)
        final_image = userimage[-2]

    except:
        os.chdir(dir2)
        for defaultimage in os.listdir():
            if defaultimage == 'user.png':
                final_image = defaultimage
                break
    if final_image == 'user.png':
        shutil.copy(f'{dir}\\{final_image}', f'{dir3}\\user.png')
        for image in os.listdir():
            if image == 'user.png':
                final_image = image
                break
    else:
        os.chdir(dir3)
        shutil.copy(f'{dir}\\{final_image}', f'{dir3}\\user.accountpicture-ms')
        os.system('cmd /c "AccountPicConverter user.accountpicture-ms')
        for image in os.listdir():
            if image == 'user-448.bmp':
                final_image = image
                break
    return final_image


print(userimage)
print(final_image)
