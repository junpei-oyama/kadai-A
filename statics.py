def sum_calc(sum_list):
    sum_ans = 0
    for i in sum_list:
        sum_ans += i
    print(f'合計値：{sum_ans}')


def max_calc(max_list):
    max_tmp = max_list[0]
    for i in max_list:
        if max_tmp < i:
            max_tmp = i
    print(f'最大値：{max_tmp}')


def min_calc(min_list):
    min_tmp = min_list[0]
    for i in min_list:
        if min_tmp > i:
            min_tmp = i
    print(f'最小値：{min_tmp}')


def ave_calc(ave_list):
    ave_tmp = 0
    for i in ave_list:
        ave_tmp += i
    ave_ans = ave_tmp // len(ave_list)
    print(f'平均値：{ave_ans}')


def main():
    nums = input("データを入力してください(スペース区切り) -> ")
    num_list = list(map(int, nums.split(' ')))

    sum_calc(num_list)

    max_calc(num_list)

    min_calc(num_list)

    ave_calc(num_list)


if __name__ == '__main__':
    main()
