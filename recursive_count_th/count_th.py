'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    counted = 0

    def num_of_times(word, th):
        into_array = list(word)
        if len(into_array) > 1:
            to_check = into_array[0] + into_array[1]
            if th in to_check:
                counted += 1

            sub_array = into_array[1:]
            return num_of_times(sub_array, th)

        else:
            pass

    return counted


count_th("Fire")
