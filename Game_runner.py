####################################
# FILE : game_runner.py
# WRITER1 : Alon Ben David , abenda93 , 311218861
# WRITER2 : Gilad Sagi Fridman   , gilad97 , 319133526
# EXERCISE : intro2cs ex12 2019-2020
# DESCRIPTION: makes the screen and games graphic, make stopwatch class
########################################

import tkinter as tk
import tkinter.messagebox
from boggle import *
import time
import datetime


class Stopwatch:
    """
    the class start counting time from the moment its made, and can returns the time have left
    to the time limit as int of second or as string as a watch
    """
    TIME_LIMIT = 180   # 3 min to play

    def __init__(self):
        self.current_time = 0
        self.start_time = None
        self.run = True

    def start_game(self):
        """
        start counting time when class is made
        """
        self.start_time = time.time()

    def get_current_time(self):
        """
        change the current time to the time has left in sec and return it as int
        """
        if self.run is False:
            return self.TIME_LIMIT
        current_time = time.time() - self.start_time
        self.current_time = int(self.TIME_LIMIT - current_time)
        time.sleep(1)
        if self.current_time <= 0:
            return 0
        return self.current_time

    def str_time(self):
        """
        return the time has left in str min:sec format
        """
        str_time = str(datetime.timedelta(seconds=self.get_current_time()))
        str_time = str_time[-5:]
        return str_time


