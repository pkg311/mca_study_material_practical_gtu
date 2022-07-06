def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    num_unq_words = 0
    with open(fname, 'r') as f:

        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if (i != " " and i != "\n"):
                        num_charc += 1

    with open(fname, 'r') as text:
        print('Number of unique short words in text file: ', sum(word.istitle() for row in text for word in row))

    print("Number of words in text file: ", num_words)
    print("Number of lines in text file: ", num_lines)
    print('Number of characters in text file: ', num_charc)
    print('Number of spaces in text file: ', num_spaces)

    test_str = "The country's foreign exchange reserves surged by USD 9.427 billion to record high of USD 620.576 billion in the week ended July 30, according to the latest RBI data. In the previous week ended July 23, the reserves had declined by USD 1.581 billion to USD 611.149 billion. In the reporting week ended July 30, the rise in the reserves was on the back of an increase in foreign currency assets (FCAs), a major component of the overall reserves, the Reserve Bank of India's (RBI) weekly data released on Friday showed. FCA increased by USD 8.596 billion to USD 576.224 billion in the reporting week. Expressed in dollar terms, the foreign currency assets include the effect of appreciation or depreciation of non-US units like the euro, pound and yen held in the foreign exchange reserves. Gold reserves were up by USD 760 million to USD 37.644 billion in the reporting week, the data showed. The special drawing rights (SDRs) with the International Monetary Fund (IMF) rose by USD 6 million at USD 1.552 billion. The country's reserve position with the IMF also increased USD 65 million to USD 5.156 billion in the reporting week, the data showed."
    print("The original string is : " + str(test_str))
    res = ''.join(format(ord(i), '08b') for i in test_str)
    print("The string after binary conversion : " + str(res))
    fname = input("Enter file name: ")
    print("\n Numbers are as follows:")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if (letter.isdigit()):
                        print(letter)

    print("\n Date as follow")
    import re
    f = open("file1.txt", "r")

    content = f.read()

    pattern = "\d{2}[/-]\d{2}[/-]\d{4}"

    dates = re.findall(pattern, content)
    for date in dates:
        if "-" in date:
            day, month, year = map(int, date.split("-"))
        else:
            day, month, year = map(int, date.split("/"))
        if 1 <= day <= 31 and 1 <= month <= 12:
            print(date)
    f.close()

    count = 0
    l1 = []
    x = open('file1.txt', 'r')
    y = open('file2.txt', 'a')
    for item in x.read():
        if item not in l1:
            count += 1
            l1.append(item)
    y.write("\nNumber of unique Pattern : " + str(count))
    y.close()

    file = open('file1.txt', 'r')
    file2 = open('file2.txt', 'a')
    for line in file:
        asc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        new = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'a', 'b', 'c', 'd', 'e']
        line = line.lower()
        line = list(line)
        for x in range(len(line)):
            if line[x] not in asc:
                continue
            ch = asc.index(line[x])
            line[x] = new[ch]
        newstr = ''
        for i in line:
            newstr += i
        print('\n\nReplace Every Character a-z by a-f:\n', newstr)
        file2.write(newstr)

if __name__ == '__main__':
    fname = 'file1.txt'
    try:
        counter(fname)
    except:
        print('File not found')