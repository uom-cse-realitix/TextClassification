import numpy as np

speech_commands_file = open("data/speech_commands.txt", "r")
words_file = open("data/words.txt", "r")

command_classes = ['count', 'color', 'focus']

speech_commands = speech_commands_file.read().split('\n')[:-1]
words = words_file.read().split('\n')[:-1]
word_vectors = []


def create_array(phrase):
    command = phrase.split('|')
    array = np.array([])
    for i in range(len(words)):
        array.((1, 0)[command[1].rfind(words[i]) == -1])

    return array, command[0]


for speech_command in speech_commands:
    word_vector, command_class = create_array(speech_command)

    word_vectors.append((word_vector, 1))
    print(command_class)


