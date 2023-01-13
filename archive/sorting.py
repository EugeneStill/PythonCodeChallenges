import random


def bubble_sort(items):
    """ Implementation of bubble sort: push highest value to end of list """
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def insertion_sort(items):
    """ Implementation of insertion sort, sorts list in place """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1


def string_sort():
    s = input("Enter a string:")
    m = sorted(s)
    i = ''.join(m)
    print(i)


def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    print(str)


def reverse_word_sentence(sentence):
    words = sentence.split(" ")
    new_words = [word[::-1] for word in words]
    new_sentence = " ".join(new_words)
    print(new_sentence)


random_items = [random.randint(-50, 100) for c in range(32)]
print("Before : {}".format(random_items))
bubble_sort(random_items)
print("After : {}".format(random_items))

random_items = [random.randint(-50, 100) for c in range(32)]
print("Before : {}".format(random_items))
insertion_sort(random_items)
print("After : {}".format(random_items))

string_sort()
reverse_word_sentence("I need to go to the store this morning.")
reverse_string("Jimmy")