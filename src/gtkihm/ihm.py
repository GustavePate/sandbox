'''
Created on 4 janv. 2013

@author: b9669
'''

import gtk


if __name__ == '__main__':
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    label = gtk.Label("Hello World!")
    window.add(label)
    label.show()
    window.show()
    gtk.main()   
    