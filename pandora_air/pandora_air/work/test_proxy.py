def get_bad_proxy():
    dict_schedule = set()  # key = (origin+dest) for hash access
    # with open("error_all_proxy.txt") as file_proxy:
    with open("error_all_proxy.txt") as file_proxy:
        for line in file_proxy:
            dict_schedule.add(line)

    return dict_schedule


def get_good_proxy():
    dict_schedule = set()  # key = (origin+dest) for hash access
    with open("good_all_proxy.txt") as file_proxy:
        for line in file_proxy:
            dict_schedule.add(line)

    return dict_schedule


bad_proxy = get_bad_proxy()
good_proxy = get_good_proxy()

sorted_bad = sorted(bad_proxy)
sorted_good = sorted(good_proxy)

print(len(bad_proxy))
print(len(good_proxy))
