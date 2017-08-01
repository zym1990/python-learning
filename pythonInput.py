#input()让程序暂停，等待用户输入一些文本，获取用户输入，接收参数，向用户展示提示信息,input()获取的值均为字符串
'''
message = input("Tell me something, and I will repeat it back to you")
print(message)
print("Please enter your name: ")
print("Hello " + input())
'''

#若提示信息超过一行，可将提示信息存变量
'''
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, "+name+"!")
'''

#while循环
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''

#让用户选择何时退出
'''
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
'''

#标志，定义一个变量，判断整个程序的活动状态
'''
active = True
while active:
    message = input()
    if message == 'quit':
        active = False
    else:
        print(message)
'''

#流程控制,使用break退出循环,continue退出当前循环，继续下次循环
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
'''

#使用while循环处理列表和字典,要在遍历的同时进行修改，可用while循环
'''
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''

#使用用户输入来填充字典
responses = {}
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #将信息存储到字典中
    responses[name] = response
    repeat = input("Would you like to let another person response? (yes/no) ")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(name+" would like to climb "+response)

