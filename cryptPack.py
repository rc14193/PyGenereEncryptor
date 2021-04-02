class Vigenre_Method:
    def init(self):
        self.key = None
        self.input_text = None
        self.output_text = None

    def apply_method(self, plain_text, key, method):
        key_index = 0
        for i in range(len(plain_text)):
            plain_char = ord(plain_text[i])
            key_char = ord(key[key_index])
            if method == 'encrypt':
                output_char = ((plain_char + key_char) + 33) % 127
            else:
                output_char = ((plain_char - key_char) - 33) % 127
            plain_text[i] = str(output_char)

class One_Time_Pad:
    def init(self):
        self.key = None
        self.input_text = None
        self.output_text = None

    def apply_method(self):

            