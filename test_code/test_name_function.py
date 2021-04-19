import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """以test_开头的函数会自动执行"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        """断言函数assertEqual（）判断是否相等"""
unittest.main()
