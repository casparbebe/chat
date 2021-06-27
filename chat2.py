# 讀取檔案
def read_file(filename):
    records = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            records.append(line.strip())
    return records


# 轉換資料
def convert(records):
    person = None
    mom_word_count = 0
    mom_sticker_count = 0
    mom_image_count = 0
    brother_word_count = 0
    brother_sticker_count = 0
    brother_image_count = 0
    my_word_count = 0
    my_sticker_count = 0
    my_image_count = 0
    for record in records:
        s = record.split(' ')
        time = s[0]
        name = s[1]
        if name == '蕭幸宜':
            if s[2] == '貼圖':
                mom_sticker_count += 1
            elif s[2] == '圖片':
                mom_image_count += 1
            else:
                for msg in s[2:]:
                    mom_word_count += len(msg)
        elif name == '張榮哲':
            if s[2] == '貼圖':
                brother_sticker_count += 1
            elif s[2] == '圖片':
                brother_image_count += 1
            else:
                for msg in s[2:]:
                    brother_word_count += len(msg)
        elif name == '張榮洋':
            if s[2] == '貼圖':
                my_sticker_count += 1
            elif s[2] == '圖片':
                my_image_count += 1
            else:
                for msg in s[2:]:
                    my_word_count += len(msg)
    print('媽媽說了', mom_word_count, '個字', '傳了', mom_sticker_count, '個貼圖', mom_image_count, '張圖片')
    print('哥哥說了', brother_word_count, '個字', '傳了', brother_sticker_count, '個貼圖', brother_image_count, '張圖片')
    print('我說了', my_word_count, '個字', '傳了', my_sticker_count, '個貼圖', my_image_count, '張圖片')


# 寫入檔案    
def write_file(filename, records):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for record in records:
            f.write(record + '\n')


# 主函示
def main():
    records = read_file('[LINE]MY DEAR.txt')
    records = convert(records)
    # write_file('output.txt', records)

main()