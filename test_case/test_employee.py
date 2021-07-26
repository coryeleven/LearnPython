import  unittest
from employee import Employee

# 模块 unittest 提供了代码测试工具,assertEqual 这一个判断给定两个参数是否相等的断言方法
class Test_emplpyee(unittest.TestCase):
    """测试模块employee。测试模块employee。"""
    def setUp(self):
        """创建一个Employee实例，以便在测试中使用。"""
        self.eric = Employee("eric","mattens",60000)

    def test_give_default_raise(self):
        """测试使用默认的年薪增加量是否可行。"""
        self.eric.give_raise()
        # assertEquals()是unittest类最有用的功能之一：一个断言方法。断言方法用来核实得到的结果与期望的结果一致。
        self.assertEqual(self.eric.salray,65000)

    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行。"""
        self.eric.give_raise(70000)
        self.assertEqual(self.eric.salary, 75000)

unittest.main()


