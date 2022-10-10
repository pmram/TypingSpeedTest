import csv
import random
import time

WORDLIST_PATH = "words_list.csv"


class WordTypingTest:

    def __init__(self):
        self.words_per_min = 0
        self.char_per_min = 0
        self.start_time = 0
        self.current_time = 0
        self.elapsed_time = 0
        self.correct_words = 0
        self.typed_text = ""
        self.words_list = self.get_words_list()

    @staticmethod
    def get_words_list():
        with open(WORDLIST_PATH, "r") as file:
            reader = csv.reader(file)
            words_list = [item[0] for item in reader if 6 > len(item[0]) > 3]
        word_for_test = random.sample(words_list, 100)
        return word_for_test

    def start_test(self):
        self.__init__()
        self.start_time = time.time()

    def register_new_char(self, text: str):
        self.typed_text = text
        self.current_time = time.time()
        self.elapsed_time = self.current_time - self.start_time
        correct_chars = 0
        word_count = 0
        correct_words = 0
        input_list = text.split(" ")[0:-1]
        for word in input_list:
            if word == self.words_list[word_count]:
                correct_chars += len(word)
                correct_words += 1
            word_count += 1
        self.char_per_min = correct_chars / (self.elapsed_time / 60)
        self.words_per_min = correct_words / (self.elapsed_time / 60)
        self.correct_words = correct_words
