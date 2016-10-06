# #Read all the questions and tags
# import json
# with open('./files/questions_with_only_frequent_words_punch_removed.json') as data_file:
# 	question_list = json.load(data_file)
# with open('./files/tags_list_list_with_frequentTags.json') as data_file:
# 	tag_list_list = json.load(data_file)

# print question_list[0]
# print tag_list_list[0]

# #Gather a list of unique tags
# all_tag_list = []
# for tag_list in tag_list_list:
# 	for tags in tag_list:
# 		all_tag_list.append(tags)



# unique_tag_list = list(set(all_tag_list))

# with open('./files/content_based/content_based_unique_tag_list.json','w') as outfile:
# 	json.dump(unique_tag_list,outfile)


# #Remove non-tag_list terms from the questions
# loop = 0
# refined_question_list = []
# refined_tag_list_list = []
# all_term_list = []
# for question in question_list:
# 	print loop
# 	# if loop>5:
# 	# 	break
# 	tag_list = tag_list_list[loop]
# 	word_list = [i for i in question.split() if i in unique_tag_list]
# 	if len(word_list)>0 and len(tag_list)>0:
# 		for words in word_list:
# 			all_term_list.append(words)
# 		refined_question = " ".join(word_list)
# 		refined_question_list.append(refined_question)
# 		refined_tag_list_list.append(tag_list)
# 	loop += 1

# print len(refined_question_list)
# # print refined_question_list
# print len(refined_tag_list_list)
# # print refined_tag_list_list

# unique_term_list = list(set(all_term_list))
# print unique_term_list

# with open('./files/content_based/content_based_refined_questions.json','w') as outfile:
# 	json.dump(refined_question_list,outfile)

# with open('./files/content_based/content_based_refined_tag_list_list.json','w') as outfile:
# 	json.dump(refined_tag_list_list,outfile)

# with open('./files/content_based/content_based_unique_term_list.json','w') as outfile:
	# json.dump(unique_term_list,outfile)

#Represent every resource as a vector of unique tags

"""Divide dataset into Train and Test"""
# import json
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	question_list = json.load(data_file)
# with open('./files/content_based/content_based_refined_tag_list_list.json') as data_file:
# 	tag_list_list = json.load(data_file)

# train_question_list,test_question_list,train_tag_list,test_tag_list = [],[],[],[]
# import random
# random.seed(100)
# train_indices = random.sample(range(1,41096),35000)
# print len(train_indices)

# for i in range(0,41096):
# 	if i in train_indices:
# 		train_question_list.append(question_list[i])
# 		train_tag_list.append(tag_list_list[i])
# 	else:
# 		test_question_list.append(question_list[i])
# 		test_tag_list.append(tag_list_list[i])

# print len(train_question_list),len(train_tag_list),len(test_question_list),len(test_tag_list)
# with open('./files/content_based/content_based_train_questions.json','w') as outfile:
# 	json.dump(train_question_list,outfile)

# with open('./files/content_based/content_based_test_questions.json','w') as outfile:
# 	json.dump(test_question_list,outfile)

# with open('./files/content_based/content_based_train_tag_list.json','w') as outfile:
# 	json.dump(train_tag_list,outfile)

# with open('./files/content_based/content_based_test_tag_list.json','w') as outfile:
# 	json.dump(test_tag_list,outfile)



"""calculate question-tag and question-term probabilities"""
# import json
# from collections import Counter
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	question_list = json.load(data_file)

# with open('./files/content_based/content_based_refined_tag_list_list.json') as data_file:
# 	tag_list_list = json.load(data_file)

# with open('./files/content_based/content_based_unique_tag_list.json') as data_file:
# 	unique_tag_list = json.load(data_file)

# with open('./files/content_based/content_based_unique_term_list.json') as data_file:
# 	unique_term_list = json.load(data_file)


# # print len(question_list)
# # print len(tag_list_list)

# question_tag_dict = dict()
# question_term_dict = dict()

# for i in range(0,41096):
# 	question = question_list[i]
# 	word_list = question.split()
# 	length_of_question = len(word_list)
# 	counts = Counter(word_list)
# 	list_of_term_count = []
# 	for term in counts.keys():
# 		list_of_term_count.append([term,float(counts[term])/float(length_of_question)])
# 	question_term_dict[i] = list_of_term_count

# 	tag_list = tag_list_list[i]
# 	list_of_tag_count =[]
# 	for tag in tag_list:
# 		list_of_tag_count.append([tag,float(1)/float(len(tag_list))])
# 	question_tag_dict[i] = list_of_tag_count
	
