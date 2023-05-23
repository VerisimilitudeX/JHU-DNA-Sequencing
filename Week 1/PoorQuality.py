import collections

def phred33ToQ(qual):
    """Converts a single character into a phred33 quality score"""
    return ord(qual) - 33

def createHist(qualities):
    """Creates a histogram of quality scores at each position in the read"""
    hist = [0] * len(qualities[0])
    for qual in qualities:
        for i, phred in enumerate(qual):
            hist[i] += phred33ToQ(phred)
    return hist

# Read in the FASTQ file
filename = 'Week 1\\files\\ERR037900_1.first1000.fastq'
sequences = []
qualities = []
with open(filename) as fh:
    while True:
        fh.readline()  # skip name line
        seq = fh.readline().rstrip()  # read base sequence
        fh.readline()  # skip placeholder line
        qual = fh.readline().rstrip() # base quality line
        if len(seq) == 0:
            break
        sequences.append(seq)
        qualities.append(qual)

# Calculate the average quality score at each position in the read
hist = createHist(qualities)
print(hist)