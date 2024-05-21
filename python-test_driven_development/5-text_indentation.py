#!/usr/bin/python3

"""This function splits a paragraph in to sentences"""


def text_indentation(text):
    """This function prints senteces of text.

    Args:
        text (str): string containing value to be printed.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    counter = 0
    while counter < len(text) and text[counter] == ' ':
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == "\n" or text[counter] in ".?:":
            if text[counter] in ".?:":
                print("\n")
            counter += 1
            while counter < len(text) and text[counter] == ' ':
                counter += 1
            continue
        counter += 1
