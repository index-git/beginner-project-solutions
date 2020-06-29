
def bubble_sort(original_list):
    sorted_list = list(original_list)
    number_len = len(sorted_list)
    changes_cnt = 0
    comparisons_cnt = 0
    for i in range(0, number_len):
        was_change = False
        for j in range(0, number_len - 1):
            comparisons_cnt += 1
            if sorted_list[j] > sorted_list[j + 1]:
                was_change = True
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                changes_cnt += 1
        if not was_change:
            break
    return {"sorted_list": sorted_list, "comparisons_cnt": comparisons_cnt, "changes_cnt": changes_cnt}


numbers = [58, 14, 92, 27, 62, 19, 7, 66]

if __name__ == "__main__":
    print(numbers)
    bsorted_list = bubble_sort(numbers)
    print(numbers)
    print(bsorted_list["sorted_list"])
    print(bsorted_list["comparisons_cnt"])
    print(bsorted_list["changes_cnt"])

# TODO měření času, počtu porovnání, počtu výměn
