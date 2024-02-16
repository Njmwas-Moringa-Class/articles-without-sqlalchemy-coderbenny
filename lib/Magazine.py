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

    def add_article(self, author, title):
        from Article import Article
        new_article = Article(self, author, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def all(cls):
        return cls.allMags

    @classmethod
    def find_by_name(cls,name):
        return next((magazine for magazine in cls.allMags if magazine.name() == name), None)
    
    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.allMags for article in magazine._articles]
    
    @classmethod
    def contributing_authors(cls):
        return [author for magazine in cls.allMags for author in magazine.contributors if len(author.articles()) > 2]