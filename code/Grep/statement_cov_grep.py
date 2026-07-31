import csv
import os
import sys
import subprocess
import filecmp
import test_grep
import re

def extract_number_after_letter(s):
    # 正则表达式匹配：字母后面的数字，允许下划线存在或不存在
    match = re.search(r'[A-Za-z](\d+)', s)
    if match:
        return match.group(1)  # 提取匹配到的数字部分
    return None  # 如果没有匹配到则返回 None

def get_output(mu):
    outputdir1 = '/Users/rendaixu/OneDrive/data/MT/MSBF/grep/RandomOutput0.csv'
    outputdir2 = '/Users/rendaixu/OneDrive/data/MT/MSBF/grep/RandomOutput{}.csv'.format(mu)
    # outputdir1 = '/home/rdx/data/MT/STVR/grep/TranstoServer/RandomOutput0.csv'
    # outputdir2 = '/home/rdx/data/MT/STVR/grep/TranstoServer/RandomOutput{}.csv'.format(mu)
    csvFile = open(outputdir1, "r")
    reader = csv.reader(csvFile)
    # 建立空字典
    outputcase1 = {}
    select = []
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        try:
            result = extract_number_after_letter(item[0])
            if result not in select and len(select) <= 100:
                select.append(result)
            if len(select) > 100:
                break
            outputcase1[item[0]] = item[1]
        except:
            print(item)
            print(reader.line_num)
            break
    csvFile.close()

    csvFile = open(outputdir2, "r")
    reader = csv.reader(csvFile)
    outputcase2 = {}
    select = []
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        try:
            result = extract_number_after_letter(item[0])
            if result not in select and len(select) <= 100:
                select.append(result)
            if len(select) > 100:
                break
            outputcase2[item[0]] = item[1]
        except:
            print(item)
            print(reader.line_num)
            break
    csvFile.close()
    return outputcase1, outputcase2


if __name__ == "__main__":
    remove_mu = [1, 4, 6, 7, 8, 9, 19]
    for mutant in range(31, 51):
        if mutant in remove_mu:
            continue
        # label = 0
        output1, output2 = get_output(mutant)
        statevalue = []
        statetitle = []
        pq = 0
        inputdata = test_grep.get_input()
        # '/Applications/work/data/MT/STVR/grep/statementResult.csv'
        str = '/Users/rendaixu/OneDrive/data/MT/MSBF/grep/statementResult{}_1.csv'.format(mutant)
        csvfile1 = open('/Users/rendaixu/OneDrive/data/MT/MSBF/grep/statementResult{}_1.csv'.format(mutant), 'w')
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        t = 1
        x = 1
        flag = 0
        for i in range(len(output1)):
            if mutant == 29:
                if x < 33:
                    t += 1
                    print(i)
                    if t > 1000:
                        x += 1
                        t = 1
                    continue
                elif x == 33 and flag == 0:
                    csvfile1 = open(
                        '/Users/rendaixu/OneDrive/data/MT/MSBF/grep/statementResult{}_{}.csv'.format(mutant, x), 'w')
                    spamwriter1 = csv.writer(csvfile1, delimiter=',')
                    flag = 1
            if t > 1000:
                x += 1
                t = 1
                pq = 0
                csvfile1 = open('/Users/rendaixu/OneDrive/data/MT/MSBF/grep/statementResult{}_{}.csv'.format(mutant, x), 'w')
                spamwriter1 = csv.writer(csvfile1, delimiter=',')
            if os.path.exists("grep.gcda"):
                os.remove("grep.gcda")
            name = list(output1.keys())[i]
            compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/grep_v{}/grep.c".format(mutant)]
            # 执行编译程序并将标准错误输出重定向到空设备文件中
            try:
                output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"编译失败，错误信息：", output.decode())
            else:
                pass
            # 判断MR
            last_underscore = name.rfind("_")
            mr = 'MR'+name[last_underscore + 1:]
            if 'source' in name:
                start = name.find('output_source') + len('output_source')
                end = name.find('_', start)
                index = name[start:end]
                input_index = name[start:last_underscore]
                pattern = inputdata.get('input'+input_index)
                if mr != 'MR11' and mr != 'MR9':
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
                elif mr == 'MR11':
                    command = ["./a.out", '-E', pattern, './targetFiles/MR11_' + index]
                else:
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
            else:
                start = name.find('output_follow') + len('output_follow')
                end = name.find('_', start)
                index = name[start:end]
                input_index = name[start:]
                pattern = inputdata.get('input'+input_index)
                if mr != 'MR11' and mr != 'MR9':
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
                elif mr == 'MR11':
                    command = ["./a.out", '-E', pattern, './targetFiles/MR11_' + index]
                else:
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test_MR9_follow']

            try:
                # output = subprocess.check_output(command)
                timeout_seconds = 60  # 设置超时时间为60秒
                # 启动进程
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    # 执行命令并设置超时时间
                    output, error = process.communicate(timeout=timeout_seconds)
                    # 输出命令执行结果
                    # print(output.decode("utf-8"))
                except subprocess.TimeoutExpired:
                    # 如果命令超时，结束进程
                    process.kill()
                    # 输出超时信息
                    print("Command execution timeout!")
                    # label = 1
                    break
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"执行失败，输出信息：", output.decode())
            else:
                # print("input{}执行成功，输出信息：\n".format(i), output.decode())
                pass

            k = 1  # 获取可执行行
            command = ["gcov", "grep.c"]
            try:
                output = subprocess.check_output(command)
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"命令执行失败，错误信息：", output.decode())
            else:
                print(name+"命令执行成功，输出信息：\n", output.decode())
                # pass

            statevalue.append(name)
            statetitle.append("test cases")

            fp2 = open("grep.c.gcov")
            for line1 in fp2:
                try:
                    flag = line1.split(":")[0]
                    flag1 = line1.split(":")[1].strip()
                    if flag1[0] == '0':
                        continue
                    if "-" in flag:
                        k = k + 1
                        continue
                    elif "#####" in flag:
                        statevalue.append("0")
                        statetitle.append(k)
                        k = k + 1
                    else:
                        statevalue.append("1")
                        statetitle.append(k)
                        k = k + 1
                except:
                    print("exiting")
                    exit(1)

            # for mu in range(1, num_mu+1):
            #     statetitle.append("Mutant{}".format(mu))
            statetitle.append("Oracle")
            if pq == 0:
                spamwriter1.writerow(statetitle)
                pq = 1
            # for mu in range(1, 12):
            #     output_oringinal = Output[0].get(name)
            #     output_mutant = Output[mu].get(name)
            #     if output_oringinal == output_mutant:
            #         statevalue.append(int('0'))
            #     else:
            #         statevalue.append(int('1'))
            output_oringinal = output1[name]
            output_mutant = output2[name]
            if output_oringinal == output_mutant:
                statevalue.append(int('0'))
            else:
                statevalue.append(int('1'))
            if len(statevalue) > 1:
                spamwriter1.writerow(statevalue)
                statevalue = []
                statetitle = []
            else:
                statevalue = []
                statetitle = []
            t += 1
            # break
        csvfile1.close()
