import os #operating system

#讀取檔案
def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8-sig') as f:#-sig 去除檔案開頭怪符號
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]   #開頭n[:3]前三個東西 開頭0~3結尾(不包含)  中間 n[2:4] n[2]跟n[3]  結尾n[-2: ] 從後面數來 倒數兩個 結尾值留空就是到最後
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2: ]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1 
            else:          
                for m in s[2: ]:            
                    viki_word_count += len(m)

    print('Allen說了', allen_word_count,'個字', '傳了', allen_sticker_count, '個貼圖', '以及傳了', allen_image_count, '張圖片')
    print('Viki說了', allen_word_count,'個字', '傳了', viki_sticker_count, '個貼圖', '以及傳了', viki_image_count, '張圖片')

#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f: #r讀取 w寫入
        for line in lines:
            f.write(line + '\n')


def main():#將此段執行程式包裹成一個主要執行程式碼
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output2.txt', lines)

main()


