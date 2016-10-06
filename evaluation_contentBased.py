"""generating recommended tags by the model"""
import json
with open('./files/content_based/positive_coverage_data/test_question_tag_prop_weight_dict.json') as datafile:
	tag_prop_weights_dict = json.load(datafile)

# # for key in tag_prop_weights_dict.keys():
# # 	print tag_prop_weights_dict[key]

with open('./files/content_based/positive_coverage_data/tag_dict.json') as datafile:
	tag_dict = json.load(datafile)

with open('./files/content_based/content_based_refined_tag_list_list.json') as datafile:
	tag_list_list = json.load(datafile)

index_tag_dict = dict()
for key in tag_dict.keys():
	index_tag_dict[int(tag_dict[key])] = key

# print index_tag_dict

recommended_tags_list_dict = dict()

for key in tag_prop_weights_dict.keys():
	predics = tag_prop_weights_dict[key]
	top_indices = (sorted(range(len(predics)), key=lambda i: predics[i])[-10:])[::-1]
	recommended_tags = [index_tag_dict[i] for i in top_indices]
	print recommended_tags
	print tag_list_list[int(key)]


"""evaluation on the test set"""
def precision(rec_list,act_list,length):
	count = 0
	for tag in rec_list:
		if tag in act_list:
			count+= 1
	precision = float(count)/float(length)
	return precision

def recall(rec_list,act_list):
	count = 0
	for tag in rec_list:
		if tag in act_list:
			count += 1
		if len(act_list) == 0:
			return 0
		else:
			return float(count)/len(act_list)


precision3_list = []
precision5_list = []
precision10_list = []
recall3_list = []
recall5_list = []
recall10_list = []
count = 0
for key in tag_prop_weights_dict.keys():
	predics = tag_prop_weights_dict[key]
	top_indices = (sorted(range(len(predics)), key=lambda i: predics[i])[-10:])[::-1]
	recommended_tags = [index_tag_dict[i] for i in top_indices]
	actual_tags = tag_list_list[int(key)]
	#precision@3
	precision3 = precision(recommended_tags[0:3],actual_tags,3)
	precision3_list.append(precision3)
	#precision@5
	precision5 =  precision(recommended_tags[0:5],actual_tags,5)
	precision5_list.append(precision5)
	#precision@10
	precision10 = precision(recommended_tags,actual_tags,10)
	precision10_list.append(precision10)
	#recall@3
	recall3 = recall(recommended_tags[0:3],actual_tags)
	recall3_list.append(recall3)
	#recall@5
	recall5 = recall(recommended_tags[0:5],actual_tags)
	recall5_list.append(recall5)
	#recall@10
	recall10 = recall(recommended_tags[0:10],actual_tags)
	recall10_list.append(recall10)


import numpy as np
print "precision3",np.mean(precision3_list)
print "precision5",np.mean(precision5_list)
print "precision10",np.mean(precision10_list)
print "recall3",np.mean(recall3_list)
print "recall5",np.mean(recall5_list)
print "recall10",np.mean(recall10_list)

