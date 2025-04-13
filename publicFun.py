import copy
import random
import numpy as np

# from openpyxl import load_workbook
random.seed(1)

Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
           'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal', 'Rogers&Tanimoto',
           'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2', 'Wong3',
           'Arithmetic Mean', 'Cohen', 'Fleiss']

def riskformula(index, t):  # 多个公式
    ev = index[0]
    es = index[1]
    nv = index[2]
    ns = index[3]
    ev_only = nv
    F = ev + nv
    P = es + ns
    if t == 0:
        if ev < F:
            formula = -1
        elif ev == F and F != 0:
            formula = ns
        else:
            formula = -1
    elif t == 1:
        formula = ev - es / (es + ns + 1)
    elif t == 2:
        formula = ev
    elif t == 3:
        formula = ev / (ev + es + nv + ns)
    elif t == 4:
        if ev < F:
            formula = 0
        elif ev == F and F != 0:
            formula = 1
        else:
            formula = 0
    elif t == 5:
        formula = ev / (ev + es + nv)
    elif t == 6:
        formula = ev / (ev + 2 * (nv + es))
    elif t == 7:
        formula = 2 * ev / (2 * ev + nv + es)
    elif t == 8:
        formula = 2 * ev / (ev + nv + es)
    elif t == 9:
        formula = (2 * ev - nv - es) / (2 * ev + nv + es)
    elif t == 10:
        formula = (ev / (ev + nv)) / (ev / (ev + nv) + es / (es + ns))
    elif t == 11:
        formula = ev / (ev + es)
    elif t == 12:
        formula = (ev / (ev + es)) - ((ev + nv) / (ev + nv + es + ns))
    elif t == 13:
        formula = ev - es
    elif t == 14:
        formula = (ev + ns - nv - es) / (ev + nv + es + ns)
    elif t == 15:
        formula = (ev + ns) / (ev + nv + es + ns)
    elif t == 16:
        formula = 2 * (ev + ns) / (2 * (ev + ns) + nv + es)
    elif t == 17:
        formula = (ev + ns) / (ev + ns + 2 * (nv + es))
    elif t == 18:
        formula = ev + ns
    elif t == 19:
        formula = np.sqrt(ev + ns)
    elif t == 20:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / ((2 * ev + nv + es) * (2 * ns + nv + es))
    elif t == 21:
        formula = 0.5 * (ev / (2 * ev + nv + es) + ns / (2 * ns + nv + es))
    elif t == 22:
        formula = 0.5 * (ev / (ev + nv) + ev / (ev + es))
    elif t == 23:
        formula = ev / ((ev + nv) * (ev + es)) ** 0.5
    elif t == 24:
        formula = ev / (ev + ns + 2 * (nv + es))
    elif t == 25:
        formula = ev / (ev + nv) - es / (es + ns)
    elif t == 26:
        if es <= 2:
            formula = ev - es
        elif 2 < es <= 10:
            formula = ev - 2 - 0.1 * (es - 2)
        else:
            formula = ev - 2.8 - 0.001 * (es - 10)
    elif t == 27:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + nv) + (ev + nv) * (es + ns))
    elif t == 28:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + es) + (ev + nv) * (nv + ns))
    else:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / (2 * ev + nv + es + 2 * ns + nv + es)

    return formula


def riskformula2(index, t, v, s):  # 多个公式
    ev = index[0]
    es = index[1]
    nv = index[2]
    ns = index[3]
    F = v
    if t == 0:
        if ev < F:
            formula = -1
        elif ev == F and F != 0:
            formula = ns
        else:
            formula = -1
    elif t == 1:
        formula = ev - es / (es + ns + 1)
    elif t == 2:
        formula = ev
    elif t == 3:
        formula = ev / (ev + es + nv + ns)
    elif t == 4:
        if ev < F:
            formula = 0
        elif ev == F and F != 0:
            formula = 1
        else:
            formula = 0
    elif t == 5:
        formula = ev / (ev + es + nv)
    elif t == 6:
        formula = ev / (ev + 2 * (nv + es))
    elif t == 7:
        formula = 2 * ev / (2 * ev + nv + es)
    elif t == 8:
        formula = 2 * ev / (ev + nv + es)
    elif t == 9:
        formula = (2 * ev - nv - es) / (2 * ev + nv + es)
    elif t == 10:
        formula = (ev / (ev + nv)) / (ev / (ev + nv) + es / (es + ns))
    elif t == 11:
        formula = ev / (ev + es)
    elif t == 12:
        formula = (ev / (ev + es)) - ((ev + nv) / (ev + nv + es + ns))
    elif t == 13:
        formula = ev - es
    elif t == 14:
        formula = (ev + ns - nv - es) / (ev + nv + es + ns)
    elif t == 15:
        formula = (ev + ns) / (ev + nv + es + ns)
    elif t == 16:
        formula = 2 * (ev + ns) / (2 * (ev + ns) + nv + es)
    elif t == 17:
        formula = (ev + ns) / (ev + ns + 2 * (nv + es))
    elif t == 18:
        formula = ev + ns
    elif t == 19:
        formula = np.sqrt(ev + ns)
    elif t == 20:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / ((2 * ev + nv + es) * (2 * ns + nv + es))
    elif t == 21:
        formula = 0.5 * (ev / (2 * ev + nv + es) + ns / (2 * ns + nv + es))
    elif t == 22:
        formula = 0.5 * (ev / (ev + nv) + ev / (ev + es))
    elif t == 23:
        formula = ev / ((ev + nv) * (ev + es)) ** 0.5
    elif t == 24:
        formula = ev / (ev + ns + 2 * (nv + es))
    elif t == 25:
        formula = ev / (ev + nv) - es / (es + ns)
    elif t == 26:
        if es <= 2:
            formula = ev - es
        elif 2 < es <= 10:
            formula = ev - 2 - 0.1 * (es - 2)
        else:
            formula = ev - 2.8 - 0.001 * (es - 10)
    elif t == 27:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + nv) + (ev + nv) * (es + ns))
    elif t == 28:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + es) + (ev + nv) * (nv + ns))
    else:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / (2 * ev + nv + es + 2 * ns + nv + es)

    return formula


