class Dog():
    """创建一个小狗类"""

    def __init__(self, name, age):
        """初始化属性name和age __init__类似与php中的__construct"""

        self.name = name
        self.age = age
        self.sex = 0

    def sit(self):
        """模拟小狗被命令时蹲下"""

        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟小狗被命令时打滚"""

        print (self.name.title() + " rolled over!")

my_dog = Dog('williw', 6)
my_dog.sex = 1#直接修改属性的值
print (my_dog.name, my_dog.age, my_dog.sex)
my_dog.sit()
my_dog.roll_over()