import pickle
from note import Note
from view import View


class ListOfNotes:
    __notes = []
    __view = View()
    __index = 0
    __index_stack = []

