def generation_big_letters():
    return [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def generation_letters():
    return [chr(i) for i in range(ord('a'), ord('z') + 1)]


def generation_numbers():
    return [chr(i) for i in range(ord('0'), ord('9') + 1)]


def generation_punctuations():
    return [',', '.', ';', ':', '!', '?', '-']
