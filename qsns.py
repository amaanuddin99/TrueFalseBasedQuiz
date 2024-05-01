import requests
class Qsns:
    response=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    data=response.json()
    
    def __init__(self):
        self.qsn=[]
        for i in range(1,10):
            self.qsn.append({"qsn":self.data["results"][i]["question"],"ans":self.data["results"][i]["correct_answer"]})
           # print(self.qsn)
          #self.qsn=1
    
