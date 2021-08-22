# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2020 Mattia Milani <mattia.milani.ext@nokia.com>

"""
files module
============

Use this module to handle files

"""

import os
import errno
import typing
from datetime import date


class FileHandler:
    """FileHandler.
    Class to manage single files
    """


    def __init__(self, filepath: str, override: bool = False,
                 already_exists: bool = False):
        """__init__.

        Parameters
        ----------
        filepath : str
            path to the file to use
        override : bool
            check if is possible to over write the file or the old copy must
            be protected
        """

        self.__filepath: str = filepath
        self.__filename: str = filepath.split("/")[-1]
        self.__path: str = os.path.join("/".join(filepath.split("/")[:-1]))
        self.__file = None

        if already_exists:
            if not os.path.isfile(self.__filepath):
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                        self.__filepath)

        # Create the file
        if override:
            self.__file = open(self.__filepath, "w")
        else:
            if already_exists:
                self.__file = open(self.__filepath, "r")
            else:
                self.__file = open(self.__filepath, "x")

    def __del__(self) -> None:
        """__del__.
        Close the file

        Parameters
        ----------

        Returns
        -------
        None

        """
        if self.file is not None:
            self.file.close()

    def __str__(self) -> None:
        """__str__.
        print information about the file handler

        Parameters
        ----------

        Returns
        -------
        None

        """
        return "File handler: {}".format(self.__filepath)

    @property
    def file(self) -> typing.TextIO:
        """file.

        Parameters
        ----------

        Returns
        -------
        typing.TextIO the file stream

        """
        return self.__file

    @property
    def fileName(self) -> str:
        return self.__filename

    @property
    def path(self) -> str:
        """path.

        Parameters
        ----------

        Returns
        -------
        str the compleate file path to the destination file

        """
        return self.__filepath

    @property
    def folderPath(self) -> str:
        """folderPath.

        Parameters
        ----------

        Returns
        -------
        str the path to the file, without the file, only the folders

        """
        return self.__path

