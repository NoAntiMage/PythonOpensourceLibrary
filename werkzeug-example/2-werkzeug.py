from werkzeug.local import LocalStack, LocalProxy
user_stack1 = LocalStack()
user_stack1.push({'name': 'Bob'})
user_stack1.push({'name': 'John'})


def get_user1():
    return user_stack1.pop()


user1 = get_user1()
print(user1['name'])
print(user1['name'])


user_stack2 = LocalStack()
user_stack2.push({'name': 'Bob'})
user_stack2.push({'name': 'John'})


def get_user2():
    return user_stack2.pop()


user2 = LocalProxy(get_user2)
print(user2['name'])
print(user2['name'])
