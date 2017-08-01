#定义函数
'''
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, "+username+"!")
#调用函数
greet_user('zhangmin')
'''

#位置实参，实参的顺序与形参的顺序一致
"""
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster', 'harry')

#关键字实参
describe_pet(pet_name='harry', animal_type='hamster')
"""

#默认值 def describe_pet(pet_name, animal_type='dog')

#函数内部返回处理后的值用return

#向函数传递列表
"""
def greet_users(names):
    for name in names:
        msg = "hello, "+name.title()+"!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
"""

#禁止函数修改列表，可将列表副本传递给函数 function_name(list_name[:])

#传递任意数量的实参,
# 形参前加上*,*的作用是让Python创建一个名为toppings的空元祖，并将所收到的所有值都封装到这个元祖中
#形参前加上**,**user_info的作用是让Python创建一个名为user_info的空字典，并将收到的所有键值对封装到这个字典中
"""
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
"""
def build_profile(**user_info):
    print(user_info)
#传参时键不需要加引号
build_profile(location='princeton', field='physics')
"""


#导入模块,使用as给模块指定别名
"""
import pythonModule as m
pythonModule.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
"""

#导入特定的函数
#from module_name import function_0, function_1, function_2
from pythonModule import make_pizza
#在导入函数时已经显示的导入了函数make_pizza(),因此调用时可不指定模块
make_pizza(16,'pepperoni')
#导入函数时可使用as给函数指定别名
from pythonModule import make_pizza as mp
mp(16, 'pepperoni')