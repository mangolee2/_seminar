from pymongo import MongoClient
from bson.objectid import ObjectId
# print("접속")#접속

client = MongoClient('mongodb://203.255.77.162:27017',
                      username='netdb',
                      password='netdb3230!',
                      authSource='RDA',
                      authMechanism='SCRAM-SHA-256')
db = client['RDA']
bestIntp = db['bestIntp']
# print(col.find_one())

# client = MongoClient('mongodb://203.255.77.162:27017', authSource='admin') # DB 접속
# # print(client) # DB 접속 확인
# db = client['RDA'] #필터접근
# # 필요시 DB에 csav를 저장할 수 있는 컬렉션 생성
# bestIntp = db['bestIntp']

def techRanking(xindex, yindex, cres):
    mse = 0
    key = ''
    for method in cres[xindex][yindex].keys():
        if cres[xindex][yindex][method] > mse:
            mse = cres[xindex][yindex][method]
            key = method
    return key

cres = [ [ { 'average' : 0.76, 'max' : 0.8, 'min' : 0.6, 'inter1' : 1.3 } , 
           { 'average' : 0.5, 'max' : 3.2, 'min' : 0.76, 'inter1' : 1.76 } , 
           { 'average' : 2.6, 'max' : 0.7, 'min' : 1.57, 'inter1' : 2.3 } , 
           { 'average' : 1.36, 'max' : 0.22, 'min' : 0.80, 'inter1' : 0.91 } , 
           { 'average' : 0.3, 'max' : 1.39, 'min' : 3.76, 'inter1' : 2.8 } 
         ],
         [ { 'average' : 1.6, 'max' : 1.8, 'min' : 0.9, 'inter1' : 1.3 } , 
           { 'average' : 1.5, 'max' : 0.6, 'min' : 1.8, 'inter1' : 2.1 } , 
           { 'average' : 1.7, 'max' : 1.8, 'min' : 1.57, 'inter1' : 2.3 } , 
           { 'average' : 1.5, 'max' : 1.1, 'min' : 0.80, 'inter1' : 0.91 } , 
           { 'average' : 1.8, 'max' : 1.4, 'min' : 3.76, 'inter1' : 2.8 }
         ],
         [ { 'average' : 0.76, 'max' : 0.8, 'min' : 0.6, 'inter1' : 1.3 } , 
           { 'average' : 0.5, 'max' : 3.2, 'min' : 0.76, 'inter1' : 1.76 } , 
           { 'average' : 2.6, 'max' : 0.7, 'min' : 1.57, 'inter1' : 2.3 } , 
           { 'average' : 1.36, 'max' : 0.22, 'min' : 0.80, 'inter1' : 0.91 } , 
           { 'average' : 0.3, 'max' : 1.39, 'min' : 3.76, 'inter1' : 2.8 }
         ]
        ]
    
for i in range(len(cres)):
    # print(i)
    csav = []
    for j in range(len(cres[i])):
        var = techRanking(i,j,cres)
        temp = {}
        temp[var] = j
        csav.append(temp)
    
    db.bestIntp.insert_many(csav)

        # print("i : {}, j : {}, var : {}, temp : {}, csav : {}".format(i, j, var, temp, csav))