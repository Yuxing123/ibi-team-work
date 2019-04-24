# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:12:09 2019

@author: 52935
"""

import re
def mRNA_protein(RNA_string):        
    start_code = 'AUG'       
    protein_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',                      
                     'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',                      
                     'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',                     
                     'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',                      
                     'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',                    
                     'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',                     
                     'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',                     
                     'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',                     
                     'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',                   
                     'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',                   
                     'UAA': 'stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',                   
                     'UAG': 'stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',                  
                     'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',                     
                     'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',                  
                     'UGA': 'stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',                  
                     'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }        
    start_sit = re.search(start_code, RNA_string)  
    protein = ''      
    for sit in range(start_sit.start(), len(RNA_string), 3): 
           protein = protein + protein_table[RNA_string[sit:sit+3]] 
    protein = re.sub(r'stop[A-Z]+','',protein)
    print('the protein sequence is',protein)
        

DNA = input("give me a sequence of DNA : ")
DNAs = list(DNA)
myDict = {}
for i in DNAs:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
count = (myDict['G'] + myDict['C'])/(myDict['A']+myDict['T']+myDict['C']+myDict['G'])
print('the GC content is %.1f%%'%(count*100))
translation = DNA[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
print('the complementary DNA strand (from 5’ to 3’) is',translation)
mRNA = DNA.replace('A','u').replace('T','a').replace('C','g').replace('G','c').upper()
print('the mRNA sequence is', mRNA)
mRNA_protein(mRNA)
