import csv
import os
import sys
import subprocess
import filecmp

num_mu = 21
num_case = 100
num_mr = 11
outputdir = '/Users/rendaixu/OneDrive/data/MT/MSBF/PT2/RandomOutput0.csv'
csvFile = open(outputdir, "r")
reader = csv.reader(csvFile)
# # 建立空字典
# # originaloutput = {}
# # for item in reader:
# #     # 忽略第一行
# #     if reader.line_num == 1:
# #         continue
# #     try:
# #         originaloutput[item[0]] = item[1].split("\n")
# #     except:
# #         print(item)
# #         print(reader.line_num)
# #         break
# #
# # mutateOutput = []
# # remove_mu = [2, 4, 5, 6, 10, 11]  # SMG超过99.**%
# # for mu in range(1, num_mu+1):
# #     if mu in remove_mu:
# #         continue
# #     outputdir = '/Users/rendaixu/OneDrive/data/MT/MSBF/PT2/RandomOutput{}.csv'.format(mu)
# #     csvFile = open(outputdir, "r")
# #     reader = csv.reader(csvFile)
# #     mutateoutput = {}
# #     for item in reader:
# #         # 忽略第一行
# #         if reader.line_num == 1:
# #             continue
# #         try:
# #             mutateoutput[item[0]] = item[1].split("\n")
# #         except:
# #             print(item)
# #             print(reader.line_num)
# #             break
# #     mutateOutput.append(mutateoutput)
# #     csvFile.close()
# #
# #
# statevalue = []
# statetitle = []
# pq = 0
# with open('/Users/rendaixu/OneDrive/data/MT/MSBF/PT2/statementResult0.csv', 'w') as csvfile1:
#     spamwriter1 = csv.writer(csvfile1, delimiter=',')
#     for i in range(num_case):
#         if os.path.exists("print_tokens2.gcda"):
#             os.remove("print_tokens2.gcda")
#         compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/printtokens2_v0/print_tokens2.c"]
#         # 执行编译程序并将标准错误输出重定向到空设备文件中
#         try:
#             output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
#         except subprocess.CalledProcessError as e:
#             output = e.output
#             print("input{}编译失败，错误信息：".format(i), output.decode())
#         else:
#             pass
#
#         l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/RandomInput/input{}.txt'.format(i)
#
#         command = ["./a.out", l1]
#         try:
#             output = subprocess.check_output(command)
#         except subprocess.CalledProcessError as e:
#             output = e.output
#             print("input{}执行失败，输出信息：".format(i), output.decode())
#         else:
#             # print("input{}执行成功，输出信息：\n".format(i), output.decode())
#             pass
#         k = 1  # 获取可执行行
#         command = ["gcov", "print_tokens2.c"]
#         try:
#             output = subprocess.check_output(command)
#         except subprocess.CalledProcessError as e:
#             output = e.output
#             print("input{}命令执行失败，错误信息：".format(i), output.decode())
#         else:
#             print("input{}命令执行成功，输出信息：\n".format(i), output.decode())
#             # pass
#
#         statevalue.append("input{}".format(i))
#         statetitle.append("inputs")
#
#         fp2 = open("print_tokens2.c.gcov")
#         for line1 in fp2:
#             try:
#                 flag = line1.split(":")[0]
#                 flag1 = line1.split(":")[1].strip()
#                 if flag1[0] == '0':
#                     continue
#                 if "-" in flag:
#                     k = k + 1
#                     continue
#                 elif "#####" in flag:
#                     statevalue.append("0")
#                     statetitle.append(k)
#                     k = k + 1
#                 else:
#                     statevalue.append("1")
#                     statetitle.append(k)
#                     k = k + 1
#             except:
#                 print("exiting")
#                 exit(1)
#
#         for mu in range(1, num_mu+1):
#             statetitle.append("Mutant{}".format(mu))
#         if pq == 0:
#             spamwriter1.writerow(statetitle)
#             pq = 1
#         # for mu in range(1, num_mu+1):
#         #     output_oringinal = originaloutput["output{}".format(i)]
#         #     output_mutant = mutateOutput[mu-1]["output{}".format(i)]
#         #     if output_oringinal == output_mutant:
#         #         statevalue.append(int('0'))
#         #     else:
#         #         statevalue.append(int('1'))
#         if len(statevalue) > 1:
#             spamwriter1.writerow(statevalue)
#             statevalue = []
#             statetitle = []
#         else:
#             statevalue = []
#             statetitle = []
#         for m in range(num_mr):
#             if os.path.exists("print_tokens2.gcda"):
#                 os.remove("print_tokens2.gcda")
#             compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/printtokens2_v0/print_tokens2.c"]
#             # 执行编译程序并将标准错误输出重定向到空设备文件中
#             try:
#                 output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
#             except subprocess.CalledProcessError as e:
#                 output = e.output
#                 print("input{}_{}编译失败，错误信息：".format(i, m), output.decode())
#             else:
#                 pass
#
#             l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/RandomInput/input{}_{}.txt'.format(i, m)
#             command = ["./a.out", l1]
#             try:
#                 output = subprocess.check_output(command)
#             except subprocess.CalledProcessError as e:
#                 output = e.output
#                 print("input{}_{}执行失败，输出信息：".format(i, m), output.decode())
#             else:
#                 # print("input{}执行成功，输出信息：\n".format(i), output.decode())
#                 pass
#             k = 1
#             command = ["gcov", "print_tokens2.c"]
#             try:
#                 output = subprocess.check_output(command)
#             except subprocess.CalledProcessError as e:
#                 output = e.output
#                 print("input{}_{}命令执行失败，错误信息：".format(i, m), output.decode())
#             else:
#                 print("input{}_{}命令执行成功，输出信息：\n".format(i, m), output.decode())
#                 # pass
#
#             statevalue.append("input{}_{}".format(i, m))
#             statetitle.append("inputs")
#
#             fp2 = open("print_tokens2.c.gcov")
#             for line1 in fp2:
#                 try:
#                     flag = line1.split(":")[0]
#                     flag1 = line1.split(":")[1].strip()
#                     if flag1[0] == '0':
#                         continue
#                     if "-" in flag:
#                         k = k + 1
#                         continue
#                     elif "#####" in flag:
#                         statevalue.append("0")
#                         statetitle.append(k)
#                         k = k + 1
#                     else:
#                         statevalue.append("1")
#                         statetitle.append(k)
#                         k = k + 1
#                 except:
#                     print("exiting")
#                     exit(1)
#
#             for mu in range(1, num_mu+1):
#                 statetitle.append("Mutant{}".format(mu))
#             if pq == 0:
#                 spamwriter1.writerow(statetitle)
#                 pq = 1
#             # for mu in range(1, num_mu+1):
#             #     output_oringinal = originaloutput["output{}_{}".format(i, m)]
#             #     output_mutant = mutateOutput[mu-1]["output{}_{}".format(i, m)]
#             #     if output_oringinal == output_mutant:
#             #         statevalue.append(int('0'))
#             #     else:
#             #         statevalue.append(int('1'))
#             if len(statevalue) > 1:
#                 spamwriter1.writerow(statevalue)
#                 statevalue = []
#                 statetitle = []
#             else:
#                 statevalue = []
#                 statetitle = []
#             for n in range(num_mr):
#                 if os.path.exists("print_tokens2.gcda"):
#                     os.remove("print_tokens2.gcda")
#                 compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/printtokens2_v0/print_tokens2.c"]
#                 # 执行编译程序并将标准错误输出重定向到空设备文件中
#                 try:
#                     output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
#                 except subprocess.CalledProcessError as e:
#                     output = e.output
#                     print("input{}_{}_{}编译失败，错误信息：".format(i, m, n), output.decode())
#                 else:
#                     pass
#
#                 l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/input{}_{}_{}.txt'.format(i, m, n)
#                 # os.system("./a.out " + l1)
#                 command = ["./a.out", l1]
#                 try:
#                     output = subprocess.check_output(command)
#                 except subprocess.CalledProcessError as e:
#                     output = e.output
#                     print("input{}_{}_{}执行失败，输出信息：".format(i, m, n), output.decode())
#                 else:
#                     # print("input{}执行成功，输出信息：\n".format(i), output.decode())
#                     pass
#                 k = 1
#                 command = ["gcov", "print_tokens2.c"]
#                 try:
#                     output = subprocess.check_output(command)
#                 except subprocess.CalledProcessError as e:
#                     output = e.output
#                     print("input{}_{}_{}命令执行失败，错误信息：".format(i, m, n), output.decode())
#                 else:
#                     print("input{}_{}_{}命令执行成功，输出信息：\n".format(i, m, n), output.decode())
#                     # pass
#
#                 statevalue.append("input{}_{}_{}".format(i, m, n))
#                 statetitle.append("inputs")
#
#                 fp2 = open("print_tokens2.c.gcov")
#                 for line1 in fp2:
#                     try:
#                         flag = line1.split(":")[0]
#                         flag1 = line1.split(":")[1].strip()
#                         if flag1[0] == '0':
#                             continue
#                         if "-" in flag:
#                             k = k + 1
#                             continue
#                         elif "#####" in flag:
#                             statevalue.append("0")
#                             statetitle.append(k)
#                             k = k + 1
#                         else:
#                             statevalue.append("1")
#                             statetitle.append(k)
#                             k = k + 1
#                     except:
#                         print("exiting")
#                         exit(1)
#
#                 for mu in range(1, num_mu+1):
#                     statetitle.append("Mutant{}".format(mu))
#                 if pq == 0:
#                     spamwriter1.writerow(statetitle)
#                     pq = 1
#                 # for mu in range(1, num_mu+1):
#                 #     output_oringinal = originaloutput["output{}_{}_{}".format(i, m, n)]
#                 #     output_mutant = mutateOutput[mu - 1]["output{}_{}_{}".format(i, m, n)]
#                 #     if output_oringinal == output_mutant:
#                 #         statevalue.append(int('0'))
#                 #     else:
#                 #         statevalue.append(int('1'))
#                 if len(statevalue) > 1:
#                     spamwriter1.writerow(statevalue)
#                     statevalue = []
#                     statetitle = []
#                 else:
#                     statevalue = []
#                     statetitle = []
# 建立空字典
originaloutput = {}
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    try:
        originaloutput[item[0]] = item[1].split("\n")
    except:
        print(item)
        print(reader.line_num)
        break

