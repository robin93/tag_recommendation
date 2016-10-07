"""data division into train and test"""
# import json
# with open('./files/questions_with_only_frequent_words_punch_removed.json') as data_file:
# 	question_list = json.load(data_file)

# with open('./files/tags_list_list_with_frequentTags.json') as data_file:
# 	tag_list_list = json.load(data_file)

# import random
# random.seed(100)
# train_indices = random.sample(range(1,47694),42694)

# train_question_list,test_question_list,train_tag_list,test_tag_list = [],[],[],[]

# for i in range(0,47694):
# 	if i in train_indices:
# 		train_question_list.append(question_list[i])
# 		train_tag_list.append(tag_list_list[i])
# 	else:
# 		test_question_list.append(question_list[i])
# 		test_tag_list.append(tag_list_list[i])
# print len(train_question_list),len(train_tag_list)
# print len(test_question_list),len(test_tag_list)

# with open("./files/modified_lda/train_question_list.json",'w') as outfile:
# 	json.dump(train_question_list,outfile)
# with open("./files/modified_lda/test_question_list.json",'w') as outfile:
# 	json.dump(test_question_list,outfile)
# with open("./files/modified_lda/train_tag_list_list.json",'w') as outfile:
# 	json.dump(train_tag_list,outfile)
# with open("./files/modified_lda/test_tag_list_list.json",'w') as outfile:
# 	json.dump(test_tag_list,outfile)

"""creating corpus for lda training"""
# import json
# with open("./files/modified_lda/train_question_list.json") as data_file:
# 	train_question_list = json.load(data_file)
# with open("./files/modified_lda/train_tag_list_list.json") as data_file:
# 	train_tag_list = json.load(data_file)


# lda_train_question_list = []
# for i in range(0,42694):
# 	print i
# 	question = train_question_list[i].split()
# 	tag_list = train_tag_list[i]
# 	termPtag = question+tag_list
# 	lda_train_question_list.append(termPtag)

# print len(lda_train_question_list)

# with open("./files/modified_lda/lda_train_termPtag.json",'w') as outfile:
# 	json.dump(lda_train_question_list,outfile)

"""training the lda model"""
# # Importing Gensim
# import gensim
# from gensim import corpora
# import numpy as np

# # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
# import json
# with open("./files/modified_lda/lda_train_termPtag.json") as data_file:
# 	question_list = json.load(data_file)

# print len(question_list)
# # doc_clean = [doc.split() for doc in question_list]
# doc_clean = question_list
# dictionary = corpora.Dictionary(doc_clean)
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
# print np.shape(doc_term_matrix)

# #creating the heldout set for perplexity estimation
# with open('./files/modified_lda/test_question_list.json') as data_file:
# 	question_list2 = json.load(data_file)

# doc_clean2 = [doc.split() for doc in question_list2]
# # doc_clean2 = question_list2
# print "creating dictionary"
# dictionary2 = corpora.Dictionary(doc_clean2)
# print "creating document term matrix"
# doc_term_matrix2 = [dictionary2.doc2bow(doc) for doc in doc_clean2]


# # Creating the object for LDA model using gensim library
# Lda = gensim.models.ldamodel.LdaModel

# # # Running and Trainign LDA model on the document term matrix.
# print "training the lda model"
# ldamodel = Lda(doc_term_matrix, num_topics=70, id2word = dictionary, passes=10,random_state= 10)
# print "perplexity",(ldamodel.log_perplexity(doc_term_matrix2))
# ldamodel.save("./files/modified_lda/30Passes_42000trainquestions_rand_70topics")


"""interpreting and predicting using the model"""
import gensim
from gensim import corpora
import numpy as np
import json
model_to_predict = gensim.models.ldamodel.LdaModel.load("./files/modified_lda/10Passes_42000trainquestions_rand_70topics")

# topic_word_list = model_to_predict.print_topics(num_topics=70, num_words=50)
topic_word_list = model_to_predict.show_topic(1, topn=100)

# print topic_word_list[0][1]

# with open("./files/modified_lda/train_tag_list_list.json") as data_file:
#  	train_tag_list = json.load(data_file)
# tags = []
# for tag_list in train_tag_list:
# 	for tag in tag_list:
# 		tags.append(tag)
# from collections import Counter
# tag_counts = Counter(tags)
# unique_tags = tag_counts.keys()

# with open('./files/modified_lda/unique_tags.json','w') as outfile:
# 	json.dump(unique_tags,outfile)

# with open('./files/modified_lda/unique_tags.json') as data_file:
# 	unique_tags = json.load(data_file)

# topic_tag_prob_dict = dict()

# for i in range(0,70):
# 	words_prob_list = model_to_predict.show_topic(i, topn=100)
# 	topic_tag_prob_dict[i] = []
# 	count = 0
# 	for word_list in words_prob_list:
# 		if count < 11:
# 			if word_list[0] in unique_tags:
# 				topic_tag_prob_dict[i].append([word_list[0],word_list[1]])
# 				count += 1
# print len(topic_tag_prob_dict.keys())

# with open('./files/modified_lda/topic_tag_dict.json','w') as outfile:
# 	json.dump(topic_tag_prob_dict,outfile)


"""prediction on the test data set"""
# with open('./files/modified_lda/topic_tag_dict.json') as data_file:
# 	topic_tag_dict = json.load(data_file)

# with open("./files/modified_lda/test_question_list.json") as data_file:
# 	test_questions = json.load(data_file)

# print len(test_questions)
# doc_clean = [doc.split() for doc in test_questions]
# dictionary = corpora.Dictionary(doc_clean)
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
# topics = model_to_predict.get_document_topics(doc_term_matrix)

# with open('./files/modified_lda/unique_tags.json') as data_file:
# 	unique_tags = json.load(data_file)


# tag_index_dict = dict()
# loop = 0
# for tag in unique_tags:
# 	tag_index_dict[tag] = loop
# 	loop += 1

# index_tag_dict = dict()
# for keys in tag_index_dict.keys():
# 	index_tag_dict[tag_index_dict[keys]] = keys


# test_question_prediction_list = []

# loop = 0
# for question in topics:
# 	preds = [0]*436
# 	for lat_topic in question:
# 		topic = lat_topic[0]
# 		topic_prob = lat_topic[1]
# 		tag_prob_list = topic_tag_dict[str(topic)]
# 		for tag_prob in tag_prob_list:
# 			tag_index = tag_index_dict[tag_prob[0]]
# 			to_add = float(tag_prob[1])*float(topic_prob)
# 			preds[tag_index] += to_add
# 	top_indices = (sorted(range(len(preds)), key=lambda i: preds[i])[-10:])[::-1]
# 	tag_recommend = [index_tag_dict[i] for i in top_indices]
# 	test_question_prediction_list.append(tag_recommend)
# 	tag_preds = []
# 	loop += 1
# 	print loop
# 	# if loop > 1:
# 	# 	break

# print len(test_question_prediction_list)

# with open('./files/modified_lda/test_set_recommended_tags.json','w') as outfile:
# 	json.dump(test_question_prediction_list,outfile)

"""evaluation"""
import json
with open('./files/modified_lda/test_set_recommended_tags.json') as data_file:
 	recommended_tag_list_list = json.load(data_file)

with open("./files/modified_lda/test_tag_list_list.json") as data_file:
	actual_tag_list_list = json.load(data_file)
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

for i in range(0,5000):
	recommended_tags = recommended_tag_list_list[i]
	actual_tags = actual_tag_list_list[i]
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


