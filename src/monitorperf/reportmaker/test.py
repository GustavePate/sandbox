import os
import urllib2

from PIL import Image


def get_python_image(filename):
    """ Get a python logo image for this example """
    if not os.path.exists(filename):
        response = urllib2.urlopen(
            'http://www.python.org/community/logos/python-logo.png')
        f = open(filename, 'w')
        f.write(response.read())
        f.close()

if __name__ == '__main__':
    get_python_image("python.png")
    im = Image.open("python.png")
    im2=im.resize((200,200),Image.ANTIALIAS)
    im2.save("python.png",'PNG')