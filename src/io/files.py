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
import typing
from datetime import date


class FileHandler:
    """FileHandler.
    Class to manage single files
    """


    def __init__(self, filepath: str, override: bool = False,
                 create_path: bool = True):
        """__init__.

        Parameters
        ----------
        filepath : str
            path to the file to use
        override : bool
            check if is possible to over write the file or the old copy must
            be protected
        create_path : bool
            create the path up to the file flag
        """

        self.__filename: str = filepath.split("/")[-1]
        self.__path: str = os.path.join("/".join(filepath.split("/")[:-1]))
        # Check the path for particular characters
        self.__path: str = self.evaluate_path(self.__path)
        # Check if the path exists
        if not os.path.exists(self.__path):
            if create_path:
                os.makedirs(self.__path)
            else:
                raise FileNotFoundError

        self.__filepath: str = os.path.join(self.__path, self.__filename)

        # Create the file
        if override:
            self.__file = open(self.__filepath, "w")
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

    def write(self, line: str) -> None:
        """write.
        Write a single line to the file, important the carriage return character
        must be handle before passing the string

        Parameters
        ----------
        line : str
            line to write

        Returns
        -------
        None

        """
        self.file.write(line)

    def evaluate_path(self, path: str) -> str:
        """evaluate_path.
        Evalaute a paht for special options, like date

        Parameters
        ----------
        path : str
            path

        Returns
        -------
        str the path with the text instead of the special options

        """
        return path.format(date=date.today())

    def get(self, appendix: str) -> str:
        """get.
        Permits to get a file path with the same file name as the handled one
        plus an appendix, remember the type of the file, the part after the '.'
        will be removed, also the '.' will be removed

        Parameters
        ----------
        appendix : str
            string to use instead of the default desinence of the file

        Returns
        -------
        str the filepath modified

        """
        pth = self.__filepath.split(".")[0]
        pth += appendix
        return pth
