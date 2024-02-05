from Article import Article
class Author:
    
    authors = []

    def __init__(self, name):
        self._name = name
        self._articles = []
        Author.authors.append(self)

    def name(self):
        return self._name

    def set_name(self, name):
        print("Cannot change the name of the author after initialization!")

    name = property(name)

    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_articles(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)

    def topic_aread(self):
        return list(set(article.magazine.category for article in self._articles))