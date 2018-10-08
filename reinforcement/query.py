def queryUser(feature_names):
	print "Please enter changes to features in the format:\n(feature 1 number) (+ for increase, - for decrease)\n(feature 2 number) (+/-)\n...\n(enter -1 -1 to stop)"
	for i in range(len(feature_names)):
		print str(i+1)+": "+feature_names[i]
	print "-------------------------------------"
	input_list = []
	for i in range(len(feature_names)):
		input_list.append(None)
	f,sign = raw_input().strip().split(' ')
	f = int(f)
	while (f!=-1):
		input_list[f-1] = sign
		f,sign = raw_input().strip().split(' ')
		f = int(f)

	return input_list

if __name__=="__main__":
	print queryUser(["a","b","c","d"])