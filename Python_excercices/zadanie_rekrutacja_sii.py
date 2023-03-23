liczby_losowe = [x for x in range(2)]


class Dom:

    # def __init__(self):

    @staticmethod
    def print_numbers():
        return liczby_losowe

    def xx(self):
        try:
            assert 2+2==5
        except:
            raise ValueError('')

    @staticmethod
    def for_loop(self):
        lst = []
        for x in range(10):
            if x % 2 == 0:
                lst.append(x)
            else:
                raise ValueError('Zle')
        return lst

    @staticmethod
    def open_write_file():
        with open('plik2.txt', 'w+') as file1:
            file1.write(str(liczby_losowe))

    @staticmethod
    def read_from_file():
        with open('plik.txt', 'r') as file:
            return file.read()


d = Dom()
print(d.open_write_file())
print(d.read_from_file())