import random
from generation import generation_letters, generation_big_letters, generation_numbers, generation_punctuations

num_tests = 5
num_conditions = 4
necessarily = []


def check_human_understand(password):
    answer = ""
    vowels = ['a', 'e', 'y', 'u', 'i', 'o', 'A', 'E', 'Y', 'U', 'I', 'O']
    list_letters = generation_letters() + generation_big_letters()
    consonants = []
    for el in list_letters:
        if el not in vowels:
            consonants.append(el)

    numbers = []
    letters = []
    punctuatuon = []
    list_numbers = generation_numbers()
    #list_punctuatuon = generation_punctuations()

    for el in password:
        if el in list_letters:
            letters.append(el)
        elif el in list_numbers:
            numbers.append(el)
        else:
            punctuatuon.append(el)

    for i in range(len(letters) // 2):
        if letters[i] in vowels:
            letters[i] = random.choice(consonants)
        answer += letters[i]
        if letters[len(letters) // 2 + len(letters) % 2 + i] in consonants:
            letters[len(letters) // 2 + len(letters) % 2 + i] = random.choice(vowels)
        answer += letters[len(letters) // 2 + len(letters) % 2 + i]

    if len(letters) % 2 == 1:
        if letters[len(letters) // 2] in vowels:
            letters[len(letters) // 2] = random.choice(consonants)
        answer += letters[len(letters) // 2]

    for el in numbers:
        answer += el

    for el in punctuatuon:
        answer += el

    return answer


def generation_password(conditions, len_password):
    global num_tests, num_conditions, necessarily

    list_symbol = []
    list_symbol.append(generation_numbers())
    list_symbol.append(generation_big_letters())
    list_symbol.append(generation_punctuations())
    list_symbol.append(generation_letters())

    password = ""
    for el in necessarily:
        replace = random.randint(0, len(password))
        password = password[:replace] + el + password[replace:]
    for i in range(num_conditions):
        if (conditions >> 1) & 1:
            if i == 3:
                continue
            else:
                replace = random.randint(0, len(password))
                password = password[:replace] + random.choice(list_symbol[i]) + password[replace:]

    symbol = []
    for i in range(num_conditions):
        symbol += list_symbol[i]

    while len(password) < len_password:
        replace = random.randint(0, len(password))
        password = password[:replace] + random.choice(symbol) + password[replace:]

    if (conditions >> 3) & 1:
        password = check_human_understand(password)

    return password


def main():
    global num_tests, num_conditions, necessarily

    tasks = []
    necessarily = ['*', '&', '@']

    tasks.append(["может содержать цифры", "обязательно содержит цифры"])
    tasks.append(["может содержать заглавные буквы", "обязательно содержит заглавные буквы"])
    tasks.append(["может содержать знаки препинания", "обязательно содержит знаки препинания"])
    # человекочитаблильный код - чередуются гласные и согласные, затем идут цифры, а в конце знаки препинания
    tasks.append(["нечеловекочитаемый пароль", "человекочитаемый пароль"])
    tasks.append(["нет обязательных символов", "обязательные символы: "])
    for i in range(len(necessarily) - 1):
        tasks[-1][1] += necessarily[i] + ", "
    tasks[-1][1] += necessarily[-1]

    max_len_password = 16
    min_len_password = 8
    a = 0
    b = (1 << num_conditions) - 1  # 1 << n   <->     2^n
    use = [0] * (1 << (num_conditions + 1))  # 1 << n   <->     2^n
    for i in range(num_tests):
        val = b
        # val % 2 == 0 - чтобы всегда учитывались обязательные символы
        while use[val] or val % 2 == 0:
            val = random.randint(a, b)
        use[val] = 1
        val += (1 << 4)

        len_password = random.randint(min_len_password, max_len_password)
        necessarily = ['*', '&', '@']

        print(f"###Тест {i + 1}")
        print(f"длина пароля = {len_password}")
        for i in range(num_conditions + 1):
            print(tasks[i][(val >> i) & 1])
        for i in range(10):
            print(generation_password(val, len_password))
        print('-' * 16)
        print()


if __name__ == '__main__':
    main()
