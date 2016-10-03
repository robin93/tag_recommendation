#https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
# compile documents
#doc_complete = [doc1, doc2, doc3, doc4, doc5]

# import pickle

# objects = []
# with (open("./Data/phase1/TrainingSetForEnTagRecUnfiltered.pickle", "rb")) as openfile:
#     while True:
#         try:
#             objects.append(pickle.load(openfile))
#         except EOFError:
#             break

# uncleaned_question_list = []
# tag_list_list = []
# loop = 0
# for resource in objects[0]:
# 	loop += 1
# 	print loop
# 	# if loop > 10:
# 	# 	break
# 	question = resource['body']
# 	tags = resource['tags']
# 	user = resource['ownerUserId']
# 	# identity = resource['Id']
# 	uncleaned_question_list.append(question)
# 	tag_list_list.append(tags)

# print len(uncleaned_question_list)
# print len(tag_list_list)

import json
# with open('uncleaned_question_list.json', 'w') as outfile:
#     json.dump(uncleaned_question_list, outfile)

# with open('tag_list_list.json', 'w') as outfile:
#     json.dump(tag_list_list, outfile)

"""stop words removal, stemming,punctuation removed,numerics removed"""
# with open('uncleaned_question_list.json') as data_file:    
#     question_list = json.load(data_file)

# loop = 0
# small_list = []
# for question in question_list:
# 	loop += 1
# 	# if loop > 10:
# 		# break
# 	small_list.append(question)



# from nltk.corpus import stopwords 
# import re
# from nltk.stem import PorterStemmer
# # from nltk.stem.wordnet import WordNetLemmatizer

# import string
# stop = set(stopwords.words('english'))
# exclude = set(string.punctuation) 
# # lemma = WordNetLemmatizer()
# port = PorterStemmer()
# def clean(doc):
#     stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
#     numeric_free = " ".join([(re.sub('[0-9]+','',i)) for i in stop_free.split()])
#     # punc_free = ''.join(ch for ch in numeric_free if ch not in exclude)
#     stemmed = " ".join(port.stem(word) for word in numeric_free.split())
#     return stemmed

# # doc_clean = [clean(doc).split() for doc in small_list]
# doc_clean = [clean(doc) for doc in small_list]

# print len(doc_clean)

# print "dumping to json"
# with open('cleaned_question_list.json', 'w') as outfile:
#     json.dump(doc_clean, outfile)

"""word frequency analysis"""
# import json
# with open('cleaned_question_list.json') as data_file:
# 	question_list = json.load(data_file)

# word_list = []
# for question in question_list:
# 	for word in question.split():
# 		word_list.append(word)

# from collections import Counter
# counts = Counter(word_list)

# print "list_of_words with all frequencies",len(counts.keys())
# list_of_words_to_retain = []
# for word in counts.keys():
# 	if counts[word] > 20:
# 		list_of_words_to_retain.append(word)

# print "list of words with frequencies greater than 20",len(list_of_words_to_retain)

# question_list_wordscountGreaterthan20 = []
# loop = 0
# for question in question_list:
# 	loop += 1
# 	modified_question = " ".join([i for i in question.split() if i in list_of_words_to_retain])
# 	print loop
# 	question_list_wordscountGreaterthan20.append(modified_question)

# print len(question_list_wordscountGreaterthan20)

# # with open('word_count_greaterThan20_dict.json','w') as outfile:
# # 	json.dump(count_greaterThan20,outfile)

# with open('questions_with_only_frequent_words.json','w') as outfile:
# 	json.dump(question_list_wordscountGreaterthan20,outfile)

"""retaining frequent tags"""
# import json
# with open('tag_list_list.json') as data_file:
# 	tag_list_list = json.load(data_file)

# print "total number of bookmarks",len(tag_list_list) 

# list_of_tags = []
# for tag_list in tag_list_list:
# 	for tag in tag_list:
# 		list_of_tags.append(tag)


# print "total number of tags", len(list_of_tags)

# from collections import Counter
# counts = Counter(list_of_tags)

# tags_to_retain = []
# for tags in counts.keys():
# 	if counts[tags] > 50:
# 		tags_to_retain.append(tags)

# print "list of tags to retain",len(tags_to_retain)

# tags_list_list_with_frequentTags = []
# loop = 0
# for tag_list in tag_list_list:
# 	loop += 1
# 	if loop%10000 == 0:
# 		print loop
# 	new_list = [i for i in tag_list if i in tags_to_retain]
# 	tags_list_list_with_frequentTags.append(new_list)



# print "total number of new bookmarks after cleaning",len(tags_list_list_with_frequentTags)

# print "dumping to json now"
# with open('tags_list_list_with_frequentTags.json','w') as outfile:
# 	json.dump(tags_list_list_with_frequentTags,outfile)

"""train and test Data Division"""
# import json
# with open('questions_with_only_frequent_words.json') as data_file:
# 	question_list = json.load(data_file)

# train_list = [] 
# test_list = []
# loop = 0
# for question in question_list:
# 	loop += 1
# 	if loop < 40000:
# 		print loop,"train"
# 		train_list.append(question)
# 	else:
# 		print loop,"test"
# 		test_list.append(question)

# print "number of questions in train list",len(train_list)
# print "number of question in the test list",len(test_list)

# with open('train_questions.json','w') as outfile:
# 	json.dump(train_list,outfile)
# with open('test_questions.json','w') as outfile:
# 	json.dump(test_list,outfile)

