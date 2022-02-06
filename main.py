from random import randint

def main():
    quit = ""

    word = ['Vintage', 'Music', 'LP', 'Vinyl', 'record', 'Phonograph', 'Art', 'Lover', 'DJ', 'Retro']

    while quit != "q":

        list1 = word[randint(0, len(word) - 1)]
        list2 = word[randint(0, len(word) - 1)]
        list3 = word[randint(0, len(word) - 1)]
        list4 = word[randint(0, len(word) - 1)]
        list5 = word[randint(0, len(word) - 1)]
        list6 = word[randint(0, len(word) - 1)]
        list7 = word[randint(0, len(word) - 1)]
        list8 = word[randint(0, len(word) - 1)]

        final = list1 + " " + list2 + " " + list3 + " " + list4 + " " + list5 + " " + list6 + " " + list7 + " " + list8
        if 50 < len(final) < 61 :
            print(final)
            input()
            quit = input("enter q to quit")
            if quit == "q":
                break

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
