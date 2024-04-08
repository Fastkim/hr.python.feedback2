class Laborer:
    def __init__(self, laborerId, laborerName, hireDate): # 생성자에 입력받은 데이터들을 저장.
        self.laborerId = laborerId
        self.laborerName = laborerName
        self.hireDate = hireDate
    
    # 캡슐화(Encapsulation) 과정
    def getLaborerId(self):
        return self.laborerId
    
    def getLaborerName(self):
        return self.laborerName
    
    def getHireDate(self):
        return self.hireDate
    
    # --------------------------------------------------------------------------------- 위는 get : read, 아래는 set : write

    def setLaborerId(self, laborerId):
        self.laborerId = laborerId    # 기존의 laborerId를 수정하는것

    def setLaborerName(self, laborerName):
        self.laborerName = laborerName

    def setHireDate(self, hireDate):
        self.hireDate = hireDate
    
    # __ : 문법상 이미 정의가 되어있는 메서드를 말한다. 호출하여 overroad하기만 하면됨.
    def __str__(self):
        return f'{self.laborerId:>5}      {self.laborerName:<5}      {self.hireDate}' # >5 : 왼쪽에서 5만큼 벌려라, <5 오른쪽에서 5만큼 벌려라, 입벌린곳에서 떨어지는것
    
