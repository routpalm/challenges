import os

# Ideally, the important image file will be included in a folder full of other dud images. 
# The player will see, definitively through ls -la, that the image is much bigger than its counterparts, indicating that there is something more to the image.
# The player can use a variety of methods to find the .zip archive inside of the zip file. Then, they can unzip.

# Example directory path
os.system("7z e ~/ritCTF/stgeasy/iyav473h.png")

# In the zip file, there is a .txt file called 'secret.txt'. When output to standard, the flag is not present, but there is a significant amount of white space in the text file. 
# After some research, the player will find that the white space is using the ICE encryption algorithm to encode a message, which is able to be decoded through the linux module stegsnow.

#Example directory path
os.system("stegsnow -C ~/ritCTF/stgeasy/secret.txt")

# After running this command, they will get the flag RS{st3g0_w4lk_432849}