def getSus(index, t):
    formula = 0
    try:
        formula = riskformula(index, t)
    except:
        if index[0] + index[1] == 0:  # e = 0
            formula = -1000
        elif index[0] + index[2] == 0:  # v = 0
            formula = -1000
        elif index[1] + index[3] == 0:  # s = 0
            formula = 1000
    return formula


def getSus2(index, t, v, s):
    formula = 0
    try:
        formula = riskformula2(index, t, v, s)
    except:
        if index[0] + index[1] == 0:  # e = 0
            formula = -1000
        elif index[0] + index[2] == 0:  # v = 0
            formula = -1000
        elif index[1] + index[3] == 0:  # s = 0
            formula = 1000
    return formula


def Sus(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    Sus = []
    staDe = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):  # 为了和FaSus保持一致
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                exe.sort()
                if MG[i][j][k] == 1:
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                elif MG[i][j][k] == 0:  #  or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
                staDe.append(round((len(exe)-len(union))/len(exe)*100, 2))
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric, staDe


def FaSus(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j], Exelines[i][j * len(MG[0][0]) + k + 1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j * len(MG[0][0]) + k + 1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1
                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j] and fault in Exelines[i][j * len(MG[0][0]) + k + 1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]

    Sus = []
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)

    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def FaflSus(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j], Exelines[i][j * len(MG[0][0]) + k + 1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j * len(MG[0][0]) + k + 1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1
                            Metric2[index][0] += 1

                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j] and fault in Exelines[i][j * len(MG[0][0]) + k + 1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][1] += 0.5
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - Metric2[i][0]
        metric[i][3] = s - Metric2[i][1]
    Sus = []
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def FaflVariantSus_test(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    Metric = []
    for _ in range(11):
        me = []
        for _ in range(11):
            metric = []
            for i in range(len(Executable)):
                metric.append([0, 0, 0, 0])  # ev es nv ns
            me.append(metric)
        Metric.append(me)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j], Exelines[i][j * len(MG[0][0]) + k + 1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j * len(MG[0][0]) + k + 1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    Metric[x][y][index][0] += 1
                            Metric2[index][0] += 1
                        for d in exe1:
                            # print("exe1")
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    Metric[x][y][index][0] += (1 - x * 0.1)
                            # Metric2[index][0] += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    # Metric[x][y][index][1] += (0.1 - (y+1) * 0.02)
                                    Metric[x][y][index][1] += (1 - y * 0.1)
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1])) #不会执行
    for k in range(11):
        for l in range(11):
            for i in range(len(Metric[k][l])):
                Metric[k][l][i][2] = v - Metric2[i][0]
                Metric[k][l][i][3] = s - Metric2[i][1]
    SUS = []
    for k in range(11):
        S = []
        for l in range(11):
            Sus = []
            for t in range(len(Formula)): # range(len(Formula))
                sus = []
                for i in range(len(Metric[k][l])):
                    sus.append(round(getSus2(Metric[k][l][i], t, v, s), 4))
                Sus.append(sus)
            S.append(Sus)
        SUS.append(S)
    return SUS, Metric


