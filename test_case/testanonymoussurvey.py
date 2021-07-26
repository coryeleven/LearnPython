import unittest
from  anonymoussurvey import AnonymousSurvey
class TestAnonyMousSurvey(unittest.TestCase):
    def setUp(self):
        #  创建一个调查对象和一组答案
        question = "世上最好的语言是？"
        self.language_survey = AnonymousSurvey(question)
        self.responses_list = ['C++','Java','Go','JS']

        # 测试保存单份问卷的方法
    def test_stor_single_response(self):
        self.language_survey.store_response(self.responses_list[1])
        self.assertIn('Java', self.language_survey.responses)

    def test_store_three_response(self):
        for response in self.responses_list:
            self.language_survey.store_response(response)
        # assertIn 断言方法来测试函数
        for response in self.responses_list:
            self.assertIn(response,self.language_survey.responses)

       

unittest.main()
        
