import sys
import csv

with open('hg83_gencode_v41_all_genes.tsv', 'r') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        # Do something with the row
        print(row)
# # First define a set of the chromosomes we want to include
# standard_chromosomes = set(["chr" + str(i) for i in range(1, 23)] + ["chrX", "chrY"])
# col_count = 0
# with open(sys.argv[1], "r") as input_file:
#     with open("hg83_gencode_v41_all_genes_output.csv", "w") as output_file:
#         for line in input_file:
#             if line.startswith("#"):
#                 output_file.write(line)
#                 col_count += 1
#                 continue

#             columns = line.strip().split("\t")
#             print
#             if columns[2] in standard_chromosomes:
#                 if (columns[9] == "protein_coding" and columns[10] == "protein_coding"):
#                     output_file.write(line)
#                     col_count += 1
# print(col_count)
    

# standard_chromosomes = set(["chr" + str(i) for i in range(1, 23)] + ["chrX", "chrY"])
# col_counter =  0
# with open("hg83_gencode_v41_all_genes.txt", "r") as input_file:
#     for line in input_file:
#         print(line)
#         # if line:
#         #     col_counter += 1
#         #     continue
#         columns = line.strip().split("\t")
#         print(columns)
#     print(col_counter)