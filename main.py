import customtkinter
import tkinter
import keyboard

from wordtypingtest import WordTypingTest

words_per_min = 0
test_time = 0

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Typing Speed Test")
app.geometry("500x550")

typing_test = WordTypingTest()
word_for_test = ""


def button_function():
    typing_test.start_test()
    wordsLabel.configure(text=typing_test.words_list)
    entryTest.delete(0, "end")


def detect_key_press(event):
    if keyboard.read_key():
        typing_test.register_new_char(entryTest.get())
        time_label.configure(text=f"Elapsed time: {int(typing_test.elapsed_time)}")
        result_word_label.configure(text=f"Words per min: {int(typing_test.words_per_min)}")
        result_char_label.configure(text=f"Char. per min: {int(typing_test.char_per_min)}")


wordsLabel = customtkinter.CTkLabel(master=app, text=word_for_test, wraplength=500, text_font=("arial.ttf", 12))
wordsLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Start / Restart", command=button_function)
button.grid(row=1, column=1, padx=10, pady=10)

entryTest = customtkinter.CTkEntry(app, width=480, height=200, text_font=("arial.ttf", 12))
entryTest.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

time_label = customtkinter.CTkLabel(master=app, text=f"Elapsed time: ", wraplength=500, text_font=("arial.ttf", 8))
time_label.grid(row=3, column=0)
result_word_label = customtkinter.CTkLabel(master=app, text=f"Words per min: ", wraplength=500,
                                           text_font=("arial.ttf", 8))
result_word_label.grid(row=3, column=1)
result_char_label = customtkinter.CTkLabel(master=app, text=f"Char. per min: ", wraplength=500,
                                           text_font=("arial.ttf", 8))
result_char_label.grid(row=3, column=2)

app.bind("<Key>", detect_key_press)
app.mainloop()
