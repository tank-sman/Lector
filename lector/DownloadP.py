import os
import logging
from ast import literal_eval

from PyQt5 import QtCore, QtGui

logger = logging.getLogger(__name__)

class Downloader():
        def __init__(self,parent) -> None:
                self.parent = parent
                self.DownLoader = QtCore.QSettings('Lector', 'Lector')
                pass
        def readWindow(self):
            self.DownLoader.beginGroup('DownloadWindow')
            self.parent.DownLoader['Download_dialog_size'] = self.DownLoader.value(
                'windowSize', QtCore.QSize(1000, 700))
            self.parent.DownLoader['Download_dialog_position'] = self.DownLoader.value(
                'windowPosition', QtCore.QPoint(0, 0))
            self.parent.DownLoader['Download_dialog_headers'] = self.DownLoader.value(
                'tableHeaders', [200, 150])
            self.DownLoader.endGroup()
