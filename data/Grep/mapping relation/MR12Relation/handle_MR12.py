#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/11
# @Anthor   : phantomDai
"""
进一步处理ＭＲ12：（去掉处于[]内的测试用例）;(2)去掉包含\?这样的测试用例
"""
import sys
sys.path.append('../..')
from myutl.Utl import Utl
import os


parent_path = os.path.join(os.path.abspath('../..'), 'mapping relation')

normal_literals_path = os.path.join(parent_path, 'normal_literals')

MR12_path = os.path.join(parent_path, 'MR12Relation', 'MR12_1')

new_MR12_path = os.path.join(parent_path, 'MR12Relation', 'MR12')

# 实例化工具类的对象
tool = Utl()

test_case_file = tool.get_file_object(MR12_path)


def handle_1():

    new_test_cases = []

    for aline in test_case_file:
        pattern = aline.strip().split(':', 1)[1]
        index = aline.strip().split(':', 1)[0]

        normal_literal = tool.get_line_content(normal_literals_path, int(index))

        if '-' in normal_literal:
            continue
        elif '[' + normal_literal + ']' in pattern or '[^' + normal_literal + ']' in pattern:
            continue
        elif r'\\\\' in pattern:
            continue
        elif len(normal_literal) == 2 and '\\' in normal_literal:
            continue
        else:
            new_test_cases.append(aline)

    tool.write_test_cases(new_MR12_path, new_test_cases)


def handle_2():

    new_test_case = []

    for aline in test_case_file:
        pattern = aline.strip().split(':', 1)[1]
        index = aline.strip().split(':', 1)[0]

        normal_literal = tool.get_line_content(normal_literals_path, int(index))

        if r'\\\\' in pattern:
            pass
        elif len(normal_literal) == 2 and '\\' in normal_literal:
            pass
        else:
            new_test_case.append(aline)

    tool.write_test_cases(new_MR12_path, new_test_case)


handle_1()

# handle_2()

