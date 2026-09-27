dna = input().strip()

a = c = g = t = 0

for nucleotide in dna:
    if nucleotide == "A":
        a += 1
    elif nucleotide == "C":
        c += 1
    elif nucleotide == "G":
        g += 1
    elif nucleotide == "T":
        t += 1
    

print(a, c, g, t)

/*
Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21
*/