def FaflVariantSus(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    Metric = []
    nn = 11
    for _ in range(nn):
        me = []
        for _ in range(nn):
            metric = []
            for i in range(len(Executable)):
                metric.append([0, 0, 0, 0])  # ev es nv ns
            me.append(metric)
        Metric.append(me)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j], Exelines[i][j * len(MG[0][0]) + k + 1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j * len(MG[0][0]) + k + 1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][0] += 1
                            Metric2[index][0] += 1
                        for d in exe1:
                            # print("exe1")
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][0] += (1 - x * 0.1)
                            Metric2[index][0] += 1

                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][1] += (1 - y * 0.1)
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1])) #不会执行
    for k in range(nn):
        for l in range(nn):
            for i in range(len(Metric[k][l])):
                Metric[k][l][i][2] = v - Metric2[i][0]
                Metric[k][l][i][3] = s - Metric2[i][1]
    SUS = []
    for k in range(nn):
        S = []
        for l in range(nn):
            Sus = []
            for t in range(len(Formula)):
                sus = []
                for i in range(len(Metric[k][l])):
                    sus.append(round(getSus2(Metric[k][l][i], t, v, s), 4))
                Sus.append(sus)
            S.append(Sus)
        SUS.append(S)
    return SUS, Metric


def MmSus(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']

    metric = []
    metric2 = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
        metric2.append([0, 0, 0, 0])
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))

                        for d in exesum:
                            index = Executable.index(d)
                            if d in Exelines[i][j] and d in Exelines[i][j * len(MG[0][0]) + k + 1]:
                                para = 2
                            else:
                                para = 1
                            metric[index][0] += para
                            metric2[index][0] += 1

                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        for d in exe:
                            index = Executable.index(d)
                            if d in Exelines[i][j] and d in Exelines[i][j * len(MG[0][0]) + k + 1]:
                                para = 2
                            else:
                                para = 1
                            metric[index][1] += para
                            metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - metric2[i][0]
        metric[i][3] = s - metric2[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def SBFLSus(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        record1 = 0
        record2 = 0
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        # s += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                        if sus_a > sus_b:
                            record1 += 1
                            exe = Exelines[i][j]

                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j], Exelines[i][j * len(MG[0][0]) + k + 1]]
                            exe = random.choice(Sum)
                            if Exelines[i][j] == exe:
                                record1 += 1
                            else:
                                for d in exe:
                                    index = Executable.index(d)
                                    metric[index][0] += 1
                                continue

                        else:
                            exe = Exelines[i][j * len(MG[0][0]) + k + 1]
                            for d in exe:
                                index = Executable.index(d)
                                metric[index][0] += 1
                            continue
                        if record1 > 1:
                            continue
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1

                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j] and fault in Exelines[i][j * len(MG[0][0]) + k + 1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        for d in Exelines[i][j * len(MG[0][0]) + k + 1]:
                            index = Executable.index(d)
                            metric[index][1] += 1
                        record2 += 1
                        if record2 > 1:
                            continue
                        for d in Exelines[i][j]:
                            index = Executable.index(d)
                            metric[index][1] += 1
                        s += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def SBFL(MG, Result, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j]) == 0 or len(Exelines[i][j * len(MG[0][0]) + k + 1]) == 0:
                    continue
                if Result[i][j]:
                    v += 1
                    for d in Exelines[i][j]:
                        index = Executable.index(d)
                        metric[index][0] += 1
                if not Result[i][j]:
                    s += 1
                    for d in Exelines[i][j]:
                        index = Executable.index(d)
                        metric[index][1] += 1
                if Result[i][j * len(MG[0][0]) + k + 1]:
                    v += 1
                    for d in Exelines[i][j * len(MG[0][0]) + k + 1]:
                        index = Executable.index(d)
                        metric[index][0] += 1
                if not Result[i][j * len(MG[0][0]) + k + 1]:
                    s += 1
                    for d in Exelines[i][j * len(MG[0][0]) + k + 1]:
                        index = Executable.index(d)
                        metric[index][1] += 1
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    return Sus, metric


def Sus_grep(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman',
               'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal', 'Rogers&Tanimoto',
               'Hamming etc.',
               'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2', 'Wong3', 'Arithmetic Mean',
               'Cohen', 'Fleiss']
    metric = []
    Sus = []
    staDe = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                exe.sort()
                if MG[i][j][k] == 1:
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
                staDe.append(round((len(exe) - len(union)) / len(exe) * 100, 2))
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric, staDe


def FaSus_grep(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j][k][0]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j][k][0], Exelines[i][j][k][1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j][k][1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1
                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j][k][0] and fault in Exelines[i][j][k][1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:   # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]

    Sus = []
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def FaflSus_grep(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j][k][0]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j][k][0], Exelines[i][j][k][1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j][k][1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1
                            Metric2[index][0] += 1


                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j][k][0] and fault in Exelines[i][j][k][1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][1] += 0.5
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - Metric2[i][0]
        metric[i][3] = s - Metric2[i][1]
    Sus = []
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def FaflVariantSus_grep(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    Metric = []
    nn = 11
    for _ in range(nn):
        me = []
        for _ in range(nn):
            metric = []
            for i in range(len(Executable)):
                metric.append([0, 0, 0, 0])  # ev es nv ns
            me.append(metric)
        Metric.append(me)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j][k][0]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j][k][0], Exelines[i][j][k][1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j][k][1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][0] += 1
                            Metric2[index][0] += 1
                        for d in exe1:
                            # print("exe1")
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][0] += (1 - x * 0.1)
                            Metric2[index][0] += 1

                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(nn):
                                for y in range(nn):
                                    Metric[x][y][index][1] += (1 - y * 0.1)
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1])) #不会执行
    for k in range(nn):
        for l in range(nn):
            for i in range(len(Metric[k][l])):
                Metric[k][l][i][2] = v - Metric2[i][0]
                Metric[k][l][i][3] = s - Metric2[i][1]
    SUS = []
    for k in range(nn):
        S = []
        for l in range(nn):
            Sus = []
            for t in range(len(Formula)):
                sus = []
                for i in range(len(Metric[k][l])):
                    sus.append(round(getSus2(Metric[k][l][i], t, v, s), 4))
                Sus.append(sus)
            S.append(Sus)
        SUS.append(S)
    return SUS, Metric


