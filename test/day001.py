a = 1
b = a
a = 2

print(a, b) # 2 1

a = [1]
b = a
a.append(2)

print(a, b) # [1, 2] [1, 2]

a = "hi"
b = a
a = a + "!"

print(a, b) # hi! hi

x = 5

def foo():
    x = 10
    print("foo:", x)

def bar():
    print("bar:", x)

foo()
bar()
print("global:", x)


# 先编译，编译为字节码，在虚拟机执行
# 解释运行

# def 作用域内，局部变量，函数内访问不到外部变量
# global 作用域内，访问全局变量
# 如果 def 内部访问了外部变量，且没有赋值，那么这个变量就是全局变量
# 如果 def 内 x = 10, 那么 x 就是新生成的局部变量，和全局变量没有关系
