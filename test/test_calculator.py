# 测试用例
# 文件以test_开头，或者_test结尾
# 类要以Test开头，方法要以test_开头
import sys
# 扩展当前路径的上一级路径(..代表上一级路径)
import pytest
import yaml

sys.path.append('..')
print(sys.path)
# 测试类：TestCalculator
from pythoncode.Calculator import Calculator


# 模块级别
def setup_module():
    print("\n资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")


# 从calculator.yml文件中获取需要那部分测试数据['add']['datas']
def get_datas():
    with open("./datas/calculator.yml", 'rb') as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'])


def get_datas1():
    with open("./datas/calculator.yml", 'rb') as f:
        datas1 = yaml.safe_load(f)
    return (datas1['div']['datas'], datas1['div']['ids'])


def setup_function():
    print("(每次函数执行前都执行)资源准备：setup function")


def teardown_function():
    print("(每次函数执行后都执行)资源销毁：teardown function")


class TestCalculator:
    # :list 类型提示，可以提示该类型的一些参数或用法
    datas: list = get_datas()
    datas1: list = get_datas1()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    # 测试方法：相加
    # 参数化装饰器
    @pytest.mark.parametrize("a,b,result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        # 创建一个实例，调用pythoncode目录下的Calculator.py 文件下的 Calculator类
        # 实例化一个 calc
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a, b)

    # 测试方法：相除
    @pytest.mark.parametrize("a,b,result", datas1[0], ids=datas1[1])
    def test_div(self, a, b, result):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                print("除数不能为0")
        else:
            print(f"a={a},b={b},result={result}")
            assert result == self.calc.div(a, b)

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")
