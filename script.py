import os
import shutil


for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)
    if file_extension == ".txt":
        if not os.path.exists("text"):
            os.mkdir("text")
        shutil.move(f"{file_name}.txt", f'text/{file_name}.txt')
    elif file_extension == ".jpg" or file_extension == ".png":
        if not os.path.exists("images"):
            os.mkdir("images")
        shutil.move(f"{file_name}{file_extension}", f"images/{file_name}{file_extension}")
    else:
        if not os.path.exists("else"):
            os.mkdir("else")
        if file_extension != ".py":
            shutil.move(f"{file_name}{file_extension}", f"else/{file_name}{file_extension}")

print("Files Deplaced Succesfully")



