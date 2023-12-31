# -*- coding: utf-8 -*-
import filecmp
import shutil
import random
import os


def comparing(path):
    """This function compares files into a given directory.

    Parameters
    ----------
    path : str
        Directory path.
    Returns
    -------

    """
    file_list = os.listdir(path)
    for file_1 in file_list:
        for file_2 in list(set(os.listdir(path)) - {file_1}):
            if filecmp.cmp(
                os.path.join(path, file_1),
                os.path.join(path, file_2)
            ):
                print('{} == {}: {}'.format(file_1, file_2, True))

        file_list.pop(file_list.index(file_1))


def moving(path, new_path, range_):
    for i in range(range_):
        shutil.move(
            os.path.join(path, random.choice(os.listdir(path))), new_path
        )
