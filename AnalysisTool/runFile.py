import sys

print ("Hello, welcome to my Analysis Tool.")
print ("Here, I will be running a few tests to help you along.\n")
print ("********\n NOTE: PLEASE ONLY USE FILES WITH '.fasta' IN THE FILE NAME!\n********\n ")
print ("The first couple test that will be run will be the conversion from DNA -> RNA -> Protein. Along with comparing files and stating where the differences are within those files.")
print ("****REMINDER**** \n This test compares only two files.\n\n")

if __name__ == "__main__":
    import ProtTrans

    print ("\nThe next test that will be run will be the alignment tool. This test will take two files and perform an alignment. It will then proceed to give the alignment score as well as the match percentage between the two files.\n")
    
    import AnalysisTool
