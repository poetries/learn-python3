''' 
枚举
''' 

from enum import Enum

class VIP(Enum):
  # 值可以相同 但是py会把第二个设置别名
  yellow = 1
  green = 2
  red = 3
  black = 4

# 枚举不能被修改
# VIP.red = 10
print(VIP.yellow)

# 获取枚举值
print(VIP.yellow.value)

# 获取枚举标签
print(VIP.yellow.name)

# 根据名称获取枚举类
print(VIP['red']) # VIP.red

# 枚举遍历 获取每个成员
for i in VIP:
  print(i)


for v in VIP.__members__.items():
  print(v)

''' 
('yellow', <VIP.yellow: 1>)
('green', <VIP.green: 2>)
('red', <VIP.red: 3>)
('black', <VIP.black: 4>)
'''

# 成员之间进行比较 不持续大小比较
res = VIP.red == VIP.black
print(res) # False

# 身份比较
print(VIP.red is VIP.red)

# 枚举类型转换
print(VIP(1)) # VIP.yellow