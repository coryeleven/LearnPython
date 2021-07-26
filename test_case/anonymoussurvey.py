class AnonymousSurvey():
    def __init__(self,question):
        # 收集匿名调查问卷的答案
        self.question = question
        self.responses = []
    def show_question(self):
        # 显示问卷
        print(self.question)
    def store_response(self,new_responsole):
        #  存储单份调查问卷
        self.responses.append(new_responsole)
    def show_results(self):
        # 显示所有答卷
        print("Survey results:")
        for response in self.responses:
            print('-',response)

def user_anonymouse_survey():
    question = 'Like language ?'
    # 显示问题
    language_survey = AnonymousSurvey(question)
    language_survey.show_question()
    # 添加问卷
    language_survey.store_response('php')
    language_survey.store_response('python')
    language_survey.store_response('java')
    # 显示所有问卷
    language_survey.show_results()

    
if __name__ == '__main__':
    user_anonymouse_survey()
    