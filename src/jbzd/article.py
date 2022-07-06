class Article:
    def __init__(self, el) -> None:
        self._id = el.get('data-content-id')
        try:
            img = el.select('div div a img')[0]
            self.src = img['src']
            self.title = img['alt']
        except:
            # need to figure out how to scrap video src
            # vid = el.find_all('video')
            self.src = ''
            self.title = ''

    def __str__(self):
        return f'Article {self._id} - {self.title} [ {self.src} ]'
