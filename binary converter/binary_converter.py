# Binary Converter
import string
class BinConverter():
    # Dictionaries
#     import string
#     letter_dict = {each_print: bin(ord(each_print) + 256)[2:] for each_print in string.printable}
#     binary_dict = {value: key for key, value in letter_dict.items()}
    
    def __init__(self):
        self.letter_dict = {each_print: bin(ord(each_print) + 256)[2:] for each_print in string.printable}
        self.binary_dict = {value: key for key, value in letter_dict.items()}

    def dictionary(self):
        """This displays the dictionay used to converts string inputs into binary outputs
        """
        for key, value in self.letter_dict.items():
            print('{} -> {}'.format(key, value))

    def encrypt(self, message):
        """This converts an alpha-numeric string into a binary output based on the binary dictionary in the script
        """
        bin_temp = [self.letter_dict[each_letter] for each_letter in message]
        return ''.join(bin_temp)

    def decrypt(self, message):
        """This converts a binary output into the alpha-numeric string equivalent based on the binary dictionary in the script
        """
        char_count = int(len(message) / 9)
        current_count = 1
        binary_length = 9
        temp = []
        for _ in range(1, char_count + 1):
            temp.append(self.binary_dict[message[((current_count * binary_length) - binary_length):(current_count * binary_length)]])
            current_count += 1
        return ''.join(temp)

    def convert():
        """this is the main converter where you can convert from text to binary (enter '1') or from binary to text (enter '2')
        """
        print('''*********************************************\nWelcome to the binary converter.\nThis converts your text into binary code and the binary output back to text.\n''')
        confirm = (input('''Would you like to:\n1. Convert text to binary (enter -> 1 or \'text\') or \n2. Convert binary to text (enter -> 2 or \'binary\')\n> ''')).lower()
        if confirm == '1' or confirm == 'text' or confirm == 't' or confirm[0] == 't':
            message = input('Please enter the text message you would like to convert to binary?\n> ')
            print(self.encrypt(message))
        elif confirm == '2' or confirm == 'binary' or confirm == 'b' or confirm[0] == 'b':
            message = input('Please enter the binary message you would like to convert to text\n> ')
            print(self.decrypt(message))
        else:
            print('*********************************************\nPlease enter:\n1 to convert to binary\tor\n2 to convert to text')
            self.convert()

