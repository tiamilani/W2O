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
strings module
==============

Module used to control in one place all the strings of the program

"""


class s:

    dist = "distributions"
    dist_name = "name"
    dist_type = "type"
    dist_seed = "seed"
    dist_mean = "mean"
    dist_variance = "variance"
    dist_lmbd = "lambda"
    dist_start = "start"
    dist_end = "end"
    normal_dists = ["normal", "gaussian"]
    expo_dists = ["exponential"]
    uniform_dists = ["uniform"]

    dataset = "datasets"
    dat_name = "name"
    dat_n = "n"
    dat_file = "file"
    clm = "columns"
    clm_name = "name"
    clm_dist = "distribution"
    overwrite = "overwrite"
