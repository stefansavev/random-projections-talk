#!/home/stefan2/anaconda/bin/python

#read the labels
f = open('../data/labels.train', 'r')
labels = map(lambda line: line.strip(), f.readlines())
f.close()

f = open('../data/annoy-results.train.txt', 'r')

missing = 0
correct = 0
evaluated = 0
#loop over the results and evaluate the accuracies
for line in f.xreadlines():
  items = line.split(' ')
  query = int(items[0])
  result = int(items[1])

  query_label = labels[query]
  results_label = labels[result]

  if (query_label == results_label):
    correct += 1
  evaluated += 1

f.close()

print 'accuracy in %: ', 100.0*float(correct)/float(evaluated)