remove_mu = [2, 4, 5, 6, 10, 11]  # SMG超过99.**%
for mutant in range(1, num_mu+1):
    label = 0
    if mutant not in remove_mu:
        continue
    outputdir = '/Users/rendaixu/OneDrive/data/MT/MSBF/PT2/RandomOutput{}.csv'.format(mutant)
    csvFile = open(outputdir, "r")
    reader = csv.reader(csvFile)
    mutateoutput = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        try:
            mutateoutput[item[0]] = item[1].split("\n")
        except:
            print(item)
            print(reader.line_num)
            break
    statevalue = []
    statetitle = []
    pq = 0
    with open('/Users/rendaixu/OneDrive/data/MT/MSBF/PT2/statementResult{}.csv'.format(mutant), 'w') as csvfile1:
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        for i in range(num_case):
            if os.path.exists("print_tokens2.gcda"):
                os.remove("print_tokens2.gcda")
            compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/UsedMutants/printtokens2_v{}/print_tokens2.c".format(mutant)]
            # 执行编译程序并将标准错误输出重定向到空设备文件中
            try:
                output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}编译失败，错误信息：".format(i), output.decode())
            else:
                pass

            l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/RandomInput/input{}.txt'.format(i)

            command = ["./a.out", l1]
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
                    label = 1
                    break
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}执行失败，输出信息：".format(i), output.decode())
                label = 1
                break
            else:
                # print("input{}执行成功，输出信息：\n".format(i), output.decode())
                pass
            k = 1  # 获取可执行行
            command = ["gcov", "print_tokens2.c"]
            try:
                output = subprocess.check_output(command)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}命令执行失败，错误信息：".format(i), output.decode())
            else:
                print("input{}命令执行成功，输出信息：\n".format(i), output.decode())
                # pass

            statevalue.append("input{}".format(i))
            statetitle.append("inputs")

            fp2 = open("print_tokens2.c.gcov")
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
            # for mu in range(1, num_mu+1):
            output_oringinal = originaloutput["output{}".format(i)]
            output_mutant = mutateoutput["output{}".format(i)]
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
            for m in range(num_mr):
                if os.path.exists("print_tokens2.gcda"):
                    os.remove("print_tokens2.gcda")
                compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/UsedMutants/printtokens2_v{}/print_tokens2.c".format(mutant)]
                # 执行编译程序并将标准错误输出重定向到空设备文件中
                try:
                    output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print("input{}_{}编译失败，错误信息：".format(i, m), output.decode())
                else:
                    pass

                l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/RandomInput/input{}_{}.txt'.format(i, m)
                command = ["./a.out", l1]
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
                        label = 1
                        break
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print("input{}_{}执行失败，输出信息：".format(i, m), output.decode())
                    label = 1
                    break
                else:
                    # print("input{}执行成功，输出信息：\n".format(i), output.decode())
                    pass
                k = 1
                command = ["gcov", "print_tokens2.c"]
                try:
                    output = subprocess.check_output(command)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print("input{}_{}命令执行失败，错误信息：".format(i, m), output.decode())
                else:
                    print("input{}_{}命令执行成功，输出信息：\n".format(i, m), output.decode())
                    # pass

                statevalue.append("input{}_{}".format(i, m))
                statetitle.append("inputs")

                fp2 = open("print_tokens2.c.gcov")
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
                # for mu in range(1, num_mu+1):
                output_oringinal = originaloutput["output{}_{}".format(i, m)]
                output_mutant = mutateoutput["output{}_{}".format(i, m)]
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
                for n in range(num_mr):
                    if os.path.exists("print_tokens2.gcda"):
                        os.remove("print_tokens2.gcda")
                    compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/UsedMutants/printtokens2_v{}/print_tokens2.c".format(mutant)]
                    # 执行编译程序并将标准错误输出重定向到空设备文件中
                    try:
                        output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
                    except subprocess.CalledProcessError as e:
                        output = e.output
                        print("input{}_{}_{}编译失败，错误信息：".format(i, m, n), output.decode())
                    else:
                        pass
                    l1 = '/Users/rendaixu/OneDrive/data/MT/STVR/PT2/RandomInput/input{}_{}_{}.txt'.format(i, m, n)
                    # os.system("./a.out " + l1)
                    command = ["./a.out", l1]
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
                            label = 1
                            break
                    except subprocess.CalledProcessError as e:
                        output = e.output
                        print("input{}_{}_{}执行失败，输出信息：".format(i, m, n), output.decode())
                        label = 1
                        break
                    else:
                        # print("input{}执行成功，输出信息：\n".format(i), output.decode())
                        pass
                    k = 1
                    command = ["gcov", "print_tokens2.c"]
                    try:
                        output = subprocess.check_output(command)
                    except subprocess.CalledProcessError as e:
                        output = e.output
                        print("input{}_{}_{}命令执行失败，错误信息：".format(i, m, n), output.decode())
                    else:
                        print("input{}_{}_{}命令执行成功，输出信息：\n".format(i, m, n), output.decode())
                        # pass

                    statevalue.append("input{}_{}_{}".format(i, m, n))
                    statetitle.append("inputs")

                    fp2 = open("print_tokens2.c.gcov")
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
                    # for mu in range(1, num_mu+1):
                    output_oringinal = originaloutput["output{}_{}_{}".format(i, m, n)]
                    output_mutant = mutateoutput["output{}_{}_{}".format(i, m, n)]
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
                if label == 1:
                   break
            if label == 1:
                break
    if label == 1:
        continue




