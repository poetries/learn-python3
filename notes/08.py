''' 
闭包 = 函数+环境变量（在函数外部）
'''

def test():
  num = 10
  def fun(x):
    return num * x
  return fun

f = test()
print(f(10))

origin = 0
def go(step):
  global origin 
  new_pos = step + origin 
  origin = new_pos
  return new_pos

print(go(1))
print(go(2))
print(go(3))