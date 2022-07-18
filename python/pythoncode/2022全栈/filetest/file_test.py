# coding:utf-8
import os
from shutil import copy,copyfile,copytree

path = os.path.join(os.getcwd(), 'test1.txt')
target = os.path.join(os.getcwd(), 'test1')


copy(path, target)
copyfile(path, target)
copytree('test3', 'test4') # 目标地址不能存在，否则会报错
# move 当目标路径不存在，并且和来源目录属于相同路径下，属于重命名
