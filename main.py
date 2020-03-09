import os


def mask(name, name_with_reg):
    start1 = 0
    end1 = 0
    start2 = 0
    end2 = 0
    x10 = 0
    x20 = 0
    stage = 0
    while start1 != len(name_with_reg):
        stage += 1
        for i in range(end1, len(name_with_reg)):
            if name_with_reg[i] != '?' and name_with_reg[i] != '*':
                start2 = i
                break
        else:
            start2 = len(name_with_reg)
        a, b = name_with_reg.find('?', start2), name_with_reg.find('*', start2)
        if a != -1 and b != -1:
            end2 = a if a < b else b
        elif a > b:
            end2 = a
        elif a < b:
            end2 = b
        else:
            end2 = len(name_with_reg)

        x1 = name.find(name_with_reg[start1:end1], x10)
        x2 = name.find(name_with_reg[start2:end2], x20) if start2 != len(name_with_reg) else len(name)
        if x1 == -1:
            x1 = len(name)
            return False
        if x2 == -1:
            x2 = len(name)
            return False
        elif '*' not in name_with_reg[end1:start2] and x2 - (x1 + end1 - start1) > start2 - end1:
            return False

        start1 = start2
        end1 = end2
        x10 = x1
        x20 = x2
    else:
        return True


def find(file_name_with_reg):
    current_dir = os.getcwd()
    list_dirs = [x.name for x in os.scandir() if x.is_dir()]
    list_files = [x.name for x in os.scandir() if x.is_file()]
    list_files.sort()
    list_dirs.sort()
    for file in list_files:
        if mask(file, file_name_with_reg):
            print(current_dir + '\\' + file)
    for dir in list_dirs:
        os.chdir(current_dir + '\\' + dir)
        find(file_name_with_reg)


find('*.txt')