# All Commands Operations and Output

# Code - Create : 
`>>> a_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## Expected output:
`>>> 
#*A new empty prompt signifies a successful creation*`


# Code Update : 
`>>> a_book = Book.objects.get(id=3)`
`>>> print(a_book)`

## Expected output:
`id: 3
title: 1984
author: George Orwell
publication_year: 1949
`

# Code - Update : 
`>>> a_book.title = "Nineteen Eighty-Four"`
`>>> a_book.save()`
`>>>print(a_book)`

## Expected output:
`id: 3
title: Nineteen Eighty-Four
author: George Orwell
publication_year: 1949
`

# Code - Delete: 

#*Code to delete an instance*
`>>> a_book.delete()`


## Expected output:
#*Output after deletion of a book object*
> 'from bookshelf.models import Book'
> `(1, {'bookshelf.Book': 1})
`

#*Output trying to retrieve all book object*

> QuerySet[ 
> Book: id: 1
title: Things fall apart
author: Chinwe Achebe
publication_year: 1959,

> Book: id: 2
title: Rich Dad Poor Dad
author: Robert kiyosaki
publication_year: 2005,

> Book: id: 4
title: Think and grow rich
author: Someone
publication_year: 1997]