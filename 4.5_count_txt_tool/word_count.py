import re
import sys
# if __name__ == '__main__':
#     with open('sample.txt','r',encoding='utf-8') as f:
#         content = f.read()
#         content= content.lower()
#         print(content)
#     content=re.sub(r'[^a-z0-9\s]',' ',content)
#     print(content)
#
#     words = content.split()
#     print(words)
#
#     word_count={}
#     for word in words:
#         word_count[word]=word_count.get(word,0) +1
#     print(word_count)
#
#     with open('result.txt','w',encoding='utf-8') as f:
#         for word ,count in word_count.items():
#             f.write(f"{word}{count}\n")




def count_words(input_file,output_file):
    try:
        with open(input_file,'r',encoding='utf-8') as f:
            content = f.read()
            content = content.lower()
    except FileNotFoundError:
        print(f'未找到{input_file}文件')
        return
    except UnicodeDecodeError:
        print(f'{input_file}文件的格式不正确请转为utf-8格式')
    content = re.sub(r'[^a-z0-9\s]', ' ', content)
    print(content)

    words = content.split()
    print(words)

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in word_count.items():
            f.write(f"{word} {count}\n")

if __name__ == '__main__':
    if len(sys.argv) !=3:
        print('使用方法：python word_count.py <输入文件> <输出文件>')
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    count_words(input_file,output_file)

