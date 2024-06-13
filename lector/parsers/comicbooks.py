# This file is a part of Lector, a Qt based ebook reader
# Copyright (C) 2017-19 BasioMeusPuga

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
# Account for files with passwords

import os
import time
import logging
import zipfile
import collections

from lector.rarfile import rarfile

logger = logging.getLogger(__name__)


class ParseCOMIC:
    def __init__(self, filename, *args):
        self.filename = filename
        self.book = None
        self.image_list = None
        self.book_extension = os.path.splitext(self.filename)

    def read_book(self):
        if self.book_extension[1] == '.cbz':
            self.book = zipfile.ZipFile(
                self.filename, mode='r', allowZip64=True)
            self.image_list = [
                i.filename for i in self.book.infolist()
                if not i.is_dir() and is_image(i.filename)]

        elif self.book_extension[1] == '.cbr':
            self.book = rarfile.RarFile(self.filename)
            self.image_list = [
                i.filename for i in self.book.infolist()
                if not i.isdir() and is_image(i.filename)]

        self.image_list.sort()

    def generate_metadata(self):
        title = os.path.basename(self.book_extension[0]).strip(' ')
        author = '<Unknown>'
        isbn = None
        tags = []
        cover = self.book.read(self.image_list[0])

        creation_time = time.ctime(os.path.getctime(self.filename))
        year = creation_time.split()[-1]

        Metadata = collections.namedtuple(
            'Metadata', ['title', 'author', 'year', 'isbn', 'tags', 'cover'])
        return Metadata(title, author, year, isbn, tags, cover)

    def generate_content(self):
        image_number = len(self.image_list)
        toc = [(1, f'Page {i + 1}', i + 1) for i in range(image_number)]

        # Return toc, content, images_only
        return toc, self.image_list, True

def is_image(filename):
    valid_image_extensions = ['.png', '.jpg', '.bmp',".webp"]
    if os.path.splitext(filename)[1].lower() in valid_image_extensions:
        return True
    else:
        return False
