import re
if __name__ == '__main__':
    with open('sample.txt','r',encoding='utf-8') as f:
        content = f.read()
        content= content.lower()
        print(content)
    content=re.sub(r'[^a-z0-9\s]',' ',content)
    print(content)

    words = content.split()
    print(words)

    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0) +1
    print(word_count)

    with open('result.txt','w',encoding='utf-8') as f:
        for word ,count in word_count.items():
            f.write(f"{word}{count}\n")