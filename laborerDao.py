import file
from laborer import Laborer

class LaborerDao: #Dao : Data access object
    def __init__(self): # 객체가 생성될떄 자동으로 call 되는 init
        self.laborers = file.load('laborers.dat') # 하드코딩 : 'laborers.dat' 변수가 아닌 고정되어있다.
        self.laborerIdSeq = file.load('laborerIdSeq.dat')

        if not self.laborers: self.laborers = [] # Seq : sequence => 순차적으로 값을 생성한다는 의미.
        if not self.laborerIdSeq: self.laborerIdSeq = 0

    def __del__(self): # 죽기전에 실행되는 녀석
        file.save(self.laborers, 'laborers.dat')
        file.save(self.laborerIdSeq, 'laborerIdSeq.dat')

    def selectLaborers(self):
        return self.laborers
    
    def selectLaborer(self, laborerId): # 값이 변하지않을것같은 data를 key로 설정한다. (laborerId)
        laborer = None
        laborers = list(filter(lambda laborer:
                               laborer.getLaborerId() == laborerId, self.laborers))