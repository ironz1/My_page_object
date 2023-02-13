from selenium.webdriver.support.wait import WebDriverWait

class OldPage:
    def __init__(self, i, n):
        self.id = i
        self.name = n
        print(f'taki tam argument {i}')


class NewPage(OldPage):
    def __init__(self, a, b, i, n):
        super().__init__(i, n)
        self.field = a
        self.text = b
        # self._wait = WebDriverWait()



d = OldPage(i=2, n='Jęczy 2')
print(f'ID = {d.id} and NAME = {d.name}')

newpage = NewPage(i=23, n='Bobek', a='The', b='Tekst napisał')
print(f'{newpage.text},{newpage.field} {newpage.name} który ma id = {newpage.id}')