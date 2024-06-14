from prompt_toolkit.styles import Style
from http import cookiejar


class PageMaker:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"
        self.dialogStyles = Style.from_dict(
            {
                "dialog": "bg:#333333",
                "dialog frame.label": "bg:#c3c3c3 #575757",
                "dialog.body": "bg:#c3c3c3 #575757",
                "dialog shadow": "bg:#232323",
            }
        )

    @staticmethod
    def drawLine(lineLength):
        print("█" * lineLength + "\n", end = '')

    @staticmethod
    def drawEndedLine(lineLength):
        print("██" + " " * (lineLength - 4) + "██\n", end = '')

    @staticmethod
    def drawSpaces(spaceCount):
        print(" " * spaceCount, end = '')

    def drawLineWithParameters(self, lineLength, *args):
        totalEmptySpaces = lineLength - 4
        for arg in args:
            totalEmptySpaces -= len(arg)
        eachSpace = totalEmptySpaces // (len(args) + 1)
        remainingSpaces = totalEmptySpaces - eachSpace * (len(args) + 1)
        print("██", end = '')
        for arg in args:
            if remainingSpaces > 0:
                self.drawSpaces(eachSpace + 1)
                remainingSpaces -= 1
            else:
                self.drawSpaces(eachSpace)
            print(arg, end = '')
        self.drawSpaces(eachSpace)
        print("██\n", end = '')

    def drawLineWithParametersStartAt(self, lineLength, start, *args):
        remainingSpace = lineLength - 4 - start
        print("██", end = '')
        self.drawSpaces(start)
        for arg in args:
            print(arg, end = '')
            print(" ", end = '')
            remainingSpace -= len(arg) + 1
        self.drawSpaces(remainingSpace)
        print("██\n", end = '')

    def drawMovieGrid(self, lineLength, movies, page):
        spaceCounts = [0, 0, 0, 0]
        dic = {'name': 'name', 'date': 'date', 'capacityLeft': 'capacity', 'price': 'price'}
        pageMovies = movies[(page - 1) * 8: min(page * 8, len(movies))]
        pageMovies.insert(0, dic)
        for movie in pageMovies:
            spaceCounts[0] = max(spaceCounts[0], len(movie['name']))
            spaceCounts[1] = max(spaceCounts[1], len(movie['date']))
            spaceCounts[2] = max(spaceCounts[2], len(movie['capacityLeft']))
            spaceCounts[3] = max(spaceCounts[3], len(movie['price']))
        for i in spaceCounts:
            lineLength -= i
        lineLength -= 16
        for i in range(len(pageMovies)):
            movie = pageMovies[i]
            print('██', end = '  ')
            if i == 0:
                self.drawSpaces(4)
            else:
                print(str(i) + ' - ', end = '')
            print(movie['name'], end = '')
            print(' ' * (spaceCounts[0] - len(movie['name'])), end = ', ')
            print(movie['date'], end = '')
            print(' ' * (spaceCounts[1] - len(movie['date'])), end = ', ')
            print(movie['capacityLeft'], end = '')
            print(' ' * (spaceCounts[2] - len(movie['capacityLeft'])), end = ', ')
            print(movie['price'], end = '')
            print(' ' * (spaceCounts[3] - len(movie['price'])), end = '')
            self.drawSpaces(max(lineLength, 0))
            print('██', end = '\n')

    def drawCardsGrid(self, lineLength, startAt, cards):
        spaceCounts = [0, 0, 0, 0]
        spaceCounts[0] = len(str(len(cards) + 5))
        for card in cards:
            spaceCounts[1] = max(spaceCounts[1], len(card['bankName']))
            spaceCounts[2] = max(spaceCounts[2], len(card['cardNumber']))
            spaceCounts[3] = max(spaceCounts[3], len(card['expireDate']))
        for i in spaceCounts:
            lineLength -= i
        lineLength -= 15
        for i in range(len(cards)):
            card = cards[i]
            print('██', end = '  ')
            print(str(i + startAt), end = '')
            print(' ' * (spaceCounts[0] - len(str(i + startAt))), end = ' - ')
            print(card['bankName'], end = '')
            print(' ' * (spaceCounts[1] - len(card['bankName'])), end = ', ')
            print(card['cardNumber'], end = '')
            print(' ' * (spaceCounts[2] - len(card['cardNumber'])), end = ', ')
            print(card['expireDate'], end = '')
            print(' ' * (spaceCounts[3] - len(card['expireDate'])), end = '  ')
            self.drawSpaces(max(lineLength, 0))
            print('██', end = '\n')

    @staticmethod
    def save_cookies(cookies):
        cookie_jar = cookiejar.LWPCookieJar(filename="cookie.txt")
        for cookie in cookies:
            cookie_jar.set_cookie(cookiejar.Cookie(
                version=0, name=cookie.name, value=cookie.value, port=None, port_specified=False,
                domain=cookie.domain, domain_specified=True, domain_initial_dot=False,
                path=cookie.path, path_specified=True, secure=cookie.secure, expires=cookie.expires,
                discard=False, comment=None, comment_url=None, rest={'HttpOnly': cookie._rest.get('HttpOnly')}, rfc2109=False
            ))
        cookie_jar.save(ignore_discard=True, ignore_expires=True)



    @staticmethod
    def get_cookies():
        try:
            cookie_jar = cookiejar.LWPCookieJar('cookie.txt')
            cookie_jar.load(ignore_discard=True, ignore_expires=True)
        except FileNotFoundError:
            cookie_jar={}
        from requests.cookies import cookiejar_from_dict
        return cookiejar_from_dict({c.name: c.value for c in cookie_jar})
