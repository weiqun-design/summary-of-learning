import sys
sys.path.append('..')
import random
import math
import operator


class SimpleTagBased():
    def __init__(self,filename):
        self.filename=filename
        self.load_data()
        self.randomly_split_data(0.2)
        self.init_stat()
        self.testRecommend()

    def loadData(self):
        filename=self.filename
        self.records = {}
        fi = open(filename)
        lineNum=0
        for line in fi:
            lineNum += 1
            if lineNum == 1:
                continue
            uid,iid,tag,timestamp = line.split('\t')
            uid = int(uid) - 1
            iid = int(iid) - 1
            tag = int(tag) - 1
            self.records.setdefault(uid,{})
            self.records[uid].setdefault(iid,[])
            self.records[uid][iid].append(tag)
        fi.close()
        print(str(lineNum))
        print(len(self.records))

    def randomly_spilit_data(self, ratio, seed=100):
        random.seed(seed)
        self.train = dict()
        self.test = dict()
        for u in self.records.keys():
            for i in self.records[u].keys():
                if random.random() < ratio:
                    self.test.setdefault(u,{})
                    self.test[u].setdefault(i,[])
                    for t in self.records[u][i]:
                        self.test[u][i].append(t)
                else:
                    self.train.setdefault(u,{})
                    self.train[u].setdefault(i,[])
                    for t in self.records[u][i]:
                        self.train[u][i].append(t)
        print(len(self.train))
        print(len(self.test))

    def _add_value_to_mat(self, mat, index, item, value=1):
        if index not in mat:
            mat.setdefault(index,{})
            mat[index].setdefalut(item,value)
        else:
            if item not in mat[index]:
                mat[index][item] = value
            else:
                mat[index][item] += value

    def init_stat(self):
        records = self.train
        self.user_tags = dict()
        self.tag_items = dict()
        self.user_items = dict()
        for u, items in records.items():
            for i ,tags in items.items():
                for tag in tags:
                    self._add_value_to_mat(self.user_tags,u,tag,1)
                    self._add_value_to_mat(self.tag_items,tag, i, 1)
                    self._add_value_to_mat(self.user_items,u, i, 1)

    def recommend(self, user, N):
        recommend_items = dict()
        tagged_items = self.user_items[user]
        for tag, wut in self.user_items[user].items():
            for item ,wti in self.tag_items[tag].items():
                if item in tagged_items:
                    continue
                if item not in recommend_items:
                    recommend_items[item] = wut * wti
                else:
                    recommend_items[item] += wut * wti

