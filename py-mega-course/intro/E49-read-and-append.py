#   7 Nov 2020
#
#   TASK
#   Append the text of bear1.txt to bear2.txt. bear2.txt should
#   contain its text and the text of bear1.txt after that.

def my_solution():
    with open( "bear1.txt", "r" ) as bear1:
        bear1_content = bear1.read()

    with open( "bear2.txt", "a" ) as bear2:
        bear2.write( bear1_content )

def solution():
    with open("bear1.txt") as file:
        content = file.read()

    with open("bear2.txt", "a") as file:
        file.write(content)
