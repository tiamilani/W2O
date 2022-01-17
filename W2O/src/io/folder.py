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
# Copyright (C) 2021 Mattia Milani <mattia.milani10@gmail.com>

import os

class folder_handler():

    def __init__(self, path: str):
        self.__path = path
        if not os.path.isdir(path):
            os.mkdir(path)

    @property
    def path(self) -> str:
        return self.__path

    def __str__(self):
        return "{}".format(self.__path)