# with open('tags_list_list_with_frequentTags.json') as data_file:
# 	tag_list_list = json.load(data_file)

# train_list = []
# test_list = []
# loop = 0
# for tag_list in tag_list_list:
# 	loop += 1
# 	if loop < 40000:
# 		print loop,"train"
# 		train_list.append(tag_list)
# 	else:
# 		print loop,"test"
# 		test_list.append(tag_list)
# print "number of tag list in train",len(train_list)
# print "number of tag list in test",len(test_list)

# output_file = open('test_tag_list.csv',"w")
# loop = 0
# for tag_list in test_list:
# 	loop += 1
# 	print loop
# 	# to_write = str(tag_list)[1:]
# 	# length = len(to_write)
# 	# to_write = to_write[:length-1] + "\n"
# 	to_write = ""
# 	for tag in tag_list:
# 		to_write = to_write + tag.encode("ascii") +","
# 	length = len(to_write)
# 	to_write = to_write[:length-1] + "\n"
# 	# print to_write
# 	# if loop > 3:
# 	# 	break
# 	# to_write = str(tag_list).replace("[","").replace("]","") + "\n"
# 	output_file.writelines(to_write)


"""train and test Data Division - 10 cross validation"""
# import json
# with open('./files/questions_with_only_frequent_words.json') as data_file:
# 	question_list = json.load(data_file)

# #Generate the random number list
# import random
# random.seed(100)
# train_indices = random.sample(range(1,50000),45000)



# train_list = [] 
# test_list = []
# loop = 0
# for question in question_list:
# 	loop += 1
# 	if loop in train_indices:
# 		print loop,"train"
# 		train_list.append(question)
# 	else:
# 		print loop,"test"
# 		test_list.append(question)

# print "number of questions in train list",len(train_list)
# print "number of question in the test list",len(test_list)

# with open('./files/10KcrossVal_data/train_questions_45000_rand.json','w') as outfile:
# 	json.dump(train_list,outfile)
# with open('./files/10KcrossVal_data/test_questions_5000_rand.json','w') as outfile:
# 	json.dump(test_list,outfile)

# with open('./files/tags_list_list_with_frequentTags.json') as data_file:
# 	tag_list_list = json.load(data_file)

# train_list = []
# test_list = []
# loop = 0
# for tag_list in tag_list_list:
# 	loop += 1
# 	if loop in train_indices:
# 		print loop,"train"
# 		train_list.append(tag_list)
# 	else:
# 		print loop,"test"
# 		test_list.append(tag_list)
# print "number of tag list in train",len(train_list)
# print "number of tag list in test",len(test_list)

# output_file = open('./files/train_tag_list.csv',"w")
# loop = 0
# for tag_list in train_list:
# 	loop += 1
# 	print loop
# 	to_write = ""
# 	for tag in tag_list:
# 		to_write = to_write + tag.encode("ascii") +","
# 	length = len(to_write)
# 	to_write = to_write[:length-1] + "\n"
# 	# if loop > 3:
# 	# 	break
# 	# to_write = str(tag_list).replace("[","").replace("]","") + "\n"
# 	output_file.writelines(to_write)

# output_file = open('./files/test_tag_list.csv',"w")
# loop = 0
# for tag_list in test_list:
# 	loop += 1
# 	print loop
# 	to_write = ""
# 	for tag in tag_list:
# 		to_write = to_write + tag.encode("ascii") +","
# 	length = len(to_write)
# 	to_write = to_write[:length-1] + "\n"
# 	# if loop > 3:
# 	# 	break
# 	# to_write = str(tag_list).replace("[","").replace("]","") + "\n"
# 	output_file.writelines(to_write)







"""apply lda model"""
# Importing Gensim
import gensim
from gensim import corpora
import numpy as np

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
# dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
# import json
# with open('./files/10KcrossVal_data/train_questions_45000_rand.json') as data_file:
# 	question_list = json.load(data_file)

import json
with open('./files/10KcrossVal_data/test_questions_5000_rand.json') as data_file:
	question_list = json.load(data_file)

print len(question_list)
doc_clean = [doc.split() for doc in question_list]
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
print np.shape(doc_term_matrix)



# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# # Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=100, id2word = dictionary, passes=1,random_state= 10)
print(ldamodel.log_perplexity(doc_term_matrix))
# ldamodel.save("10Passes_40000trainquestions")

# print(ldamodel.print_topics(num_topics=100, num_words=100))

"""prediction on unseen questions"""
# import json
# with open('test_questions.json') as data_file:
# 	question_list = json.load(data_file)

# model_to_predict = gensim.models.ldamodel.LdaModel.load("10Passes_40000trainquestions")
# print model_to_predict.print_topics(num_topics=100,num_words=100)

# doc_to_predict = [doc.split() for doc in question_list]
# dictionary = corpora.Dictionary(doc_to_predict)
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_to_predict]
# topics = model_to_predict[doc_term_matrix]


# output_file = open('test_questions_topic_distribution.csv','w')
# loop = 0
# for i in topics:
# 	empty_list = [0]*100
# 	loop += 1
# 	print loop
# 	for prob_values in i:
# 		empty_list[prob_values[0]] = prob_values[1]
# 	# if loop > 3:
# 	# 	break
# 	to_write = str(empty_list).replace("[","").replace("]","")
# 	output_file.writelines(to_write+"\n")


