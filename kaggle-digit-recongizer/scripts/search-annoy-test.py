#!/home/stefan2/anaconda/bin/python

from annoy import AnnoyIndex
#from annoy import AnnoyIndexEuclidean
import timeit

num_features = 784
num_nn = 100 #number of nearest neighbors

f='../data/index.annoy'

print 'loading index'
index = AnnoyIndex(num_features)
index.load(f)

print "reading test data"
f = open('../data/test.flann', 'r')
vectors = []
i = 0 #index for the points
for line in f:
  values = map(lambda value: float(value), line.rstrip().split(' '))
  vectors.append(values)  
  i += 1
f.close()

num_points = i

print 'reading labels'
f = open('../data/labels.train', 'r')
labels = map(lambda line: line.strip(), f.readlines())
f.close()

print "searching for nn and predicting"
start_time = timeit.default_timer()
output = []
for i in range(0, num_points):
  items = index.get_nns_by_vector(vectors[i], num_nn) #if you have the vectors
  as_str = str(i + 1) + "," + str(labels[items[0]])
  output.append(as_str)  
elapsed = timeit.default_timer() - start_time

print "Elapsed: ", elapsed

results = open('../data/kaggle-test-submission.txt', 'w')
results.write("ImageId,Label\n")
for as_str in output:
  results.write(as_str + "\n")
results.close()


