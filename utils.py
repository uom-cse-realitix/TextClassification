import numpy as np

speech_commands_file = open("data/speech_commands.txt", "r")
words_file = open("data/words.txt", "r")

command_classes = {'count': 0, 'color': 1, 'focus': 2, 'no_op': 3}

speech_commands = speech_commands_file.read().split('\n')[:-1]
words = words_file.read().split('\n')[:-1]

input_x = np.array([]).reshape(0, 16)
input_y = np.array([]).reshape(0, 4)
input_x_test = np.array([]).reshape(0, 16)
input_y_test = np.array([]).reshape(0, 4)


def create_array(phrase):
    command = phrase.split('|')
    bin_val = '0b'
    for i in range(len(words)):
        bin_val += str((1, 0)[command[1].rfind(words[i]) == -1])

    return [int(bin_val, 2), command_classes[command[0]]]