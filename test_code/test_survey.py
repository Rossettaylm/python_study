import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        """方法 setUp() 做了两件事情:创建一个调查对象;创建一个答案列表。存储这
两样东西的变量名包含前缀 self (即存储在属性中),因此可在这个类的任何地方使用。这让两
个测试方法都更简单,因为它们都不用创建调查对象和答案。方法 test_store_three_response()
核 实 self.responses 中 的 第 一 个 答 案 —— self.responses[0] —— 被 妥 善 地 存 储 , 而 方 法
test_store_three_response() 核实 self.responses
中的全部三个答案都被妥善地存储。"""
        question = "What is your first language learnd to speak? "
        # self.responses是setUp的属性，和self.my_survey.responses不一样 
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']

    def test_single_store_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_store_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses: 
            self.assertIn(response, self.my_survey.responses)


unittest.main()
        

