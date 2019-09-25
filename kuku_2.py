def main():
    rows = int(input('行数の入力 -> '))
    cols = int(input('列数の入力 -> '))

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(f'{i * j} ', end='')
        print()


if __name__ == '__main__':
    main()
