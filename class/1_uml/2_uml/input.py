import datetime
from documents import Document, Book, Email

doc1 = Document( 101, ['anto', 'brenda', 'cate'])
print(doc1)
doc1.addAuthorName('dave')
print(doc1)

doc2 = Book( 102, ['boyd', 'carson'], 'Wiley', 'Basic')
print(doc2)

doc3 = Email( 103, ['lucas', 'Farias'], 'Wiley', 'Basic', datetime.date(2021, 2, 5))
print(doc3)