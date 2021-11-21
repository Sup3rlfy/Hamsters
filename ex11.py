"""
Author: Stanislaus Silber
Matr.Nr.: k0256733
Exercise 11
"""

import os
import glob

# os.system(...) = print()
#file_content = ""
#with open(os.path.join('00256733', 'data_00-000.gene.dat')) as f:
#    file_content = f.read()
file_content = ""
with open(os.path.join('ex11_testfiles', 'correct_7.gene.dat')) as f:
    file_content = f.read()

def count_bases_and_subsequence(data_as_string: str, subsequence: str):
    lines = data_as_string.split("\n")
    base_counts = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    gene_str = ""
    for line in lines:
        if line.startswith("% DATA_END"):
            gene_str += "."
            break
        if not line.startswith('%') and not line == '' and not line == ' ':
            split_line = line.split(';')
            base = split_line[1]
            if (float(split_line[2]) >= 0.07):
                if (base.upper() == "A"):
                        base_counts["a"] += 1
                        gene_str += "a"
                elif (base.upper() == "C"):
                        base_counts["c"] += 1
                        gene_str += "c"
                elif (base.upper() == "G"):
                        base_counts["g"] += 1
                        gene_str += "g"
                elif (base.upper() == "T"):
                        base_counts["t"] += 1
                        gene_str += "t"
            else:
                gene_str += "."
        else:
            gene_str += "."
    print(gene_str)
    # print(f"a: {base_counts['a']}\nc: {base_counts['c']}\ng: {base_counts['g']}\nt: {base_counts['t']}\n")
    subsequence_count = count_subsequence(gene_str, subsequence.lower())
    return (subsequence_count, base_counts)
# info ; base ; quality

def find_match(genes: str, a: int, sub: str, b: int):
    if genes[a] != sub[b]:
        return False
    elif b == len(sub)-1:
        return True
    return find_match(genes, a + 1, sub, b +1)

def count_subsequence(all_genes: str, subsequence: str):
    count = 0
    for i in range(len(all_genes) - len(subsequence)+1):
        j = 0
        match = find_match(all_genes, i, subsequence, j)
        if match:
            count += 1
    return count



print (count_bases_and_subsequence(file_content, "at"))

