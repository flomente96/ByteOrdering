import numpy


class ByteOrdering:
    big_matrix = []
    little_matrix = []

    # Reads the file and return the content
    def read(self):
        temp = open("input.in", 'r').read().split('\n')
        print("Temp: ")
        print(temp)
        return temp

    # Print the data
    def print_data(self, data):
        data = list(data)
        string = ""
        for letter in data:
            string += letter + "   "
        print(string)

    def to_big(self, data):
        data = self.add_zeros(data)
        self.big_matrix = self.to_4byte(data)
        for index in self.big_matrix:
            self.print_data(index)

    def to_little(self, data):
        data = self.add_zeros(data)
        self.little_matrix = self.to_4byte(data)
        for index in self.little_matrix:
            self.print_data(index[::-1])

    def add_zeros(self, data):
        ctr = 0
        while ctr < len(data) % 4 != 0:
            data += "0"
            ctr += 1
        return data

    def to_4byte(self, data):
        start = 0
        end = 0
        data_array = []
        while end < len(data):
            end = start + 4
            byte_string = data[start:end:]
            data_array.append(byte_string)
            start = end
        print(data_array)
        return data_array


b = ByteOrdering()
text_data = b.read()
print("BIG ENDIAN FORMAT")
for line in text_data:
    b.to_big(line)

print("LITTLE ENDIAN FORMAT")
for line in text_data:
    b.to_little(line)