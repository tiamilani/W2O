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
import re
import sys
import yaml
import errno
import argparse
import datetime
import pandas as pd
import pandas.io.formats.excel

from src.util.strings import s
from src.util.checks import check_conf as cc
from src.io.file import FileHandler as fh

parser = argparse.ArgumentParser(usage="usage: main.py [options]",
                                 description=s.script_description,
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# TODO make all this strings in the strings file
parser.add_argument("-f", "--file", dest="yamlfile", default="config/basic.yaml",
                    action="store", help="define the yaml input file")
parser.add_argument("-x", "--students", dest="students", default="ListaStudentiEsameExport.xls",
                    action="store", help="defines the name of the xls file that represent the list of the students from ESSE3.unitn.it")
parser.add_argument("-g", "--grades", dest="grades", default="grades.csv",
                    action="store", help="grades csv from moodle")
parser.add_argument("-t", "--time", dest="time", default="time.csv", action="store",
                    help="csv file that defines the time slots for the oral exam")
parser.add_argument("-o", "--output", dest="output", default="schedule.xls",
                    action="store", help="output file name")
parser.add_argument("-s", "--separetor", dest="separetor", default=".",
                    action="store", help="Separetor used in the excel output files for decimal number")
parser.add_argument("-r", "--round", dest="round", default=True,
                    action="store_false", help="Create a second file with the rounded marks to the nearest integer")


def main():
    # Parse the arguments
    options = parser.parse_args()

    # Load the data from the yaml file
    with open(options.yamlfile) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # Check the configuration
    cc(data)

    # Check the arguments
    fh_students = fh(options.students, override=False, already_exists=True)
    fh_grades = fh(options.grades, override=False, already_exists=True)
    fh_time_table = fh(options.time, override=False, already_exists=True)
    fh_output = fh(options.output, override=False, already_exists=False)

    students = pd.read_excel(fh_students.path, skiprows=data[s.skyp_row][s.vl],
                             index_col=s.students_idx)

    for elem in s.OPT_C:
        if elem not in list(students.columns):
            s.STUDENTS_COLUMNS.remove(elem)
            s.STUDENTS_COLUMNS_ROUND.remove(elem)

    preamble = pd.read_excel(fh_students.path, nrows=data[s.skyp_row][s.vl]-1)
    grades = pd.read_csv(fh_grades.path)
    grades = grades.drop(grades.index[-1])
    grades = grades.drop(s.grades_drops, axis=1)
    grades[[s.students_idx]] = grades[[s.students_idx]].astype(int)

    number_of_passed = 0
    for matricola, grade in zip(grades["Matricola"].values, grades["Valutazione/11,00"].values):
        grade_separetor = re.sub(r'[0-9]*', '', grade)
        correct_grade = float(grade.replace(grade_separetor, '.') if grade_separetor in grade else grade)
        if matricola not in students.index:
            print("ERROR, {} not in the students registered for the exam in {}".format(
                    matricola, options.students))
        if correct_grade >= data[s.s_threshold][s.vl]:
            students.loc[matricola, "Esito"] = str(grade).replace(grade_separetor, options.separetor)
            students.loc[matricola, "Esito_round"] = round(correct_grade/11*30)
            number_of_passed += 1
        else:
            students.loc[matricola, "Esito"] = "0"
            students.loc[matricola, "Esito_round"] = "0"

    assenti = set(students.index.values) - set(grades["Matricola"].values)
    for ass in assenti:
        students.loc[ass, "Esito"] = "ASS"
        students.loc[ass, "Esito_round"] = "ASS"

    students = students.reset_index()
    students = students.set_index('#')
    students_round = students[s.STUDENTS_COLUMNS_ROUND]
    students = students[s.STUDENTS_COLUMNS]
    students_round.rename(columns={'Esito_round': 'Esito'}, inplace=True)

    students.index = students.index.map(str)
    students = students.astype({'Matricola': str, 'Unnamed: 6': str})
    preamble = preamble.fillna('')
    preamble = preamble.astype(str)

    students.rename(columns={'Unnamed: 6': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 5': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 6': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 7': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 8': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 9': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 10': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 11': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 12': ''}, inplace=True)
    preamble.rename(columns={'Unnamed: 13': ''}, inplace=True)

    writer = pd.ExcelWriter(data[s.output_folder][s.vl].path + "/" + fh_students.fileName)
    pandas.io.formats.excel.ExcelFormatter.header_style = None
    preamble.to_excel(writer, sheet_name='esse3', index=False)
    students.to_excel(writer, startrow=data[s.skyp_row][s.vl], sheet_name='esse3')
    writer.save()

    if options.round:
        file_name = fh_students.fileName.split('.')[0] + "_rounded.xls"
        writer = pd.ExcelWriter(data[s.output_folder][s.vl].path + "/" + file_name)
        pandas.io.formats.excel.ExcelFormatter.header_style = None
        preamble.to_excel(writer, sheet_name='esse3', index=False)
        students_round.to_excel(writer, startrow=data[s.skyp_row][s.vl], sheet_name='esse3')
        writer.save()

    pass_students = students[(students["Esito"] != "ASS") & (students["Esito"] != "0") &
                             (students["Esito"] != "RIT")][["Matricola", "Cognome", "Nome"]]

    slots = []
    time_slots = pd.read_csv(options.time)
    for day, start, end in zip(time_slots["day"].values, time_slots["start"].values,
                          time_slots["end"].values):
        start = datetime.datetime.strptime(day + " " + start, "%d/%m/%Y %H:%M")
        end = datetime.datetime.strptime(day + " " + end, "%d/%m/%Y %H:%M")
        delta = datetime.timedelta(minutes=data[s.student_time][s.vl])
        while start < end:
            end_tmp = start + delta
            slots.append(start)
            start += delta

    if len(pass_students.index) > len(slots):
        print("ERROR, NOT ENOUGH TIME SLOTS")
        sys.exit(2)

    if len(pass_students.index) != number_of_passed:
        print("ERROR, That's strange, len(pass_students) != number of passed students")

    pass_students = pass_students.sample(frac=1)
    pass_students["Orale"] = slots[:len(pass_students.index)]
    writer = pd.ExcelWriter(fh_output.path)
    pass_students.to_excel(writer, sheet_name="Schedule")
    writer.save()

if __name__ == "__main__":
    main()
