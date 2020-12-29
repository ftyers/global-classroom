# Based on code from https://github.com/kchan7/WER-CER
# MIT Licence
#coding:utf-8
import sys
import difflib
import numpy
from difflib import SequenceMatcher

class WER:

    
    def editDistance(self, r, h):
        '''
        This function is to calculate the edit distance of reference sentence and the hypothesis sentence.
    
        Main algorithm used is dynamic programming.
    
        Attributes: 
            r -> the list of words produced by splitting reference sentence.
            h -> the list of words produced by splitting hypothesis sentence.
        '''
        d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
        for i in range(len(r)+1):
            d[i][0] = i
        for j in range(len(h)+1):
            d[0][j] = j
        for i in range(1, len(r)+1):
            for j in range(1, len(h)+1):
                if r[i-1] == h[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    substitute = d[i-1][j-1] + 1
                    insert = d[i][j-1] + 1
                    delete = d[i-1][j] + 1
                    d[i][j] = min(substitute, insert, delete)
        return d
    
    def getStepList(self, r, h, d):
        '''
        This function is to get the list of steps in the process of dynamic programming.
    
        Attributes: 
            r -> the list of words produced by splitting reference sentence.
            h -> the list of words produced by splitting hypothesis sentence.
            d -> the matrix built when calulating the editting distance of h and r.
        '''
        x = len(r)
        y = len(h)
        l = []
        while True:
            if x == 0 and y == 0: 
                break
            elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1] and r[x-1] == h[y-1]: 
                l.append("e")
                x = x - 1
                y = y - 1
            elif y >= 1 and d[x][y] == d[x][y-1]+1:
                l.append("i")
                x = x
                y = y - 1
            elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1]+1:
                l.append("s")
                x = x - 1
                y = y - 1
            else:
                l.append("d")
                x = x - 1
                y = y
        return l[::-1]
    
    def alignedPrint(self, l, r, h, result):
        '''
        This funcition is to print the result of comparing reference and hypothesis sentences in an aligned way.
        
        Attributes:
            l   -> the list of steps.
            r      -> the list of words produced by splitting reference sentence.
            h      -> the list of words produced by splitting hypothesis sentence.
            result -> the rate calculated based on edit distance.
        '''
        print("REF:", end=" ")
        for i in range(len(l)):
            if l[i] == "i":
                count = 0
                for j in range(i):
                    if l[j] == "d":
                        count += 1
                index = i - count
                print(" "*(len(h[index])), end=" ")
            elif l[i] == "s":
                count1 = 0
                for j in range(i):
                    if l[j] == "i":
                        count1 += 1
                index1 = i - count1
                count2 = 0
                for j in range(i):
                    if l[j] == "d":
                        count2 += 1
                index2 = i - count2
                if len(r[index1]) < len(h[index2]):
                    print(r[index1] + " " * (len(h[index2])-len(r[index1])), end=" ")
                else:
                    print(r[index1], end=" "),
            else:
                count = 0
                for j in range(i):
                    if l[j] == "i":
                        count += 1
                index = i - count
                print(r[index], end=" "),
        print("\nHYP:", end=" ")
        for i in range(len(l)):
            if l[i] == "d":
                count = 0
                for j in range(i):
                    if l[j] == "i":
                        count += 1
                index = i - count
                print(" " * (len(r[index])), end=" ")
            elif l[i] == "s":
                count1 = 0
                for j in range(i):
                    if l[j] == "i":
                        count1 += 1
                index1 = i - count1
                count2 = 0
                for j in range(i):
                    if l[j] == "d":
                        count2 += 1
                index2 = i - count2
                if len(r[index1]) > len(h[index2]):
                    print(h[index2] + " " * (len(r[index1])-len(h[index2])), end=" ")
                else:
                    print(h[index2], end=" ")
            else:
                count = 0
                for j in range(i):
                    if l[j] == "d":
                        count += 1
                index = i - count
                print(h[index], end=" ")
        print("\nEVA:", end=" ")
        for i in range(len(l)):
            if l[i] == "d":
                count = 0
                for j in range(i):
                    if l[j] == "i":
                        count += 1
                index = i - count
                print("D" + " " * (len(r[index])-1), end=" ")
            elif l[i] == "i":
                count = 0
                for j in range(i):
                    if l[j] == "d":
                        count += 1
                index = i - count
                print("I" + " " * (len(h[index])-1), end=" ")
            elif l[i] == "s":
                count1 = 0
                for j in range(i):
                    if l[j] == "i":
                        count1 += 1
                index1 = i - count1
                count2 = 0
                for j in range(i):
                    if l[j] == "d":
                        count2 += 1
                index2 = i - count2
                if len(r[index1]) > len(h[index2]):
                    print("S" + " " * (len(r[index1])-1), end=" ")
                else:
                    print("S" + " " * (len(h[index2])-1), end=" ")
            else:
                count = 0
                for j in range(i):
                    if l[j] == "i":
                        count += 1
                index = i - count
                print(" " * (len(r[index])), end=" ")
        print("\nWER: " + result)
    
    def wer(self, r, h):
        """
        This is a function that calculate the word error rate in ASR.
        You can use it like this: wer("what is it".split(), "what is".split()) 
        """
        # build the matrix
        d = self.editDistance(r, h)
    
        # find out the manipulation steps
        l = self.getStepList(r, h, d)
    
        # print the result in aligned way
        result = float(d[len(r)][len(h)]) / len(r) * 100
        #result_s = str("%.2f" % result) + "%"
        #self.alignedPrint(l, r, h, result_s)
    
        #不一致の単語数
        word_error=d[len(r)][len(h)]
        #単語数
        words=len(r)
        return result

    def evaluate(self, ref_lines, tst_lines):
        total = 0.0
        n_lines = 0
        for (r, h) in zip(ref_lines, tst_lines):
            w = self.wer(r.split(' '), h.split(' '))