class Screen:

    def __init__(self, game):
        # for screen
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.title("Boggle! :)")
        self.root.geometry('550x500')

        # for game
        self.buttons_coordinates = []
        self.game = game
        self.stopwatch = Stopwatch()
        self.count = 0

        # index to dictionary
        self.NUM_TO_COOR = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
                            8: (2, 0),
                            9: (2, 1), 10: (2, 2), 11: (2, 3), 12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)}

    def graphics(self):
        """
        makes the graphics of game and add it to screen
        """
        frame = tk.Frame()
        frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # making buttons on screen
        self.print_buttons()

        # score label
        self.score_event(frame)

        # stopwatch
        self.stopwatch_event(frame)

        # letters been chosen
        self.chosen_letters_event(frame)

        # correct words list
        self.chosen_words_event(frame)

        # check word
        self.check_word_event()

        # end game button
        self.quit_button_event(frame)

    def quit_button_event(self, frame):
        """
        print quit button on screen
        """
        quitButton = tk.Button(frame, text="Quit", bg="red", command=self.handle_exit)
        quitButton.pack()
        self.root.update()

    def check_word_event(self):
        """
        print the check word button on screen
        """
        check_word = tk.Button(self.root, font=(None, 10), text="check", command=lambda: self.check_button_event(),
                               width=15, bg="green")
        check_word.pack()
        check_word.place(x=150, y=400)

    def chosen_words_event(self, frame):
        """
        print the correct words the player a chived
        """
        self.chosen_words = tk.StringVar()
        self.chosen_words.set("")
        chosen_wordsTitle = tk.Label(frame, text="words")
        chosen_wordsTitle.pack()
        wordsFrame = tk.Frame(frame, height=5, bd=1, \
                              relief=tk.SUNKEN)
        wordsFrame.pack()
        words = tk.Label(wordsFrame, height=10, width=20, \
                         textvariable=self.chosen_words, fg="green", bg="white")
        words.pack()

    def stopwatch_event(self, frame):
        """
        print the stop watch on screen
        """
        self.stop_watch = tk.StringVar()
        self.stop_watch.set('03:00')
        watchTitle = tk.Label(frame, text="Stopwatch")
        watchTitle.pack()
        watchFrame = tk.Frame(frame, height=2, bd=1, \
                              relief=tk.SUNKEN)
        watchFrame.pack()
        self.watch = tk.Label(watchFrame, height=2, width=20, \
                         textvariable=self.stop_watch, fg="Yellow", bg="black")
        self.watch.pack()

    def chosen_letters_event(self, frame):
        """
        print on screen the letters been chosen
        """
        self.letters = tk.StringVar()
        self.letters.set('')
        lettersTitle = tk.Label(frame, text="Word")
        lettersTitle.pack()
        lettersFrame = tk.Frame(frame, height=2, bd=1, \
                                relief=tk.SUNKEN)
        lettersFrame.pack()
        letter = tk.Label(lettersFrame, height=2, width=20, \
                          textvariable=self.letters, fg="blue", bg="white")
        letter.pack()

    def score_event(self, frame):
        """
        print the score in screen
        """
        self.score_val = tk.StringVar()
        self.score_val.set('0')
        scoreTitle = tk.Label(frame, text="Score")
        scoreTitle.pack()
        scoreFrame = tk.Frame(frame, height=2, bd=1, \
                              relief=tk.SUNKEN)
        scoreFrame.pack()
        score = tk.Label(scoreFrame, height=2, width=20, \
                         textvariable=self.score_val, fg="blue", bg="white")
        score.pack()

    def set_coordinate(self, coordinate):
        """
        changing pushed_coordinate value
        """
        self.pushed_coordinate = coordinate
        return

    def get_coordinate(self):
        """
        return True if pushed_coordinate is full, false if not
        """
        if self.pushed_coordinate is None:
            return False
        return True

    def set_choosed_letters(self, letters):
        """
        change the letters been choose so far on the screen
        :param letters: str of letters
        """
        self.letters.set(letters)
        return

    def handle_exit(self):
        """
        if pressed quit button. end game
        lets the user choose between playing again or quiting
        """
        self.stopwatch.run = False
        self.frame_exit = tk.Tk()
        self.frame_exit.geometry('200x200')
        play_again_q = tk.Label(self.frame_exit, text="would you like to play again?")
        play_again_q.pack()
        exit_button = tk.Button(self.frame_exit, text="no", command=self.should_end,bg= "red")
        exit_button.pack(side=tk.LEFT)
        play_button = tk.Button(self.frame_exit, text="yes", command=self.play_again,bg = "green")
        play_button.pack(side=tk.RIGHT)

    def play_again(self):
        """
        restart game when player choose to
        """
        self.frame_exit.destroy()
        self.root.destroy()
        self.root.quit()
        main()

    def should_end(self):
        """
        :returns: True if the game should end or not (if "q" was pressed or not)
        """
        self.frame_exit.destroy()
        self.print_message(title="exit", message="the user quit")
        self.root.destroy()
        self.root.quit()

    def set_score(self, val):
        """
        Sets the current game score
        :param val: The game score
        :type val: int
        """
        self.score_val.set(str(val))

    def set_chosen_words(self, words_list):
        """
        Sets the current words_been chosen
        :param words_list: list of string of words been chosen
        """
        string = "\n".join(words_list)
        self.chosen_words.set(str(string))

    def set_stopwatch(self, time_left):
        """
        set the current time left in grafic
        :param time_left: str of time that has left in min:sec format
        """
        self.stop_watch.set(time_left)

    def print_buttons(self):
        """
        print letters button on screen and save them in self.buttons_coordinates list
        """
        for i in range(16):
            button = tk.Button(self.root, bg="blue", text=self.game.board.coordinate_to_letter(self.NUM_TO_COOR.get(i)),
                               font=(None, 30), command=lambda i=i: self.callback(i))
            button.pack()
            button.place(x=self.NUM_TO_COOR.get(i)[1] * 100, y=self.NUM_TO_COOR.get(i)[0] * 100)
            self.buttons_coordinates.append(button)

    def callback(self, i_coordinate):
        """
        return coordinate if button been pushed
        """
        coordinate = self.NUM_TO_COOR[i_coordinate]
        if self.game.choose_letter(self.game.chosen_coordinates, coordinate):
            # check if coordinate is valid, if it is- update
            self.game.chosen_coordinates.append(coordinate)
            self.game.word += self.game.board.coordinate_to_letter(coordinate)
            self.set_choosed_letters(self.game.word)
            self.change_color(i_coordinate)
        else:
            self.print_message(title="error", message=self.game.INVALID_LETTER)
        return

    def set_correct_words(self, correct_words):
        """
        update the score
        """
        self.correct_words_list = correct_words

    def print_message(self, title, message):
        """
        print message on screen
        """
        tkinter.messagebox.showinfo(str(title), str(message))

    def clock_event(self):
        """
        print time on screen and manage when time is up
        """
        timer = self.stopwatch.str_time()
        self.set_stopwatch(timer)
        self.count += 1      # counter

        # check if time is up, go to handle exit
        if timer == "00:00":
            self.print_message(title="error", message=self.game.TIMES_UP)
            self.handle_exit()

        # change frame to red in last 10 sec
        if self.count >= self.stopwatch.TIME_LIMIT - 15:
            self.watch.configure(bg="red", fg="black")

        if self.stopwatch.run:
            # check if game is still on
            self.root.after(200, self.clock_event)

    def check_button_event(self):
        """
        handle when check button is pressed,
        if word is valid, add to list, and update word
        if not, print message to screen
        reset letters and buttons
        """
        if self.game.check_word(self.game.word):
            if self.game.word not in self.game.chosen_words:
                # if word is valid
                self.game.update_score(self.game.word)
                self.game.chosen_words.append(self.game.word)
                self.set_chosen_words(self.game.chosen_words)
                self.set_score(self.game.get_score())
            else:
                self.print_message(title="error", message=self.game.CHOOSE_TWICE)
        else:
            # if word not valid
            self.print_message(title="error", message=self.game.INVALID_WORD)
        # reset word and chosen coordinate list
        self.game.word = ''
        self.set_choosed_letters(self.game.word)
        self.game.chosen_coordinates = []
        self.buttons_coordinates = []
        self.print_buttons()

    def start(self):
        """
        print start button at the start of game
        """
        self.start_button = tk.Button(self.root, text='start', command=self.start_event, bg="green")
        self.start_button.pack()
        self.root.mainloop()

    def start_event(self):
        """
        start game when player is ready
        """
        self.start_button.destroy()
        self.stopwatch.start_game()
        self.game_loop()

    def change_color(self, i_coordinate):
        """
        change color of letter to red when one is pressed
        """
        self.buttons_coordinates[i_coordinate].configure(bg="red")

    def game_loop(self):
        """
        runs the main loop of the game
        """
        self.graphics()
        self.clock_event()
        self.root.mainloop()


def main():
    """
    the main func that make board, screen and call to star
    """
    game = Game('boggle_dict.txt')
    screen = Screen(game)
    screen.start()


if __name__ == '__main__':
    main()
