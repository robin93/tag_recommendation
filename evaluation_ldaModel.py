"""generating recommended tags by the model"""

# with open('/home/robin/Documents/tags/files/10KcrossVal_data/predictions_MultiNB_6Oct.csv') as csvfile:
# 	loop = 0
# 	for row in csvfile:
# 		print row
# 		loop += 1
# 		if loop >3:
# 			break

# index_tag_dict = dict()
# with open("./files/tag.set.csv") as tags_file:
# 	loop = -2
# 	for line in tags_file:
# 		loop += 1
# 		if loop > -1:
# 			tag_duple_str = line.split(",")[1]
# 			index_tag_dict[loop] = (tag_duple_str).strip()[1:-1]

# print index_tag_dict[2]

# list_of_recommended_tags = []
# with open("./files/10KcrossVal_data/predictions_MultiNB_6Oct.csv") as datafile:
# 	loop = 0
# 	for line in datafile:
# 		loop += 1
# 		# if loop>4:
# 		# 	break
# 		print loop
# 		str_list = line.split(",")[1:436]
# 		int_list = [ float(i) for i in str_list]
# 		top_indices = (sorted(range(len(int_list)), key=lambda i: int_list[i])[-10:])[::-1]
# 		recommended_tags = [index_tag_dict[i] for i in top_indices]
# 		list_of_recommended_tags.append(recommended_tags)

# # print list_of_recommended_tags[0:4]

# import json
# with open('./files/10KcrossVal_data/recommended_tags_multiNB.json','w') as outfile:
#  	json.dump(list_of_recommended_tags,outfile)

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



import json
with open('./files/10KcrossVal_data/recommended_tags_multiNB.json') as datafile:
	recommendations_list = json.load(datafile)



print len(recommendations_list)

precision3_list = []
precision5_list = []
precision10_list = []
recall3_list = []
recall5_list = []
recall10_list = []
count = 0
with open('./files/10KcrossVal_data/test_tag_list.csv') as datafile:
	loop = 0
	for line in datafile:
		loop += 1
		print loop
		if loop != 4782:
			# print line
			actual_tags = (line[1:-1]).split(",")
			recommended_tags = [str(i) for i in recommendations_list[loop-1]]
			# print len(actual_tags)
			# print recommended_tags
			# print ",".join(actual_tags)
			# print ",".join(recommended_tags)
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
# 			# outcome = [precision3,precision5,precision10,recall3,recall5,recall10]
# 			# to_write = ",".join([str(i) for i in outcome])
# 			# print to_write

# 			# outcome = precision3+precision5+precision10+recall3+recall5+recall10
# 			# if outcome > 0:
# 			# 	print loop,outcome,"non zero"
# 			# 	print actual_tags
# 			# 	print recommended_tags
import numpy as np
print "precision3",np.mean(precision3_list)
print "precision5",np.mean(precision5_list)
print "precision10",np.mean(precision10_list)
print "recall3",np.mean(recall3_list)
print "recall5",np.mean(recall5_list)
print "recall10",np.mean(recall10_list)

