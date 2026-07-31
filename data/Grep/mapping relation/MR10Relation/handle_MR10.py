#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/11
# @Anthor   : phantomDai
"""
进一步处理与MR10有关的测试用例：（１）去掉正常字符后面带有{}或者＋的测试用例；（２）处理正常字符在[]中的测试用例
"""
import sys

sys.path.append('../..')
from myutl.Utl import Utl
import os

parent_path = os.path.join(os.path.abspath('../..'), 'mapping relation')

target_normal_literals_path = os.path.join(parent_path, 'MR10Relation', 'normal_literals_4_MR10_lines')

normal_literals_path = os.path.join(parent_path, 'normal_literals')

MR10_path = os.path.join(parent_path, 'MR10Relation', 'MR10_1')

new_MR10_path = os.path.join(parent_path, 'MR10Relation', 'MR10')

# 实例化工具类的对象
tool = Utl()


def handle_1():
    new_test_cases = []
    test_case_file = tool.get_file_object(MR10_path)
    for aline in test_case_file:
        pattern = aline.strip().split(':', 1)[1]
        index = aline.strip().split(':', 1)[0]

        normal_literal = tool.get_line_content(normal_literals_path, int(index))

        if normal_literal + "{" in pattern or normal_literal + "+" in pattern:
            pass
        else:
            new_test_cases.append(index + ":" + pattern + '\n')

    tool.write_test_cases(MR10_path, new_test_cases)


def handle_2():
    new_test_cases = []
    test_case_file = tool.get_file_object(MR10_path)
    for aline in test_case_file:
        pattern = aline.strip().split(':', 1)[1]
        index = aline.strip().split(':', 1)[0]

        normal_literal = tool.get_line_content(normal_literals_path, int(index))

        # 获得正常字符串的起始位置
        started_position = pattern.find(normal_literal)
        ended_position = started_position + len(normal_literal)

        flag_start = False
        flag_end = False

        # 分别向前后辐射
        for i in range(started_position, -1, -1):
            if pattern[i] == '[':
                flag_start = True
                break

        for i in range(ended_position, len(pattern)):
            if pattern[i] == ']':
                flag_end = True
                break

        if flag_start and flag_end:
            pass
        else:
            new_test_cases.append(index + ":" + pattern + '\n')

    tool.write_test_cases(new_MR10_path, new_test_cases)


handle_1()
handle_2()
