def is_isbn_or_key(word):
    """
    确定是isbn还是关键字
    isbn13 13个0到9的数字组成
    isbn10 10个0到9数字组成,含有一些' - '
    """
    global short_word
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
        short_word = word.replace('-', '')
    if '_' in word and len(short_word) == 10 and short_word.isdigit():
        # 把大概率为假的条件放前面,耗时的操作放在后面
        isbn_or_key = 'isbn'
    return isbn_or_key

