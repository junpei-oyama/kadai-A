import random


def main():
    dice_num = int(input('サイコロの面の数は？ -> '))
    try_num = int(input('何回振りますか？ -> '))

    result_list = []
    for i in range(try_num):
        result_list.append(random.randint(1, dice_num))

    print(result_list)


if __name__ == '__main__':
    main()
