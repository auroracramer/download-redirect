"""

Filename: filters.py
Author: Jason Cramer

Classes for file filters. 

"""


"""
Things to keep in mind:

Prioritize filters
Rename

"""


from abc import ABCMeta, abstractmethod


class FileFilter(object):

    """
    The base class for filters, providing the interface for the subclasses
    """

    __metaclass__ = ABCMeta

    def __init__(self, filter_string, destination):
        """
        Set the instance variables for the string used for filtering, and the
        destination for the files that fit the filter.
        """
        assert self.input_check(filter_string, destination) == True, 'Erroneous arguments'
        self._filter_string = filter_string
        self._destination = destination
    
    @abstractmethod     
    def needs_redirecting(self, filename):
        """
        Returns true if the file needs to be redirected, i.e. the filename
        fits is the filter.
        """
        # Implemented by subclass
        return False

    @abstractmethod
    def input_check(self, filter_string, destination):
        """
        Ensures that inputs are correct
        """
        return False

    def filter_string(self):
        """
        Returns the string of the filter.
        """
        return self._filter_string

    def destination(self):
        """
        Returns the filter's destination for files.
        """
        return self._destination

class ExtFileFilter(FileFilter):
    """
    Filters files based on file extension.
 
    Filter string should be a file extension (starting with a '.').
    
    >>> filt = ExtFileFilter('.txt', '~/')
    >>> assert filt.destination() == '~/', "ExtFileFilter: Destination is incorrect"
    >>> assert filt.filter_string() == '.txt', "ExtFileFilter: Filter string is incorrect"
    
    """

    def needs_redirecting(self, filename):
        return filename.endswith(filter_string)

    def input_check(self, filter_string, destination):
        # Keep in mind the direction of the slash between Unix and Windows
        # Check that the filter string begins with a period
        return filter_string[0] == '.'

# Register subclasses of FileFilter
FileFilter.register(ExtFileFilter)




