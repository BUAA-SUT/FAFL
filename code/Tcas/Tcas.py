import sys
from mutants.Mutants import *


def MR1(argv, dynamic):
    # MR12
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR2(argv, dynamic):
    # MR13
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR3(argv, dynamic):
    # MR14
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] >= 3:
            return result, argv_f
        else:
            argv_f[6] = argv[6] + 1
    elif o_s == 'DOWNWARD_RA':
        if argv[6] <= 0:
            return result, argv_f
        else:
            argv_f[6] = argv[6] - 1
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] <= 0:
                return result, argv_f
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] >= 3:
                return result, argv_f
            else:
                argv_f[6] = argv[6] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_f)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_f


def MR4(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
        argv_ff = argv_f.copy()
        argv_ff[8] = argv_f[8] - 10
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] + 10  # y8>x8
        if argv_f[11] == 1:
            argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
        else:
            argv_ff[8] = argv_ff[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] - 10  # y8<x8
        argv_ff[8] = argv_f[8] + 10  # y9>x9
        if argv_f[11] == 1:
            if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
            elif argv_f[7] == (argv_f[8] - 100):
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 110
        else:
            if argv_f[7] > argv_f[8]:
                argv_ff[7] = argv_ff[8] + 1
            elif argv_f[7] == argv_f[8]:  # 无解
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 1

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    z_r_s = TCAS().Tcas(argv)
    z_r_f = TCAS().Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR5(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
        argv_ff = argv_f.copy()
        if argv_f[6] >= 3:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
        argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
        argv_ff = argv_f.copy()
        if argv_f[6] <= 0:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] - 1
    elif o_s == 'UNRESOLVED':
        argv_f[3] = ((argv[3] + argv[5]) / 2)
        argv_f[5] = ((argv[3] + argv[5]) / 2)
        argv_ff = argv_f.copy()
        if argv_f[3] <= argv_f[5]:
            if argv_f[6] <= 0:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        else:
            if argv_f[6] >= 3:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR6(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_ff
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_ff
            else:
                argv_f[8] = argv_f[7] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR7(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] >= 3:
            return result, argv_f
        else:
            argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
    elif o_s == 'DOWNWARD_RA':
        if argv[6] <= 0:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] - 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] <= 0:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] >= 3:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
        argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR8(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        argv_f[8] = argv[8] - 10
        argv_ff = argv_f.copy()
        if argv_f[6] >= 3:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] + 1
    elif o_s == 'DOWNWARD_RA':
        argv_f[7] = argv[7] + 10  # y8>x8
        if argv[11] == 1:
            argv_f[8] = argv_f[7] + 110  # y8+100<=y9
        else:
            argv_f[8] = argv_f[7] + 10  # y8<=y9
        argv_ff = argv_f.copy()
        if argv_f[6] <= 0:
            return result, argv_ff
        else:
            argv_ff[6] = argv_f[6] - 1
    elif o_s == 'UNRESOLVED':
        argv_f[7] = argv[7] - 10  # y8<x8
        argv_f[8] = argv[8] + 10  # y9>x9
        if argv[11] == 1:
            if argv[7] > (argv[8] - 100):  # x8>x9-100
                argv_f[8] = argv_f[7] + 90  # y8>y9-100
            elif argv[7] == (argv[8] - 100):
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 110
        else:
            if argv[7] > argv[8]:
                argv_f[7] = argv_f[8] + 1
            elif argv[7] == argv[8]:  # 无解
                return result, argv_f
            else:
                argv_f[8] = argv_f[7] + 1
        argv_ff = argv_f.copy()
        if argv_f[3] <= argv_f[5]:
            if argv_f[6] <= 0:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        else:
            if argv_f[6] >= 3:
                return result, argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1

    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


def MR9(argv, dynamic):
    o_s = TCAS().Tcas(argv)
    argv_f = argv.copy()
    argv_ff = argv_f.copy()
    result = 2
    if o_s == 'UPWARD_RA':
        if argv[6] >= 3:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[8] = argv_f[8] - 10
    elif o_s == 'DOWNWARD_RA':
        if argv[6] <= 0:
            return result, argv_ff
        else:
            argv_f[6] = argv[6] - 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] + 10  # y8>x8
        if argv_f[11] == 1:
            argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
        else:
            argv_ff[8] = argv_ff[7] + 10  # y8<=y9
    elif o_s == 'UNRESOLVED':
        if argv[3] <= argv[5]:
            if argv[6] <= 0:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] - 1
        else:
            if argv[6] >= 3:
                return result, argv_ff
            else:
                argv_f[6] = argv[6] + 1
        argv_ff = argv_f.copy()
        argv_ff[7] = argv_f[7] - 10  # y8<x8
        argv_ff[8] = argv_f[8] + 10  # y9>x9
        if argv_f[11] == 1:
            if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
            elif argv_f[7] == (argv_f[8] - 100):
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 110
        else:
            if argv_f[7] > argv_f[8]:
                argv_ff[7] = argv_ff[8] + 1
            elif argv_f[7] == argv_f[8]:  # 无解
                return result, argv_ff
            else:
                argv_ff[8] = argv_ff[7] + 1
    r_s = dynamic.Tcas(argv)
    r_f = dynamic.Tcas(argv_ff)
    if r_f == r_s:
        result = 0
    else:
        result = 1
    return result, argv_ff


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
