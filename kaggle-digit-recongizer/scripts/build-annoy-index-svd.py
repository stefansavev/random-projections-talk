#!/home/stefan2/anaconda/bin/python

from annoy import AnnoyIndex
#from annoy import AnnoyIndexEuclidean

num_features = 100
num_trees = 10

index = AnnoyIndex(num_features) #alternative: AnnoyIndexEuclidean(num_features) 

f = open('../data/train.flann.svd', 'r')

print "reading data"
vectors = []
i = 0 #index for the points
for line in f:
  values = map(lambda value: float(value), line.rstrip().split(' '))
  index.add_item(i, values)
  vectors.append(values)  
  i += 1
f.close()
numPoints = i

print "building index"
index.build(num_trees)
print "saving trees"
index.save('../data/index.annoy')


