# 模块级别
def setup_module():
    print("\n(仅执行一次)资源准备：setup module")


def teardown_module():
    print("(仅执行一次)资源销毁：teardown module")


# 测试方法
def test_case1():
    print("case11111111111")


def setup_function():
    print("(每次函数执行前都执行)资源准备：setup function")


def teardown_function():
    print("(每次函数执行后都执行)资源销毁：teardown function")


class TestDemo:

    # 执行类 前后分别执行setup_class  teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup,teardown
    def setup(self):
        print("(每次方法执行前都执行)TestDemo setup")

    def teardown(self):
        print("(每次方法执行后都执行)TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")


class TestDemo1:

    # 执行类 前后分别执行setup_class  teardown_class
    def setup_class(self):
        print("TestDemo1 setup_class")

    def teardown_class(self):
        print("TestDemo1 teardown_class")

    # 每个类里面的方法前后分别执行 setup,teardown
    def setup(self):
        print("(每次方法执行前都执行)TestDemo1 setup")

    def teardown(self):
        print("(每次方法执行后都执行)TestDemo1 teardown")

    def test_demo3(self):
        print("test demo3")

    def test_demo4(self):
        print("test demo4")
