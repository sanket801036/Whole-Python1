def outer(msg):
    def inner():
        print(msg)
        return inner
    inner=outer('hello')del outer
    inner() #hello
-	Output:- hello
