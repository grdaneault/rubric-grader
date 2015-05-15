# rubric-grader
Grade rubric parser and calculator.
==============

Developed for python version: 3.4.2 or higher

This program looks in the specified or current directory for .txt files. It then parses through them and calculates
the grades for each file.

The format of the rubric should be something as follows:

                Updated DlList Functions (20 Points):
                  	createList          (2  / 2 points )
                  	clear				(2  / 2 points )
                  	toString		    (2  / 2 points )
                  	append 			    (2  / 2 points )
                  	insertAt		    (2  / 2 points )
                  	get					(2  / 2 points )
                  	set					(2  / 2 points )
                  	pop					(2  / 2 points )
                  	index				(2  / 2 points )
                  	isEmpty			    (2  / 2 points )

The program first parses on '2 / 2' using a regular expression which can have any number of spaces between the numbers and '/' symbol and any number greater than or equal to 0.

You can also choose to write the total grade to the end of the text files, on program completion it prints out all the grades in alphabetical order.
