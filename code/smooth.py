# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:41:49 2018

@author: Administrator
"""

import numpy
import random
import pandas as pd
import scipy.special as special
import math
from math import log

class HyperParam(object):
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def sample_from_beta(self, alpha, beta, num, imp_upperbound):
        #产生样例数据
        sample = numpy.random.beta(alpha, beta, num)
        I = []
        C = []
        for click_ratio in sample:
            imp = random.random() * imp_upperbound
            #imp = imp_upperbound
            click = imp * click_ratio
            I.append(imp)
            C.append(click)
        return pd.Series(I), pd.Series(C)

    def update_from_data_by_FPI(self, tries, success, iter_num, epsilon):
        #更新策略
        #self.alpha,self.beta = self.update_from_data_by_moment(tries,success)
        print("初始值alpha:{0},beta:{1}".format(self.alpha,self.beta))
        for i in range(iter_num):
            print (i)
            new_alpha, new_beta = self.__fixed_point_iteration(tries, success, self.alpha, self.beta)
            print(new_alpha,"-------->",new_beta)
            if abs(new_alpha-self.alpha)<epsilon and abs(new_beta-self.beta)<epsilon:
                break
            self.alpha = new_alpha
            self.beta = new_beta
			
    def __compute_moment(self, tries, success):
        '''moment estimation'''
        ctr_list = []
        var = 0.0
        for i in range(len(tries)):
            ctr_list.append(float(success[i])/(tries[i] + 0.000000001))
        mean = sum(ctr_list)/len(ctr_list)
        for ctr in ctr_list:
            var += pow(ctr-mean, 2)

        return mean, var/(len(ctr_list)-1)
            
    def update_from_data_by_moment(self, tries, success):
        '''estimate alpha, beta using moment estimation'''
        mean, var = self.__compute_moment(tries, success)
        #print 'mean and variance: ', mean, var
        #self.alpha = mean*(mean*(1-mean)/(var+0.000001)-1)
        self.alpha = (mean+0.000001) * ((mean+0.000001) * (1.000001 - mean) / (var+0.000001) - 1)
        #self.beta = (1-mean)*(mean*(1-mean)/(var+0.000001)-1)
        self.beta = (1.000001 - mean) * ((mean+0.000001) * (1.000001 - mean) / (var+0.000001) - 1)
        return self.alpha,self.beta

    def __fixed_point_iteration(self, tries, success, alpha, beta):
        #迭代函数
        
        sumfenzialpha = 0.0
        sumfenzibeta = 0.0
        sumfenmu = 0.0
        sumfenzialpha = (special.digamma(success+alpha) - special.digamma(alpha)).sum()
        sumfenzibeta = (special.digamma(tries-success+beta) - special.digamma(beta)).sum()
        sumfenmu = (special.digamma(tries+alpha+beta) - special.digamma(alpha+beta)).sum()
		
        return alpha*(sumfenzialpha/sumfenmu), beta*(sumfenzibeta/sumfenmu)
        '''
        numerator_alpha = 0.0
        numerator_beta = 0.0
        denominator = 0.0
        for i in range(len(tries)):
            numerator_alpha += (special.digamma(success[i] + alpha) - special.digamma(alpha))
            numerator_beta += (special.digamma(tries[i] - success[i] + beta) - special.digamma(beta))
            denominator += (special.digamma(tries[i] + alpha + beta) - special.digamma(alpha + beta))

        return alpha * (numerator_alpha / denominator), beta * (numerator_beta / denominator)
        '''
