import csv
import random
import time

WORDLIST_PATH = "words_list.csv"


class WordTypingTest:

    def __init__(self, words: int):
        """
        Class initialization
        :param words: Quantity of words for the test
        """
        self.words_per_min = 0
        self.char_per_min = 0
        self.start_time = 0
        self.current_time = 0
        self.elapsed_time = 0
        self.correct_words = 0
        self.typed_text = ""
        self.words_qtd = words
        self.words_list = get_words_list(words)

    def start_test(self) -> None:
        """
        Reinitialize the test with the same word quantity as configured previously
        """
        self.__init__(self.words_qtd)
        self.start_time = time.time()

    def register_new_char(self, text: str) -> bool:
        """
        Registers the new character and calculates test metrics
        :rtype: True if test is finished
        """
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
        self.calculate_metrics(correct_chars, correct_words)
        return self.is_complete(input_list)

    def calculate_metrics(self, correct_chars: int, correct_words: int) -> None:
        """
        Calculates the test metrics and stores them in internal variables
        :param correct_chars: Integer representing the correct words char count
        :param correct_words: Integer representing the correct words
        """
        self.char_per_min = correct_chars / (self.elapsed_time / 60)
        self.words_per_min = correct_words / (self.elapsed_time / 60)
        self.correct_words = correct_words

    def is_complete(self, input_words: [str]) -> bool:
        """
        Verifies if the test is completed
        :param input_words: List of input words
        :return: True if test ended
        """
        if len(input_words) == len(self.words_list):
            return True
        else:
            return False


def get_words_list(words: int) -> [str]:
    """
    Reads database of english words and filters the words with 4 and 5 chars
    :param words: Integer of the number of words for the test
    :return: Returns a list of n words randomly selected from the database
    """
    with open(WORDLIST_PATH, "r") as file:
        reader = csv.reader(file)
        words_list = [item[0] for item in reader if 6 > len(item[0]) > 3]
    word_for_test = random.sample(words_list, words)
    return word_for_test
