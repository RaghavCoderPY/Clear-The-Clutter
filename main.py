import os

files = os.listdir("images/")
for i, file in enumerate(files):
    os.rename(f"images/{file}", f"{i}.jpg")

