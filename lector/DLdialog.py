# This file is a part of Lector, a Qt based ebook reader
# Copyright (C) 2017-2019 BasioMeusPuga

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# TODO
# Get Cancel working with the file system model

import os
import copy
import logging
import pathlib

from PyQt5 import QtWidgets, QtCore, QtGui

from lector import database
from lector.annotations import AnnotationsUI
from lector.models import MostExcellentFileSystemModel
from lector.threaded import BackGroundBookSearch, BackGroundBookAddition
from lector.resources import downloadwindow
from lector.settings import Settings
from lector.logger import logger_filename, VERSION

logger = logging.getLogger(__name__)


class DownloadUI(QtWidgets.QDialog, downloadwindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(DownloadUI, self).__init__()
        self.setupUi(self)
        # self.verticalLayout_4.setContentsMargins(1000, 0, 0, 0)
        self._translate = QtCore.QCoreApplication.translate

        self.main_window = parent
        self.image_factory = self.main_window.QImageFactory

        # The annotation dialog will use the settings dialog as its parent
        # self.annotationsDialog = AnnotationsUI(self)

        self.resize(self.main_window.DownLoader['Download_dialog_size'])
        self.move(self.main_window.DownLoader['Download_dialog_position'])