def FaflVariantSus_grep_test(MG, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    Metric = []
    for _ in range(11):
        me = []
        for _ in range(11):
            metric = []
            for i in range(len(Executable)):
                metric.append([0, 0, 0, 0])  # ev es nv ns
            me.append(metric)
        Metric.append(me)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        if sus_a > sus_b:
                            exe = Exelines[i][j][k][0]
                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j][k][0], Exelines[i][j][k][1]]
                            exe = random.choice(Sum)
                        else:
                            exe = Exelines[i][j][k][1]
                        exe1 = [x for x in exesum if x not in exe]
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    Metric[x][y][index][0] += 1
                            Metric2[index][0] += 1
                        for d in exe1:
                            # print("exe1")
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    Metric[x][y][index][0] += (1 - x * 0.1)
                            # Metric2[index][0] += 1

                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exe:
                            index = Executable.index(d)
                            for x in range(11):
                                for y in range(11):
                                    # Metric[x][y][index][1] += (0.1 - (y+1) * 0.02)
                                    Metric[x][y][index][1] += (1 - y * 0.1)
                            Metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1])) #不会执行
    for k in range(11):
        for l in range(11):
            for i in range(len(Metric[k][l])):
                Metric[k][l][i][2] = v - Metric2[i][0]
                Metric[k][l][i][3] = s - Metric2[i][1]
    SUS = []
    for k in range(11):
        S = []
        for l in range(11):
            Sus = []
            for t in range(len(Formula)):
                sus = []
                for i in range(len(Metric[k][l])):
                    sus.append(round(getSus2(Metric[k][l][i], t, v, s), 4))
                Sus.append(sus)
            S.append(Sus)
        SUS.append(S)
    return SUS, Metric


def MmSus_grep(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']

    metric = []
    metric2 = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
        metric2.append([0, 0, 0, 0])
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exesum:
                            index = Executable.index(d)
                            if d in Exelines[i][j][k][0] and d in Exelines[i][j][k][1]:
                                para = 2
                            else:
                                para = 1
                            metric[index][0] += para
                            metric2[index][0] += 1

                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        for d in exe:
                            index = Executable.index(d)
                            if d in Exelines[i][j][k][0] and  d in Exelines[i][j][k][1]:
                                para = 2
                            else:
                                para = 1
                            metric[index][1] += para
                            metric2[index][1] += 1
                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - metric2[i][0]
        metric[i][3] = s - metric2[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def SBFLSus_grep(MG, Executable, Exelines, flag):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    wrong = 0
    ot = 0
    of = 0
    al = 0
    fault = Executable[flag.index(1)]
    for i in range(len(MG)):
        record1 = 0
        record2 = 0
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        # s += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_v = MG[i][j].count(1)
                        sum_s += MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        sum_v += MG[i][k+1].count(1)
                        # 求每个测试用例的ev es nv ns
                        ev_a = MG[i][j].count(1)
                        es_a = MG[i][j].count(0)# + MG[i][j].count(3)
                        nv_a = sum_v - ev_a
                        ns_a = sum_s - es_a
                        index_a = [ev_a, es_a, nv_a, ns_a]
                        ev_b = MG[i][k+1].count(1) + 1
                        es_b = MG[i][k+1].count(0)# + MG[i][k+1].count(3)
                        nv_b = sum_v - ev_b
                        ns_b = sum_s - es_b
                        index_b = [ev_b, es_b, nv_b, ns_b]
                        # 求测试用例的可疑度
                        sus_a = getSus(index_a, 27)  # 'Arithmetic Mean'
                        sus_b = getSus(index_b, 27)
                        exesum = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                        if sus_a > sus_b:
                            record1 += 1
                            exe = Exelines[i][j][k][0]

                        elif sus_a == sus_b:
                            Sum = [Exelines[i][j][k][0], Exelines[i][j][k][1]]
                            exe = random.choice(Sum)
                            if Exelines[i][j][k][0] == exe:
                                record1 += 1
                            else:
                                for d in exe:
                                    index = Executable.index(d)
                                    metric[index][0] += 1
                                continue

                        else:
                            exe = Exelines[i][j][k][1]
                            for d in exe:
                                index = Executable.index(d)
                                metric[index][0] += 1
                            continue
                        if record1 > 1:
                            continue
                        for d in exe:
                            index = Executable.index(d)
                            metric[index][0] += 1
                        if fault not in exesum:
                            print("VMG中没有failing test case")
                        if fault not in exe:
                            wrong += 1
                        if fault in Exelines[i][j][k][0] and fault in Exelines[i][j][k][1]:
                            al += 1
                        else:
                            if fault in exe:
                                ot += 1
                            else:
                                of += 1
                    elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                        s += 1
                        for d in Exelines[i][j][k][1]:
                            index = Executable.index(d)
                            metric[index][1] += 1
                        record2 += 1
                        if record2 > 1:
                            continue
                        for d in Exelines[i][j][k][0]:
                            index = Executable.index(d)
                            metric[index][1] += 1
                        s += 1

                    else:
                        continue
                else:
                    exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1])) #不会执行
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    if v == 0:
        percent = 0
        pot = 0
        pof = 0
        pal = 0
    else:
        percent = round(wrong / v * 100, 2)
        pot = round(ot / v * 100, 2)
        pof = round(of / v * 100, 2)
        pal = round(al / v * 100, 2)
    return Sus, metric, percent, pot, pof, pal


