import pickle

objects = []
with (open("./Data/phase1/TrainingSetForEnTagRecUnfiltered.pickle", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

output_file = open('postId_user_number_of_tags.csv','w')
output_file.writelines(("identity"+","+"user"+","+"number_of_tags"+"\n"))

loop = 0
for resource in objects[0]:
	loop += 1
	# print loop
	if loop > 1:
		break
	# question = resource['body']
	# tags = resource['tags']
	# user = resource['ownerUserId']
	# identity = resource['Id']
	# to_write = identity+","+user+","+str(len(tags))+"\n"
	# output_file.writelines(to_write)
	print resource
