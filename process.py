"""

Filename: process.py
Author: Jason Cramer

The main processing class for the files. Handles iterating through
the files and filtering them.

"""
from os import *
from os.path import *
from shutil import move
import platform

# Determine the slash we need for the OS

if platform.system() == 'Windows':
    slash_char = '\\'
else:
    slash_char = '/'

# Note for later: provide default download directory via:
# getenv("HOME") + slash_char

class DirectoryProcessor(object):

    # TODO: parse JSON config file
    # TODO: save and ecrypt passwords for directories
    def __init__(self, directory, config = [], filters=[]):
        """
        Initializes the object that processes the files in a directory
        
        directory - (str) the directory things will be moved to
        config - (dict) a dictionary containing various user options
        filters - (list[str]) a list of filters, in descending order of priority
        """
        # config should be processed by another module
        try:
            assert isdir(self.directory) == True, 'Target folder is not a directory'
        except:
            self.directory = ''
            # Come up with a better way to handle this bro
        self.directory = directory
        self.filters = filters
        self.config = config
        # Keychain is a dictionary of usernames (owners), with
        # passwords as keys
        self.keychain = self.load_keychain()


    def process(self):
        # Called every time daemon says 'word yo'
        # copy the list so that we can move files without worrying about the list
        for item in list(listdir(self.directory)):
            for filt in filters:
                # TODO: specially/recursively handle directories
                # TODO: implement option to only move new items
                if not isdir(item) and filt.needs_redirecting(item):
                    self.move(item, filt.destination)
                    break


    def move(self, item, destination):
        if self.authenticate(item, destination):
            move(item, destination)
        else:
            # Later, handle with warning message to user
            pass

    def authenticate(self, item, destination):
        # First make sure file is okay to move
        if not access(item, W_OK):
            # Check keychain to see if password is needed
            pass
        # Next, make sure destination is okay to move file
        if not access(destination, W_OK):
            pass 
    
    def load_keychain(self):
        return None

    def add_password(self):
        return None
