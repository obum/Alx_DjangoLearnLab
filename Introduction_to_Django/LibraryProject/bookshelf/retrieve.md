# CRUD Operations - Retrieve: 

## Command Instruction: 
Retrieve and display all attributes of the book you just created.

## Code : 
`>>> a_book = Book.objects.get(id=3)`
`>>> print(a_book)`

## Expected output:
`id: 3
title: 1984
author: George Orwell
publication_year: 1949
`