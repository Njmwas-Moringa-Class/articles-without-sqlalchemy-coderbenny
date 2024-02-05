from Article import Article

class Magazine:
    
    allMags = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.allMags.append(self)

    def name(self):
        return self._name
    
    def category(self):
        return self._category

    @classmethod
    def add_mag(cls, mag):
        if mag in cls.allMags:
            print("Magazine already exists!")
        else:
            cls.allMags.append(mag)
            print("Added the magazine succesfully!")

    @classmethod
    def all(cls):
        return cls.allMags

    @classmethod
    def find_by_name(cls,name):
        return next((magazine for magazine in cls.allMags if magazine.name == name), None)
    
    @classmethod
    def article_titles(cls):
        return [article.title for magazine in cls.allMags for article in magazine._articles]
    
    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]