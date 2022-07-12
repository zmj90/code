# 适合面向过程(全局变量,函数)
import exercise_module

print(exercise_module.data)
exercise_module.func01()
m = exercise_module.MyClass()
m.func02()

# 适合面向对象(类)
from exercise_module import *

print(data)
func01()
m =  MyClass()
m.func02()
