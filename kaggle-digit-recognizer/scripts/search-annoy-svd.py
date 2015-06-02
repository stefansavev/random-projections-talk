#!/home/stefan2/anaconda/bin/python

from annoy import AnnoyIndex
#from annoy import AnnoyIndexEuclidean

num_features = 100
num_points = 42000
num_nn = 100 #number of nearest neighbors

f='../data/index.annoy'

index = AnnoyIndex(num_features)
index.load(f)

results = open('../data/annoy-results.train.txt', 'w')
print "search for nn"

for i in range(0, num_points):
  items = index.get_nns_by_item(i, num_nn)
  #items = t.get_nns_by_vector(vectors[i], 100) #if you have the vectors
  if (items[0] != i):
    print 'the top nn is expected to be the item itself'
    raise SystemExit
  as_str = " ".join(map(str, items))  
  results.write(as_str + "\n")
results.close()


