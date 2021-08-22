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


from typing import Dict
from .strings import s
from ..io.folder import folder_handler as fh


def check_value(value: float):
    pass


def check_file(value: str):
    pass


def check_folder(value: str):
    return fh(value)


def check_operation(value: str):
    pass


def check_conf(conf: Dict):
    for elem in conf:
        if elem not in s.conf_elements:
            raise ValueError("{} is not a valid element".format(elem))
        if conf[elem][s.typ] not in s.types:
            raise ValueError("{} is not a valid type".format(conf[elem][s.typ]))

        if conf[elem][s.typ] == s.vl_typ:
            check_value(conf[elem][s.vl])
        if conf[elem][s.typ] == s.fl_typ:
            check_file(conf[elem][s.vl])
        if conf[elem][s.typ] == s.dr_typ:
            conf[elem][s.vl] = check_folder(conf[elem][s.vl])
        if conf[elem][s.typ] == s.op_typ:
            check_operation(conf[elem][s.vl])
