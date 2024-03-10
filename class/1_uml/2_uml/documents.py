
class Document:
    def __init__(self, documentID, authors):
        self.documentID = documentID
        self.authors = authors

    def __repr__(self):
        return f'Document ID: {self.documentID}, Authors: {self.authors}'
    
    def addAuthorName(self, authorName):
        self.authors.append(authorName)

class Book(Document):
    def __init__(self, documentID, authors, publisher, title):
        super().__init__(documentID, authors)
        self.publisher = publisher
        self.title = title

    def __repr__(self):
        return f'{super().__repr__()} Publisher: {self.publisher}, Title: {self.title}'
    

class Email(Document):
    def __init__(self, documentID, authors, subject, sentTo, sentDate):
        super().__init__(documentID, authors)
        self.subject = subject
        self.sentTo= sentTo
        self.sentDate =  sentDate

    def __repr__(self):
        return f'{super().__repr__()} Subject: {self.subject}, Sent To: {self.sentTo}, Sent Date: {self.sentDate}'

    