cat ../data/train.csv | awk 'BEGIN { FS = "," } ; {$1=""; print substr($0,2)}' | tail -n +2 > ../data/train.flann
#cat ../data/test.csv | sed "s/,/ /g" | tail -n +2 > ../data/test.flann
#cat ../data/train.csv | awk 'BEGIN { FS = "," } ; {print $1}' | tail -n +2 > ../data/labels.train

