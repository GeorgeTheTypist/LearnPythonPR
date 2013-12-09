__author__ = 'Pneumatic'
# To create a module either right click on current project (left display bar) and select python package  or click file
# - new - python package. Then create any new .py files you need
import math  # This is a module. It consists of python code you can bind and reference
from Modules import importModules, support  # from package Modules import file importModules and support
contents = dir(math)  # this returns a sorted list of strings containing the names defined by a module.
# print(contents)  prints contents of dir(math)
importModules.mod()  # called the function mod from the module importModules
support.func_name("Thomas")  # call func_name from file support using arguments("thomas")