def SBFL_grep(MG, Result, Executable, Exelines):
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(1):
            for k in range(len(MG[i][j])):
                if len(Exelines[i][j][k][0]) == 0 or len(Exelines[i][j][k][1]) == 0:
                    continue
                if Result[i][j][k][0]:
                    v += 1
                    for d in Exelines[i][j][k][0]:
                        index = Executable.index(d)
                        metric[index][0] += 1
                if not Result[i][j][k][0]:
                    s += 1
                    for d in Exelines[i][j][k][0]:
                        index = Executable.index(d)
                        metric[index][1] += 1
                if Result[i][j][k][1]:
                    v += 1
                    for d in Exelines[i][j][k][1]:
                        index = Executable.index(d)
                        metric[index][0] += 1
                if not Result[i][j][k][1]:
                    s += 1
                    for d in Exelines[i][j][k][1]:
                        index = Executable.index(d)
                        metric[index][1] += 1
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            sus.append(round(getSus2(metric[i], t, v, s), 4))
        Sus.append(sus)
    return Sus, metric


def Exam(Sus, Flag):
    Sus_c = copy.deepcopy(Sus)
    fault = Flag.index(1)
    EXAM = []
    Maximal = []
    for i in range(len(Sus_c)):
        value = Sus_c[i][fault]
        a = 0
        for j in Sus_c[i]:
            if j > value:
                a += 1
        Sus_c[i].sort(reverse=True)
        index_list = [a for a, b in enumerate(Sus_c[i]) if b == value]
        if len(index_list) > 1:
            # 和fault statement可疑度相等
            b = len(index_list)
            exam = ((a + 1) + (a + b)) / 2
        else:
            exam = a + 1
        max_list = [a for a, b in enumerate(Sus_c[i]) if b == Sus_c[i][0]]
        if len(max_list) > 1:
            # 最大值不止一个
            Max = (1 + len(max_list)) / 2
        else:
            Max = 1
        exam = round(exam / len(Sus_c[0]) * 100, 2)
        Max = round(Max / len(Sus_c[0]) * 100, 2)
        Maximal.append(Max)
        EXAM.append(exam)
    return EXAM, Maximal


def TopN(Sus, Flag, N):
    FLAG = []
    Maximal = []
    fault = Flag.index(1)
    for i in range(len(Sus)):
        flag1 = 0
        value = Sus[i][fault]
        a = 0
        for j in Sus[i]:
            if j > value:
                a += 1
        if a >= N:
            # 找不到
            FLAG.append(flag1)
        else:
            index_list = [a for a, b in enumerate(Sus[i]) if b == value]
            if a + len(index_list) <= N:
                flag1 = 1
            else:
                flag1 = (N-a) / len(index_list)
            FLAG.append(round(flag1, 2))
        max_list = [a for a, b in enumerate(Sus[i]) if b == max(Sus[i])]
        if len(max_list) <= N:
            # 最大值不止一个
            flag2 = 1
        else:
            flag2 = N / len(max_list)
        Maximal.append(round(flag2, 2))
    return FLAG, Maximal


