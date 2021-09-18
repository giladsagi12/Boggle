####################################
# FILE : boggle.py
# WRITER1 : Alon Ben David , abenda93 , 311218861
# WRITER2 : Gilad Sagi Fridman   , gilad97 , 319133526
# EXERCISE : intro2cs ex12 2019-2020
# DESCRIPTION: makes the ground rules of boggle game
########################################

import boggle_board_randomizer


class Board:
    """
       make board class, list of list of letters
    """

    def __init__(self):
        self.board = boggle_board_randomizer.randomize_board()

    COL_ROW_LIMIT = 4

    def board_coordinates(self):
        """
        return a list of list of the boards rows coordinate
        """
        coordinate_list = []
        for row in range(self.COL_ROW_LIMIT):
            temp_row = []
            for col in range(self.COL_ROW_LIMIT):
                temp_row.append((row, col))
            coordinate_list.append(temp_row)
        return coordinate_list

    def coordinate_to_letter(self, coordinate):
        """returns the letter of the given coordinate on board"""
        return self.board[coordinate[0]][coordinate[1]]

    def __str__(self):
        string_board = ''
        for row in self.board:
            for letter in row:
                string_board += letter + " "
            string_board += '\n'
        return string_board


class Game:
    """
    makes the logical rule of game
    """
    ROW = 0
    COL = 1
    INVALID_LETTER = " you cant pick that, plz try again"
    INVALID_WORD = " this word does not exist in our dictionary :( "
    CHOOSE_TWICE = " you have already chose this word "
    TIMES_UP = "your time is up! "

    def __init__(self, word_file, score=0):
        self.score = score
        self.board = Board()
        self.words_dict = self.make_words_dictionary(word_file)

        # for loop game
        self.coordinate = ''
        self.chosen_coordinates = []
        self.chosen_words = []
        self.word = ''

    def get_score(self):
        """
        returns the score value
        """
        return self.score

    def update_score(self, word):
        """
        update the score value
        """
        self.score += len(word) ** 2

    def make_words_dictionary(self, file_name):
        """
        get file txt of words and make it a list of string
        :return: list of string with all the valid words
        """
        with open(file_name) as data_file:
            words_dict = set()
            for line in data_file:
                words_dict.add(line.strip())
        return words_dict

    def get_word_list(self):
        """
        return the valid words list
        """
        return self.words_dict

    def choose_letter(self, chosen_coordinates_lst, coordinate=()):
        """ this function gets a coordinate of a chosen letter from the board,
         and a list of chosen letters, and checks if the letter is valid to be chosen.
         Return True if valid, else False"""
        letter_valid = True
        if chosen_coordinates_lst:
            # check if list is not empty
            current_coordinate = chosen_coordinates_lst[-1]
            if (abs(current_coordinate[0] - coordinate[0]) <= 1
                and abs(current_coordinate[1] - coordinate[1] <= 1)) \
                    and coordinate not in chosen_coordinates_lst:
                # if coordinate is valid
                letter_valid = True
            else:
                # letter not valid, print a message
                letter_valid = None
        return letter_valid

    def chosen_list(self, coordinate):
        """ This function lets the user choose coordinates(letters) checks if valid( with choose_letter()), and if so,
         updates the list with the new coordinate """
        chosen_coordinates_lst = []
        if self.choose_letter(coordinate, chosen_coordinates_lst) is True:
            chosen_coordinates_lst.append(coordinate)

    def check_word(self, word):
        """
        check if word is in the valid words_list
        :return: True if word is valid, False otherwise
        """
        if word in self.get_word_list():
            return True
        return False

