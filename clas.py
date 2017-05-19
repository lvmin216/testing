class stu(object):
    pass
s=stu()
def set_age(self,age):
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

def set_score(self,score):
    self.score=score
stu.set_score=set_score