# 	print len(list_of_tag_count),"----",len(list_of_term_count)
# 	# if i > 10:
# 	# 	break
# 	if i%1000 == 0:
# 		print i

# print len(question_tag_dict.keys())
# # print question_tag_dict
# print "term dictionary"
# print len(question_term_dict.keys())
# # print question_term_dict

# with open('./files/content_based/content_based_question_tag_norm_prob.json','w') as outfile1:
# 	json.dump(question_tag_dict,outfile1)
# with open('./files/content_based/content_based_question_term_norm_prob.json','w') as outfile2:
# 	json.dump(question_term_dict,outfile2)

"""create the tag and term significance for each tag and term"""
# #create the tag significance dictionary
# import json
# import numpy as np
# with open('./files/content_based/content_based_question_tag_norm_prob.json') as data_file:
# 	question_tag_dict = json.load(data_file)
# tag_significance_dict = dict()
# loop = 0
# for question in question_tag_dict.keys():
# 	tag_prob_list_list = question_tag_dict[question]
# 	for tag_prob_list in tag_prob_list_list:
# 		if tag_prob_list[0] in tag_significance_dict.keys():
# 			entropy = abs(float(tag_prob_list[1])*np.log(float(tag_prob_list[1])))
# 			tag_significance_dict[tag_prob_list[0]] = tag_significance_dict[tag_prob_list[0]] + entropy
# 		else:
# 			entropy = abs(float(tag_prob_list[1])*np.log(float(tag_prob_list[1])))
# 			tag_significance_dict[tag_prob_list[0]] = entropy
# 	# if loop > 2:
# 	# 	break
# 	loop += 1
# 	if loop%10000==0:
# 		print loop

# print len(tag_significance_dict.keys())

# significance_values_list = []
# for keys in tag_significance_dict.keys():
# 	significance_values_list.append(tag_significance_dict[keys])
# normalizing_value = max(significance_values_list)
# for keys in tag_significance_dict.keys():
# 	tag_significance_dict[keys] = (1 - (tag_significance_dict[keys])/normalizing_value)
# with open('./files/content_based/tag_significance_dict.json','w') as outfile2:
#  	json.dump(tag_significance_dict,outfile2)

# #create the term significance dictionary
# import json
# import numpy as np
# with open('./files/content_based/content_based_question_term_norm_prob.json') as data_file:
# 	question_term_dict = json.load(data_file)
# term_significance_dict = dict()
# loop = 0
# for question in question_term_dict.keys():
# 	term_prob_list_list = question_term_dict[question]
# 	for term_prob_list in term_prob_list_list:
# 		if term_prob_list[0] in term_significance_dict.keys():
# 			entropy = abs(float(term_prob_list[1])*np.log(float(term_prob_list[1])))
# 			term_significance_dict[term_prob_list[0]] = term_significance_dict[term_prob_list[0]] + entropy
# 		else:
# 			entropy = abs(float(term_prob_list[1])*np.log(float(term_prob_list[1])))
# 			term_significance_dict[term_prob_list[0]] = entropy
# 	# if loop > 2:
# 	# 	break
# 	loop += 1
# 	if loop%10000==0:
# 		print loop

# print len(term_significance_dict.keys())

# significance_values_list = []
# for keys in term_significance_dict.keys():
# 	significance_values_list.append(term_significance_dict[keys])
# normalizing_value = max(significance_values_list)
# for keys in term_significance_dict.keys():
# 	term_significance_dict[keys] = (1 - (term_significance_dict[keys])/normalizing_value)
# with open('./files/content_based/term_significance_dict.json','w') as outfile2:
#  	json.dump(term_significance_dict,outfile2)

"""calculate tag coverage of questions and term coverage of questions"""
#Calculation of tag coverage for each question
# import json
# import numpy as np
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	question_list = json.load(data_file)
# with open('./files/content_based/tag_significance_dict.json') as data_file:
# 	tag_significance_dict = json.load(data_file)
# with open('./files/content_based/content_based_question_tag_norm_prob.json') as data_file:
# 	question_tag_prob_dict = json.load(data_file)
# question_tag_coverage_dict = dict()
# loop = 0
# for question in question_list:
# 	length_of_question = len(question.split())
# 	tag_coverage = 0
# 	# print length_of_question
# 	for tag_prob_list in question_tag_prob_dict[str(loop)]:
# 		tag_significance = tag_significance_dict[tag_prob_list[0]]
# 		tag_coverage = tag_coverage + float(tag_prob_list[1])*float(tag_significance)*np.log(length_of_question)
# 	# print tag_coverage
# 	question_tag_coverage_dict[loop] = tag_coverage
# 	loop += 1
# 	print loop
# 	# if loop >1:
# 	# 	break

