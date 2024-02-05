from Author import Author
from Magazine import Magazine
class Article:

    articles = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.articles.append(self)
        Author.add_article(magazine, title)
        Magazine._articles.append(self)

    def title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine
    
    @classmethod
    def all(cls):
        return cls.articles