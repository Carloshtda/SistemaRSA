class InputTreatment:
    def __init__(self):
        self.input = 0

    def boolean_input(self):
        while True:
            print("Input True or False:")
            try:
                self.input = input()
                if self.input.lower() == 'true':
                    self.input = True
                    break
                if self.input.lower() == 'false':
                    self.input = False
                    break
                raise ValueError
            except ValueError:
                print('Wrong Input! Try Again.')
        return self.input

    def message_input(self):
        while True:
            print("(Please use only lower case letters and numbers)")
            try:
                self.input = input()
                for i in range(len(self.input)):
                    numerical_represent = ord(self.input[i])
                    if not (97 <= numerical_represent <= 122 or numerical_represent == 32 or 48 <= numerical_represent <= 57):
                        raise ValueError
                break
            except ValueError:
                print('Input not supported! Try Again.')
        return self.input

    def limited_int_input(self, bottom_lim, upper_lim):
        while True:
            print("Input a integer between {} and {}:".format(bottom_lim, upper_lim))
            try:
                self.input = int(input())
                if not(bottom_lim <= self.input <= upper_lim):
                    raise ValueError
                break
            except ValueError:
                print('Input not supported! Try Again.')
        return self.input

