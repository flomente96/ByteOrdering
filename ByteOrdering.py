

class ByteOrdering:
    # Reads the file and return the content
    def read(self):
        temp = open("input.in", 'r').read().split('\n')
        print("Temp: ")
        print(temp)
        return temp

    # Print the data
    @staticmethod
    def print_data(data):
        data = list(data)
        string = ""
        for letter in data:
            string += letter + "   "
        print(string)

    def store_string(self, data, tobigendian):
        data = self.add_zeros(data)
        data_list = self.to_4byte(data, False)

        for index in data_list:
            if tobigendian is True:
                self.print_data(index)
            else:
                self.print_data(index[::-1])

    def store_integer(self, data):
        data_list = self.to_4byte(data, True)
        self.print_data(data_list)

    def add_zeros(self, data):
        ctr = 0
        while ctr < len(data) % 4 != 0:
            data += "0"
            ctr += 1
        return data

    def to_4byte(self, data, isinteger):
        start = 0
        end = 0
        data_array = []
        if isinteger is False:
            while end < len(data):
                end = start + 4
                byte_string = data[start:end:]
                data_array.append(byte_string)
                start = end
        else:
            n = 8
            data_array = [data[index: index + n] for index in range(0, len(data), n)]
            self.parse(data_array)
        return data_array

    def parse(self, binary_array):
        for i in range(len(binary_array)):
            binary_array[i] = str(int(binary_array[i], 2))


b = ByteOrdering()
text_data = b.read()
print("BIG ENDIAN FORMAT")
for line in text_data:
    if line.isdigit() is False:
        b.store_string(line, True)
    else:
        digit = int(line)
        binary_str = "{0:032b}".format(digit)
        b.store_integer(binary_str)

print("LITTLE ENDIAN FORMAT")
for line in text_data:
    if line.isdigit() is False:
        b.store_string(line, False)
    else:
        digit = int(line)
        binary_str = "{0:032b}".format(digit)
        b.store_integer(binary_str)
