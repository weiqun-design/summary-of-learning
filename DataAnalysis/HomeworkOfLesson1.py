import numpy as np

score_type = np.dtype({"names": ["name", "chinese", "english", "math"], "formats": ['S32', 'i', 'i', 'i']})
score_list = np.array(
    [("zhangfei", 66, 65, 30), ('guanyu', 95, 85, 98), ('zhaoyun', 93, 92, 96), ("huangzhong", 90, 88, 77),
     ('dianwei', 80, 90, 90)], dtype=score_type)
print("科目|mean|min|max|方差|标准差")
for name in ['chinese','english','math']:
    print(name + '|' +str(np.mean(score_list[:][name])) + '|' + str(np.amin(score_list[:][name])) + '|' + str(np.amax(score_list[:][name])) + '|'
          + str(np.var(score_list[:]['chinese'])) + '|' + str(np.std(score_list[:][name])))

total_score_list = list()
for score in score_list:
    total_score = 0
    for name in ['chinese','english','math']:
        total_score += score[name]
    total_score_list.append([score['name'],total_score])

print(sorted(total_score_list,key=lambda x:x[1], reverse=True))