#            print(w, n_lines)
            total += w
            n_lines += 1

#        print('T:', total, n_lines)
        return total/n_lines

class CER:

    def __init__(self):
        self.x = True
    
    ####関数定義##############################################################################################
    #input:string rows(行番号), string origin_st(正解の文字列), string target_st(比較対象の文字列)
    #return:num charas(語数),num diff_charas(異なる語数) 
    def diffLines(self, rows, origin_st, target_st):
        
        s1=list(origin_st)
        s2=list(target_st)
    
        diff=[]
        num_charas=len(s1)
        num_delete=0
        num_insert=0
        num_replace=0
    
        matcher = difflib.SequenceMatcher(None, s1, s2)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'delete':
                diff.append('del'+''.join(s1[i1:i2]))
                num_delete+=i2-i1
                #print('delete',s1[i1:i2], i1, i2)
            elif tag == 'equal':
                pass
                #print('equal',i1, i2, j1, j2)
            elif tag == 'insert':
                diff.append('ins'+''.join(s2[j1:j2]))
                num_insert+=j2-j1
                #print('insert',s2[j1:j2], j1, j2, i1)
            elif tag == 'replace':
                diff.append('rep'+''.join(s1[i1:i2])+'->'+''.join(s2[j1:j2]))
                num_replace+=i2-i1
                #print('replace',s1[i1:i2], i1, i2, s2[j1:j2], j1, j2)
    
        return num_charas, (num_delete+num_insert+num_replace)
   
    
    ####メイン処理##############################################################################################
    def evaluate(self, ref_lines, tst_lines):
        total_chara=0
        total_diff_chara=0
    
        for i in range(len(ref_lines)):
            str1=ref_lines[i]
            str2=tst_lines[i]
            num_charas, diff_charas = self.diffLines(i+1,str1,str2)
    
            total_chara+=num_charas
            total_diff_chara+=diff_charas
    
#        print("#################################################################")
#        print("Total:"+str(total_chara) + \
#            "  Diff:"+str(total_diff_chara) + \
#            "  CER:"+str(total_diff_chara/total_chara) \
#            )

        return total_diff_chara/total_chara
    
cer = CER()
wer = WER()

ref_lines = [i.strip().split('\t')[1] for i in open(sys.argv[1]).readlines()]
tst_lines = [i.strip().split('\t')[1] for i in open(sys.argv[2]).readlines()]

res = cer.evaluate(ref_lines, tst_lines)

print('CER:', res*100)

res = wer.evaluate(ref_lines, tst_lines)

print('WER:', res)

