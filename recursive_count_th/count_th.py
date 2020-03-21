'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counted = 0


def count_th(word):
    global counted
    counted = 0
    th = "th"

    def num_of_times(word, th):
        global counted
        into_array = list(word)
        if len(into_array) >= 2:
            to_check = into_array[0] + into_array[1]
            if th in to_check:
                counted += 1
            sub_array = into_array[1:]
            return num_of_times(sub_array, th)
        else:
            return counted

    counted = num_of_times(word, th)
    print(counted)
    return counted


count_th("thhtthht")

