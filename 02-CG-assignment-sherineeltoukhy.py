#reading in the sequence
flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'

#finding "c" count
c_count = flu_ns1_seq.count("C")
print (c_count)

#finding "G" count
G_count = flu_ns1.seq.count("G")
print(G_count)

#adding "c" and "g"
CG_count = c_count + G_count
print (CG_count)

#finding total
total_n = len(flu_ns1_seq)
print (total_n)

#calculating percentage
percent = CG_count/total_n
print (percent)
