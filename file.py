import pickle

def save(val, filename='save.dat'):
    isGood = False # flag , flag 변수는 if/else 구문과 연계해서 사용하기가 좋다 

    try: # io(input, output)은 try로 묶는게 안전
        f = open(filename, 'wb') # 파일객체 생성 , wb = write binary
        pickle.dump(val, f)
        isGood = True
    except:
        pass

    if isGood: result = '성공'
    else: result = '실패'

    print(f'{filename} 저장 {result}했습니다.')

def load(filename='save.dat'):
    val = None

    try: # save,load : string, number 타입일경우 txt 형태로 저장, but 객체일경우 binary로 저장
        f = open(filename, 'rb') # rb = read binary
        val = pickle.load(f) # load() : 데이터 불러오기
    except:
        pass # 예외가 발생하였을때 어떤 처리를 하지않고 지나가는것.

    return val