# print len(question_tag_coverage_dict.keys())

# coverage_values = []
# for questions in question_tag_coverage_dict.keys():
# 	coverage_values.append(question_tag_coverage_dict[questions])
# normalizing_value = max(coverage_values)
# for questions in question_tag_coverage_dict.keys():
# 	question_tag_coverage_dict[questions] = float(question_tag_coverage_dict[questions])/float(normalizing_value)

# with open('./files/content_based/question_tag_coverage_dict.json','w') as outfile2:
#  	json.dump(question_tag_coverage_dict,outfile2)
	




# #Calculation of term coverage for each question
# import json
# import numpy as np
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	question_list = json.load(data_file)
# with open('./files/content_based/term_significance_dict.json') as data_file:
# 	term_significance_dict = json.load(data_file)
# with open('./files/content_based/content_based_question_term_norm_prob.json') as data_file:
# 	question_term_prob_dict = json.load(data_file)
# question_term_coverage_dict = dict()
# loop = 0
# for question in question_list:
# 	length_of_question = len(question.split())
# 	term_coverage = 0
# 	# print length_of_question
# 	for term_prob_list in question_term_prob_dict[str(loop)]:
# 		term_significance = term_significance_dict[term_prob_list[0]]
# 		term_coverage = term_coverage + float(term_prob_list[1])*float(term_significance)*np.log(length_of_question)
# 	# print tag_coverage
# 	question_term_coverage_dict[loop] = term_coverage
# 	loop += 1
# 	print loop
# 	# if loop >1:
# 	# 	break

# print len(question_term_coverage_dict.keys())

# coverage_values = []
# for questions in question_term_coverage_dict.keys():
# 	coverage_values.append(question_term_coverage_dict[questions])
# normalizing_value = max(coverage_values)
# for questions in question_term_coverage_dict.keys():
# 	question_term_coverage_dict[questions] = float(question_term_coverage_dict[questions])/float(normalizing_value)

# with open('./files/content_based/question_term_coverage_dict.json','w') as outfile2:
#  	json.dump(question_term_coverage_dict,outfile2)

"""filtering of questions with positive tag and term coverage"""
# import json
# with open('./files/content_based/question_tag_coverage_dict.json') as data_file:
# 	question_tag_coverage_dict = json.load(data_file)
# with open('./files/content_based/question_term_coverage_dict.json') as data_file:
# 	question_term_coverage_dict = json.load(data_file)
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	question_list = json.load(data_file)
# with open('./files/content_based/content_based_refined_tag_list_list.json') as data_file:
# 	tag_list_list = json.load(data_file)

# #write to csv to analyse the number of resources with zero tag or term coverage
# # output_file =  open('./files/content_based/question_tag_term_coverage.csv','w')
# # for i in range(0,41096):
# # 	if i%1000==0:
# # 		print i
# # 	ind = str(i)
# # 	to_write = ind+","+str(question_tag_coverage_dict[ind])+","+str(question_term_coverage_dict[ind])+"\n"
# # 	output_file.writelines(to_write)

# #retain the data with only positive tag or term coverage
# pos_coverages_indexes = []
# count = 0
# for i in range(0,41096):
# 	ind = str(i)
# 	tag_coverage,term_coverage = question_tag_coverage_dict[ind],question_term_coverage_dict[ind]
# 	if (tag_coverage > 0 and term_coverage >0):
# 		pos_coverages_indexes.append(i)

# with open('./files/content_based/positive_coverage_data/pos_coverage_indexes.json','w') as outfile2:
#  	json.dump(pos_coverages_indexes,outfile2)

# import random
# random.seed(100)
# train_indices = random.sample(range(1,32607),26000)
# print len(train_indices)

# train_indices_list,test_indices_list = [],[]
# loop = 0
# for indic in pos_coverages_indexes:
# 	loop += 1
# 	if loop in train_indices:
# 		train_indices_list.append(indic)
# 	else:
# 		test_indices_list.append(indic)
# print len(train_indices_list)
# print len(test_indices_list)

# with open('./files/content_based/positive_coverage_data/pos_coverage_train_indexes.json','w') as outfile2:
#  	json.dump(train_indices_list,outfile2)

# with open('./files/content_based/positive_coverage_data/pos_coverage_test_indexes.json','w') as outfile2:
#  	json.dump(test_indices_list,outfile2)




