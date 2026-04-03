if __name__ == '__main__':
    n=int(input())
    if n % 400==0:
        print(n, '年是闰年')
    elif n % 4==0 and n % 100 != 0:
        print(n,'年是闰年')
    else:print(n,'不是闰年')


if __name__ == '__main__':
    n=list(map(int,input().strip().split()))
    new=[]
    for each in n :
        if each % 2==0:
            new.append(each)
    print(new)


if __name__ == '__main__':
    text_str=input()
    words = text_str.split()
    result=[]
    for word in words:
        if word[0]>='A'and word[0]<='Z':
            result.append(word)
    print(result)


