#!/usr/bin/env python
"""Contains menu class and related code"""


class Menu:
    """
    Menu class

    Selections are dynamically made. Recommend last selection be a quit.

    __init__(self, title, *choices)

    display(self)
        returns a string containing the menu

    get_choice(self)
        Gets and returns a choice based on the number of available selections.
    """

    def __init__(self, title, *choices):
        self._title = title
        self._choices = choices
        self._choice_num = len(self._choices)

    def display(self):
        """Returns constructed menu string"""
        display_str = "{T}\n".format(T=self._title)
        for idx, line in enumerate(self._choices, start=1):
            display_str = "{D}{I})  {L}\n".format(D=display_str, I=idx, L=line)
        return display_str

    def get_choice(self):
        """Menus have choices, and a valid choice is returned if entered"""
        while True:
            try:
                usr_choice = input("\n: ")
                choice = int(usr_choice)
            except ValueError:
                print("\nInvalid input, must enter a number")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\nQuiting...")
                choice = self._choice_num
            if choice > self._choice_num or choice < 1:
                print("\nInvalid input, must enter a number corresonding to a"
                      " menu choice")
                continue
            break
        return choice


if __name__ == "__main__":
    pass