"""Calculate the similarity of all the questions in the test set to all in train set"""
# import json
# with open('./files/content_based/positive_coverage_data/pos_coverage_train_indexes.json') as data_file:
# 	pos_coverage_train_indexes = json.load(data_file)
# with open('./files/content_based/positive_coverage_data/pos_coverage_test_indexes.json') as data_file:
# 	pos_coverage_test_indexes = json.load(data_file)
# # with open('./files/content_based/question_tag_coverage_dict.json') as datafile:
# #  	question_tag_coverage_dict = json.load(datafile)
# with open('./files/content_based/question_term_coverage_dict.json') as datafile:
#  	question_term_coverage_dict = json.load(datafile)
# with open('./files/content_based/content_based_refined_questions.json') as data_file:
# 	refined_questions_list = json.load(data_file)

# output_file = open('./files/content_based/positive_coverage_data/test_train_URL_sim.csv','w')
# from collections import Counter
# # similarity_mat = dict()
# loop = 0
# for ind in pos_coverage_test_indexes:
# 	sim_mat_list = []
# 	for train_ind in pos_coverage_train_indexes:
# 		term_cover_test = question_term_coverage_dict[str(ind)]
# 		term_cover_train = question_term_coverage_dict[str(train_ind)]
# 		term_vector_test,term_vector_train = (refined_questions_list[ind]).split(),(refined_questions_list[train_ind]).split()
# 		length_test,length_train = len(term_vector_test),len(term_vector_train)
# 		count_test,count_train = Counter(term_vector_test),Counter(term_vector_train)
# 		sim = 0
# 		for terms in count_test.keys():
# 			for train_term in count_train.keys():
# 				if terms == train_term:
# 					sim = sim + count_test[terms]*count_train[terms]
# 		sim = float(sim)/float(length_train*length_test)
# 		sim = sim * float(term_cover_test)*float(term_cover_train)
# 		if sim > 0.0:
# 			to_write = str(ind)+","+str(train_ind)+","+str(sim)+"\n"
# 			output_file.writelines(to_write)
# 			# sim_mat_list.append([train_ind,sim])
# 	# similarity_mat[ind] = sim_mat_list
# 	loop += 1
# 	print loop
	# if loop > 3:
	# 	break

"""calculate the question tag propogated weight"""
import json
with open('./files/content_based/content_based_question_tag_norm_prob.json') as datafile:
 	question_tag_prob_dict = json.load(datafile)

with open('./files/content_based/content_based_refined_tag_list_list.json') as datafile:
	tag_list_list = json.load(datafile)

with open('./files/content_based/content_based_refined_questions.json') as datafile:
	question_list = json.load(datafile)

# tag_dict = dict()
# val = -1
# for tag_list in tag_list_list:	
# 	for tag in tag_list:
# 		if tag not in tag_dict.keys():
# 			val = val + 1
# 			tag_dict[tag] = val

# with open('./files/content_based/positive_coverage_data/tag_dict.json','w') as outfile:
# 	json.dump(tag_dict,outfile)

with open('./files/content_based/positive_coverage_data/tag_dict.json') as data_file:
	tag_dict = json.load(data_file)


test_question_tag_prop_weight_dict = dict()
with open("./files/content_based/positive_coverage_data/test_train_URL_sim.csv") as csvfile:
	loop = 1
	for row in csvfile:	
		test_ind,train_ind,sim = row.strip().split(",")[0],row.strip().split(",")[1],float(row.strip().split(",")[2])
		# train_url_tags = tag_list_list[loop]
		if test_ind not in test_question_tag_prop_weight_dict.keys():
			test_question_tag_prop_weight_dict[test_ind] = [0]*436
		tag_prob_list = question_tag_prob_dict[train_ind]
		question_length = len(question_list[int(train_ind)].split())
		for tag_list in tag_prob_list:
			tag = tag_list[0]
			prob_url2 = tag_list[1]
			tag_index = tag_dict[tag]
			test_question_tag_prop_weight_dict[test_ind][tag_index] += float(sim)*float(prob_url2)*float(question_length)
		# if loop > 3000:
		# 	break
		if loop%1000 == 0:
			print loop
		loop += 1

print test_question_tag_prop_weight_dict.keys()

with open('./files/content_based/positive_coverage_data/test_question_tag_prop_weight_dict.json','w') as outfile:
	json.dump(test_question_tag_prop_weight_dict,outfile)


"""Rank the tags for every question in the test set and recommend the tags"""