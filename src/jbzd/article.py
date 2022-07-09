class Article:
    def __init__(self, el) -> None:
        self._id = int(el.get('data-content-id'))
        try:
            img = el.select('div div a img')[0]
            self.src = img['src']
            self.title = img['alt']
            self.type = 'img'
        except:
            # TODO better exception handling
            vid = el.find_all('videoplyr')[0]
            self.src = vid['video_url']
            self.title = ''.join(el.select('h3 a')[0].get_text()).strip()
            self.type = 'vid'

    def __str__(self):
        return f'Article {self._id} {self.type} - {self.title} [ {self.src} ]'
