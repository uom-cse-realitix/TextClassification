import numpy as np

speech_commands_file = open("data/speech_commands.txt", "r")
words_file = open("data/words.txt", "r")

command_classes = {'count': 0, 'color': 1, 'focus': 2, 'no_op': 3}

speech_commands = speech_commands_file.read().split('\n')[:-1]
words = words_file.read().split('\n')[:-1]

# Arrays to store training dataset
input_x = np.array([]).reshape(0, 16)
input_y = np.array([]).reshape(0,1)

# Arrays to store test dataset
input_x_test = np.array([]).reshape(0, 16)
input_y_test = np.array([]).reshape(0,1)


# Calculate a unique decimal value for each sentence
def create_array(phrase):
    command = phrase.split('|')
    bin_val = '0b'
    for i in range(len(words)):
        bin_val += str((1, 0)[command[1].rfind(words[i]) == -1])

    return [int(bin_val, 2), command_classes[command[0]]]


# Creates an arrays of decimals for valid sentences
ground_truth = [create_array(speech_command) for speech_command in speech_commands]

# Generates an array of random decimal values between 0 to 65535
random_numbers = np.random.choice(range(0, 100), 5, replace=False)
random_numbers = np.append(random_numbers, np.random.choice(range(100, 1000), 15, replace=False))
random_numbers = np.append(random_numbers, np.random.choice(range(1000, 10000), 50, replace=False))
random_numbers = np.append(random_numbers, np.random.choice(range(10000, 65535), 30, replace=False))

# Creates an array of invalid commands
input_array = [[i, 3] for i in random_numbers]

# Populate training dataset
for i in ground_truth:
    word_vector = [int(j) for j in format(i[0], '#018b').replace('0b', '')]
    labels = np.array([[0]])
    labels[0][0] = i[1]
    input_x_test = np.concatenate((input_x_test, np.array([word_vector])), axis=0)
    input_y_test = np.concatenate((input_y_test, labels), axis=0)

# Checks whether the input arrays has valid commands
for i in range(len(input_array)):
    for j in range(len(ground_truth)):
        if input_array[i][0] == ground_truth[j][0]:
            print(input_array[i][0], ground_truth[j][0])
            input_array[i][1] = ground_truth[j][1]
            del ground_truth[j]
            break

# Combine both valid and invalid sentences
input_array = input_array + ground_truth

# Shuffle the dataset
np.random.shuffle(input_array)

# Populate test dataset
for i in input_array:
    word_vector = [int(j) for j in format(i[0], '#018b').replace('0b', '')]
    labels = np.array([[0]])
    labels[0][0] = i[1]
    input_x = np.concatenate((input_x, np.array([word_vector])), axis=0)
    input_y = np.concatenate((input_y, labels), axis=0)


# Save files
np.savetxt("data/input_x.csv", input_x)
np.savetxt("data/input_y.csv", input_y)
np.savetxt("data/input_x_test.csv", input_x_test)
np.savetxt("data/input_y_test.csv", input_y_test)
