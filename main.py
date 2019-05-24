import numpy as np

speech_commands_file = open("data/speech_commands.txt", "r")
words_file = open("data/words.txt", "r")

command_classes = {'count': 0, 'color': 1, 'focus': 2, 'no_op': 3}

speech_commands = speech_commands_file.read().split('\n')[:-1]
words = words_file.read().split('\n')[:-1]


input_x = np.array([]).reshape(0, 16)
input_y = np.array([]).reshape(0, 4)


def create_array(phrase):
    command = phrase.split('|')
    bin_val = '0b'
    for i in range(len(words)):
        bin_val += str((1, 0)[command[1].rfind(words[i]) == -1])

    return [int(bin_val, 2), command_classes[command[0]]]


ground_truth = [create_array(speech_command) for speech_command in speech_commands]
input_array = [[i, 3] for i in range(0, 65535)]

for i in ground_truth:
    input_array[i[0]][1] = i[1]

del ground_truth

for i in input_array:
    word_vector = [int(j) for j in format(i[0], '#018b').replace('0b', '')]
    labels = np.array([[0, 0, 0, 0]])
    labels[0][i[1]] = 1
    input_x = np.concatenate((input_x, np.array([word_vector])), axis=0)
    input_y = np.concatenate((input_y, labels), axis=0)

np.savetxt("data/input_x.csv", input_x)
np.savetxt("data/input_y.csv", input_y)


# def create_array(phrase):
#     command = phrase.split('|')
#     array = []
#     for i in range(len(words)):
#         array.append((1, 0)[command[1].rfind(words[i]) == -1])
#
#     labels = np.array([[0, 0, 0, 0]])
#     labels[0][command_classes[command[0]]] = 1
#     array = np.array([array])
#     return array, labels
#
#
# for speech_command in speech_commands:
#     word_vector, labels = create_array(speech_command)
#     input_x = np.concatenate((input_x, word_vector), axis=0)
#     input_y = np.concatenate((input_y, labels), axis=0)
#
# print((input_x, input_y))
