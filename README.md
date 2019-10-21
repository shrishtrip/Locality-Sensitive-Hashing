# Locality-Sensitive-Hashing
 Text based information retrieval system using Locality Sensitive Hashing.
 
 * Here LSH is implemented on the  http://millionsongdataset.com/musixmatch/ dataset.
 * 3 distance metric is used:
   * Euclidean distance
   * Hamming distance
   * Angle distance
 * For each distance metric, a family of hash function is used (which is locality sensitive) which hash documents to buckets.
 * The union of all the buckets to which the query gets hashed, gives us the candidates for similarilty calculation.
 
