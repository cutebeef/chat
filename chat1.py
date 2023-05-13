import os #operating system

#讀取檔案
def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8-sig') as f:#-sig 去除檔案開頭怪符號
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue #下面的都跳過，為了跳過new.append()          
        elif line == 'Tom':
            person = 'Tom'
            continue 
        if person: #如果person有被設值過的才做
            new.append(person + ': ' + line)
    return new

#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f: #r讀取 w寫入
        for line in lines:
            f.write(line + '\n')
   # print(n)


def main():#將此段執行程式包裹成一個主要執行程式碼
    lines = read_file('input1.txt')
    lines = convert(lines)
    write_file('output1.txt', lines)


main()


