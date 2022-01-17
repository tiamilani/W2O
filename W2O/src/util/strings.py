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


    # Argparse
    script_description = "Use this script in order to automatically generate " +\
                         "the oral part of an exam, starting from the list of "+\
                         "students registered to the written part, with the "  +\
                         "grades and a time schedule"

    # main
    vl = "value"
    typ = "type"
    # Configuration
    s_threshold = "sufficiency_threshold"
    skyp_row = "skyp_row"
    output_folder = "output_folder"
    gc_factor = "grade_correction_factor"
    student_time = "minutes_per_student"
    conf_elements = [s_threshold, skyp_row, output_folder, gc_factor,
                     student_time]
    # Values
    vl_typ = "value"
    fl_typ = "file"
    dr_typ = "folder"
    op_typ = "operation"
    types = [vl_typ, fl_typ, dr_typ, op_typ]

    # Pandas
    students_idx = "Matricola"
    grades_drops = ['Cognome', 'Nome', 'Indirizzo email', 'Dipartimento',
                    'Stato', 'Iniziato', 'Completato', 'Tempo impiegato']

    # Constants
    STUDENTS_COLUMNS = ['Data Iscrizione', 'Matricola', 'Cognome', 'Nome', 'Data Nascita', 'Unnamed: 6', 'Esito', 'Domande d\'esame', 'Data superamento', 'Nota per lo studente', 'Presa Visione', 'Misure Compensative', 'Email']
    STUDENTS_COLUMNS_ROUND = ['Data Iscrizione', 'Matricola', 'Cognome', 'Nome', 'Data Nascita', 'Unnamed: 6', 'Esito_round', 'Domande d\'esame', 'Data superamento', 'Nota per lo studente', 'Presa Visione', 'Misure Compensative', 'Email']

    # Optional columns
    OPT_C = ['Misure Compensative']

