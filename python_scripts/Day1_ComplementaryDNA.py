# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:26:30 2021
A funtion to find the complementary DNA strand
@author: ireekie
"""

def complementary(base):
    #This function returns a complementary base
    #input is a nucleotide (T,A,C or G)
    #output is the complementary nucleotide
    output = None
    if base=="A":
        output="T"
    elif base=="T":
        output="A"
    elif base=="C":
        output="G"
    elif base=="G":
        output="C"
    else: 
        output="*"
    #print(output)        
    return output
     

def complementaryDNAstrand (strand):
    #this function uses the function above to return a full sequence
    #input is a DNA strand 
    #print(strand)
    complementarystrand = " "
    for n in strand:
        x = complementary(n)
        complementarystrand = complementarystrand + x
    print(complementarystrand)
    return(complementarystrand)
        
    
sequence="ATGCCCT"     
print(sequence)
Complement_strand = complementaryDNAstrand(sequence) 
             

def reversestring (string):
    return string[::-1]

print(reversestring(Complement_strand))

