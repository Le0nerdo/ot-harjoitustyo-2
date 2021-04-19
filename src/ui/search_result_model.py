import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class SearchModel(QtCore.QAbstractListModel):

    def __init__(self, movie_list = []):
        super().__init__()
        self.movie_list = movie_list

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.movie_list[index.row()].title \
                + " " + self.movie_list[index.row()].description
            return text

    def rowCount(self, index):
        return len(self.movie_list)