def getMetrics_1(row, ws, mu, MG, sus, FAsus, Flag, percent):
    """
    不带权重的，带指标最优值
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    title.append("MS-EXAM")
    title.append("FA-EXAM")
    title.append("MS-EXAMMax")
    for i in [1, 3, 5, 10]:
        title.append("MS-TOP{}".format(i))
        title.append("FA-TOP{}".format(i))
        title.append("MS-TOP{}Max".format(i))
    title.append('SMG')
    title.append('FS')
    title.append('WrongP')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    fs2 = []
    v = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0) + MG[i][j].count(3)
                        sum_fs = MG[i][j].count(3)
                        sum_s += MG[i][k + 1].count(0) + MG[i][k + 1].count(3)
                        sum_fs += MG[i][k + 1].count(3)
                        if sum_s == 0:
                            fs2.append(0)
                        else:
                            fs2.append(round(sum_fs / sum_s * 100, 2))

    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    if len(fs2) == 0:
        fs2.append(0)
    if v == 0:
        print("Mutant{}的VMG为0".format(mu))

    MSexam, MSexamMax = Exam(sus, Flag)
    FAexam, _ = Exam(FAsus[-1], Flag)
    MStop = []
    FAtop = []
    MStopMax = []
    for i in [1, 3, 5, 10]:
        mstop, mstopmax = TopN(sus, Flag, i)
        FAmstop, FAmstopmax = TopN(FAsus[-1], Flag, i)
        MStop.append(mstop)
        FAtop.append(FAmstop)
        MStopMax.append(mstopmax)
    for t in range(len(Formula)):
        value = []
        value.append(MSexam[t])
        value.append(FAexam[t])
        value.append(MSexamMax[t])
        for i in range(4):
            value.append(MStop[i][t])
            value.append(FAtop[i][t])
            value.append(MStopMax[i][t])
        value.append(s)
        value.append(fs)
        value.append(percent)
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_2(row, ws, mu, MG, sus, FAsus, Flag, percent, pot, pof, pal, staDe):
    """
    带权重的，不带指标最优值
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    for t in range(1, 6):
        title.append("MS-EXAM")
        title.append("FA{}-EXAM".format(100 - t * 20))
        for i in [1, 3, 5, 10]:
            title.append("MS-TOP{}".format(i))
            title.append("FA{}-TOP{}".format(100 - t * 20, i))
    title.append('SMG')
    title.append('FS')
    title.append('WrongP')
    title.append('pot')
    title.append('pof')
    title.append('pal')
    title.append('StaDe')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    fs2 = []
    v = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:  #
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0) + MG[i][j].count(3)
                        sum_fs = MG[i][j].count(3)
                        sum_s += MG[i][k + 1].count(0) + MG[i][k + 1].count(3)
                        sum_fs += MG[i][k + 1].count(3)
                        if sum_s == 0:
                            fs2.append(0)
                        else:
                            fs2.append(round(sum_fs / sum_s * 100, 2))

    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    if len(fs2) == 0:
        fs2.append(0)
    if v == 0:
        print("Mutant{}的VMG为0".format(mu))

    MSEXAM = []
    FAEXAM = []
    for t in range(5):
        MSexam, _ = Exam(sus, Flag)
        FAexam, _ = Exam(FAsus[t], Flag)
        MSEXAM.append(MSexam)
        FAEXAM.append(FAexam)
    MSTOP = []
    FATOP = []
    for t in range(5):
        MStop = []
        FAtop = []
        for i in [1, 3, 5, 10]:
            MStop.append(TopN(sus, Flag, i)[0])
            FAtop.append(TopN(FAsus[t], Flag, i)[0])
        MSTOP.append(MStop)
        FATOP.append(FAtop)
    for t in range(len(Formula)):
        value = []
        for k in range(5):
            value.append(MSEXAM[k][t])
            value.append(FAEXAM[k][t])
            for i in range(4):
                value.append(MSTOP[k][i][t])
                value.append(FATOP[k][i][t])
        value.append(s)
        value.append(fs)
        value.append(percent)
        value.append(pot)
        value.append(pof)
        value.append(pal)
        value.append(round(sum(staDe)/len(staDe), 2))
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_3(row, ws, mu, MG, sus, FAsus, PSsus, FAFLsus, MMsus, Flag, percent, pot, pof, pal, staDe):
    """
    带权重的，不带指标最优值
    2025.1
    pure SBFL
    FAFL降低smg权重为0.5
    增加矩阵乘法方法（MM）
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    for t in range(1, 6):
        title.append("MS-EXAM")
        title.append("FA{}-EXAM".format(100 - t * 20))
        title.append("PS-EXAM")
        title.append("FAFL{}-EXAM".format(100 - t * 20))
        title.append("MM-EXAM")
        for i in [1, 3, 5, 10]:
            title.append("MS-TOP{}".format(i))
            title.append("FA{}-TOP{}".format(100 - t * 20, i))
            title.append("PS-TOP{}".format(i))
            title.append("FAFL{}-TOP{}".format(100 - t * 20, i))
            title.append("MM-TOP{}".format(i))
    title.append('SMG')
    title.append('FS')
    title.append('WrongP')
    title.append('pot')
    title.append('pof')
    title.append('pal')
    title.append('StaDe')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    fs2 = []
    v = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:  #
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0) + MG[i][j].count(3)
                        sum_fs = MG[i][j].count(3)
                        sum_s += MG[i][k + 1].count(0) + MG[i][k + 1].count(3)
                        sum_fs += MG[i][k + 1].count(3)
                        if sum_s == 0:
                            fs2.append(0)
                        else:
                            fs2.append(round(sum_fs / sum_s * 100, 2))

    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    if len(fs2) == 0:
        fs2.append(0)
    if v == 0:
        print("Mutant{}的VMG为0".format(mu))

    MSEXAM = []
    FAEXAM = []
    PSEXAM = []
    FAFLEXAM = []
    MMEXAM = []
    for t in range(5):
        MSexam, _ = Exam(sus, Flag)
        FAexam, _ = Exam(FAsus[t], Flag)
        PSexam, _ = Exam(PSsus, Flag)
        FAFLexam, _ = Exam(FAFLsus[t], Flag)
        MMexam, _ = Exam(MMsus, Flag)
        MSEXAM.append(MSexam)
        FAEXAM.append(FAexam)
        PSEXAM.append(PSexam)
        FAFLEXAM.append(FAFLexam)
        MMEXAM.append(MMexam)
    MSTOP = []
    FATOP = []
    PSTOP = []
    FAFLTOP = []
    MMTOP = []
    for t in range(5):
        MStop = []
        FAtop = []
        PStop = []
        FAFLtop = []
        MMtop = []
        for i in [1, 3, 5, 10]:
            MStop.append(TopN(sus, Flag, i)[0])
            FAtop.append(TopN(FAsus[t], Flag, i)[0])
            PStop.append(TopN(PSsus, Flag, i)[0])
            FAFLtop.append(TopN(FAFLsus[t], Flag, i)[0])
            MMtop.append(TopN(MMsus, Flag, i)[0])
        MSTOP.append(MStop)
        FATOP.append(FAtop)
        PSTOP.append(PStop)
        FAFLTOP.append(FAFLtop)
        MMTOP.append(MMtop)
    for t in range(len(Formula)):
        value = []
        for k in range(5):
            value.append(MSEXAM[k][t])
            value.append(FAEXAM[k][t])
            value.append(PSEXAM[k][t])
            value.append(FAFLEXAM[k][t])
            value.append(MMEXAM[k][t])
            for i in range(4):
                value.append(MSTOP[k][i][t])
                value.append(FATOP[k][i][t])
                value.append(PSTOP[k][i][t])
                value.append(FAFLTOP[k][i][t])
                value.append(MMTOP[k][i][t])
        value.append(s)
        value.append(fs)
        value.append(percent)
        value.append(pot)
        value.append(pof)
        value.append(pal)
        value.append(round(sum(staDe)/len(staDe), 2))
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_3_test(row, ws, mu, MG, sus, FAsus, PSsus, FAFLsus, MMsus, SBFLsus, Flag, percent, pot, pof, pal, staDe):
    """
    带权重的，不带指标最优值
    2025.1
    pure SBFL
    FAFL降低smg权重为0.5
    增加矩阵乘法方法（MM）
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    title.append("MS-EXAM")
    title.append("FA-EXAM")
    title.append("PS-EXAM")
    title.append("FAFL-EXAM")
    title.append("MM-EXAM")
    title.append("SBFL-EXAM")
    for i in [1, 3, 5, 10]:
        title.append("MS-TOP{}".format(i))
        title.append("FA-TOP{}".format( i))
        title.append("PS-TOP{}".format(i))
        title.append("FAFL-TOP{}".format(i))
        title.append("MM-TOP{}".format(i))
        title.append("SBFL-TOP{}".format(i))
    title.append('SMG')
    title.append('FS')
    title.append('WrongP')
    title.append('pot')
    title.append('pof')
    title.append('pal')
    title.append('StaDe')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    fs2 = []
    v = 0
    for i in range(len(MG)):
        if 1 not in MG[i][0]:
            continue
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
                if j == 0:
                    if MG[i][j][k] == 1:
                        v += 1
                        sum_s = MG[i][j].count(0)# + MG[i][j].count(3)
                        sum_fs = MG[i][j].count(3)
                        sum_s += MG[i][k + 1].count(0)# + MG[i][k + 1].count(3)
                        sum_fs += MG[i][k + 1].count(3)
                        if sum_s == 0:
                            fs2.append(0)
                        else:
                            fs2.append(round(sum_fs / sum_s * 100, 2))
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    if len(fs2) == 0:
        fs2.append(0)
    if v == 0:
        print("Mutant{}的VMG为0".format(mu))
    MSexam, _ = Exam(sus, Flag)
    FAexam, _ = Exam(FAsus, Flag)
    PSexam, _ = Exam(PSsus, Flag)
    FAFLexam, _ = Exam(FAFLsus, Flag)
    MMexam, _ = Exam(MMsus, Flag)
    SBFLexam, _ = Exam(SBFLsus, Flag)
    MStop = []
    FAtop = []
    PStop = []
    FAFLtop = []
    MMtop = []
    SBFLtop = []
    for i in [1, 3, 5, 10]:
        MStop.append(TopN(sus, Flag, i)[0])
        FAtop.append(TopN(FAsus, Flag, i)[0])
        PStop.append(TopN(PSsus, Flag, i)[0])
        FAFLtop.append(TopN(FAFLsus, Flag, i)[0])
        MMtop.append(TopN(MMsus, Flag, i)[0])
        SBFLtop.append(TopN(SBFLsus, Flag, i)[0])
    for t in range(len(Formula)):
        value = []
        value.append(MSexam[t])
        value.append(FAexam[t])
        value.append(PSexam[t])
        value.append(FAFLexam[t])
        value.append(MMexam[t])
        value.append(SBFLexam[t])
        for i in range(4):
            value.append(MStop[i][t])
            value.append(FAtop[i][t])
            value.append(PStop[i][t])
            value.append(FAFLtop[i][t])
            value.append(MMtop[i][t])
            value.append(SBFLtop[i][t])
        value.append(s)
        value.append(fs)
        value.append(percent)
        value.append(pot)
        value.append(pof)
        value.append(pal)
        if len(staDe) == 0:
            value.append(0)
        else:
            value.append(round(sum(staDe)/len(staDe), 2))
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_4(row, ws, mu, FAFLVariantsus, Flag):
    """
    带权重的，不带指标最优值
    2025.2
    FAFL's variants
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2',
               'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    nn = 11
    for k in range(nn):
        for t in range(nn):
            title.append("FAFLV{}S{}-EXAM".format(round(1 - k * 0.1, 1), round(1 - t * 0.1, 1)))
            for i in [1, 3, 5, 10]:
                title.append("FAFLV{}S{}-TOP{}".format(round(1 - k * 0.1, 1), round(1 - t * 0.1, 1), i))
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    FAFLEXAM = []
    for k in range(nn):
        FAFLE = []
        for t in range(nn):
            FAFLexam, _ = Exam(FAFLVariantsus[k][t], Flag)
            FAFLE.append(FAFLexam)
        FAFLEXAM.append(FAFLE)

    FAFLTOP = []
    for k in range(nn):
        FAFLT = []
        for t in range(nn):
            FAFLtop = []
            for i in [1, 3, 5, 10]:
                FAFLtop.append(TopN(FAFLVariantsus[k][t], Flag, i)[0])
            FAFLT.append(FAFLtop)
        FAFLTOP.append(FAFLT)
    for t in range(len(Formula)):
        value = []
        for k in range(nn):
            for l in range(nn):
                value.append(FAFLEXAM[k][l][t])
                for i in range(4):
                    value.append(FAFLTOP[k][l][i][t])
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_4_test(row, ws, mu, FAFLVariantsus, Flag):
    """
    带权重的，不带指标最优值
    2025.2
    FAFL's variants
    """
    Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
               'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal',
               'Rogers&Tanimoto', 'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2',
               'AMPLE2', 'Wong3', 'Arithmetic Mean', 'Cohen', 'Fleiss']
    datadict = {}
    title = []
    for k in range(11):
        for t in range(11):
            title.append("FAFLV{}S{}-EXAM".format(round(1 - k * 0.1, 1), round(1 - t * 0.1, 1)))
            for i in [1, 3, 5, 10]:
                title.append("FAFLV{}S{}-TOP{}".format(round(1 - k * 0.1, 1), round(1 - t * 0.1, 1), i))
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)

    # N = [1, 3, 5, 10]
    # for t in range(len(Formula)):
    #     value = []
    #     for k in range(11):
    #         for l in range(11):
    #             FAFLexam, _ = Exam(FAFLVariantsus[k][l], Flag)
    #             value.append(FAFLexam[t])
    #             for i in range(4):
    #                 value.append(TopN(FAFLVariantsus[k][l], Flag, N[i])[0][t])
    #     data = {
    #         Formula[t]: value
    #     }
    #     datadict.update(data)

    FAFLEXAM = []
    for k in range(11):
        FAFLE = []
        for t in range(11):
            FAFLexam, _ = Exam(FAFLVariantsus[k][t], Flag)
            FAFLE.append(FAFLexam)
        FAFLEXAM.append(FAFLE)
    FAFLTOP = []
    for k in range(11):
        FAFLT = []
        for t in range(11):
            FAFLtop = []
            for i in [1, 3, 5, 10]:
                FAFLtop.append(TopN(FAFLVariantsus[k][t], Flag, i)[0])
            FAFLT.append(FAFLtop)
        FAFLTOP.append(FAFLT)
    for t in range(len(Formula)):
        value = []
        for k in range(11):
            for l in range(11):
                value.append(FAFLEXAM[k][l][t])
                for i in range(4):
                    value.append(FAFLTOP[k][l][i][t])
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row
