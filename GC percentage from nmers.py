
#FUNCTION NAME: Table2Xls
#PARAMETERS: 2 (A list of nmers, name of excel file)
#PURPOSE: For each nmer in the list, count the number of G's and C's and calculate the GC percentage.
#         Write the nmer, count, and GC percentage to an output excel file.
#         [NOTE: Write a "Tab" between each field. Write a "Newline" at the end of each line.]
#RETURN VALUES: The Name of the Output Excel File.

#== FUNCTION 2 ==
def Table2Xls(nmer_tablist,fs):
    count_gc = 0.0
    total_gc = 0.0
    avg_gc = 0.0
    percent_gc = 0.0
    gc = []
    per = []
    
    for i in range(0,len(nmer_tablist)):
        fin = open(fs,'w')
        for k in range(0,len(nmer_tablist[i])):
            if nmer_tablist[i][k] == "G" or nmer_tablist[i][k] == "C":
                count_gc += 1
                percent_gc = (count_gc/len(nmer_tablist[i]))*100
                gc.append(count_gc)
                per.append(percent_gc)
                
                fin.write(nmer_tablist[i])
                fin.write("\t")
                for j in range(0,len(gc)):
                    fin.write(gc[j])
                    fin.write("\t")
                    fin.write(per[j])
                fin.write("\n")
                #fin.write(count_gc)
                #fin.write(percent_gc)
        print nmer_tablist[i],"\t",count_gc,"\t",percent_gc
        print per
        total_gc += percent_gc
        count_gc = 0.0

    fin.close()
    return fs

#EXAMPLE:
nmer_tablist=["AAUG","GCGA","AGCG","TCGA"]
fo=Table2Xls(nmer_tablist, 'nmer.xls')
#print fo

