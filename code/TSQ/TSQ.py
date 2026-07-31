import math
import sys
from mutants.Original import *


def MR1(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = b
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR2(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR3(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = b
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR4(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = math.sqrt(3 * pow(b, 2) + 6 * pow(c, 2) - 2 * pow(a, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR5(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    zs, symbol = Trisquare().trisquare(argv)
    s, symbol = dynamic.trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
    b1 = b
    c1 = math.sqrt(6 * pow(b, 2) + 3 * pow(c, 2) - 2 * pow(a, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR6(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(c, 2) - 2 * pow(b, 2))
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = c
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR7(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(b, 2) - 2 * pow(c, 2))
    b1 = b
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR8(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
    c1 = math.sqrt(6 * pow(a, 2) + 3 * pow(c, 2) - 2 * pow(b, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MR9(argv, dynamic):
    a = argv[0]
    b = argv[1]
    c = argv[2]
    s, symbol = dynamic.trisquare(argv)
    zs, symbol = Trisquare().trisquare(argv)
    if zs == 0:
        return 2
    a1 = a
    b1 = math.sqrt(6 * pow(a, 2) + 3 * pow(b, 2) - 2 * pow(c, 2))
    c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
    edge = [a1, b1, c1]
    s1, symbol = dynamic.trisquare(edge)
    s = float('%.4f' % s)
    s1 = float('%.4f' % s1)
    if abs(s1 - s) < 1e-4:
        return 0, edge
    else:
        return 1, edge


def MTG(argv, dynamic):
    source = argv.copy()
    follow_case = []
    MG = []
    current_module = sys.modules[__name__]
    for i in range(1, 10):  # MR
        result, follow = getattr(current_module, 'MR' + str(i))(source, dynamic)
        MG.append(result)
        follow_case.append(follow)
    return MG, follow_case
