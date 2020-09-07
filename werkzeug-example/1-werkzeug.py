from werkzeug.local import Local, LocalStack, LocalProxy

ls = LocalStack()
ls.push(42)
print(ls.top)
ls.push(23)
print(ls.top)
print(ls.pop())
print(ls.top)
