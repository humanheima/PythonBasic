print(" I am A！")

print("__name__的值：",__name__)   

# 直接作为脚本执行，会执行下面的代码
# 被别人引用的时候，不会执行下面的代码，参考 name_main_two.py
# 
if __name__ == "__main__":
    print(" I am B！")