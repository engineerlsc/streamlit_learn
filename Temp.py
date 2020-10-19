# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:06:37 2020
@author: shuchao.lv
"""
# streamlit run C:\Users\shuchao.lv\Desktop\pywork\Temp.py

import streamlit as st
import pandas as pd
import numpy as np
import math
from bokeh.io import output_file,show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import scipy
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from bokeh.plotting import figure, output_file, show
from bokeh.models import Arrow, OpenHead, NormalHead, VeeHead




class Tem(object):
    def __init__(self):
        
        self.unit = 'dB'
        self.TorR = 'R'
        self.X1  = ['D110008','D110010','D110001']# x1
        
        self.X2 = ['Ch1','Ch2','Ch3','Ch4'] # x2
        
        self.labels = ['40℃','50℃','60℃','70℃','80℃'] # labels

        self.colors =  [ '#766AB3', '#CD0000','#BC7431','#B7AD48','#0F7542','#3C73B0','#6AB38F','#CDB79E','#CDB5CD','#CDB38B',
	'#CDAF95', 		'#CDAD00', 		'#CDAA7D', 		'#CD9B9B',
	'#CD9B1D', 		'#CD96CD', 		'#CD950C', 		'#CD919E',
	'#CD8C95', 		'#CD853F', 		'#CD8500',		'#CD8162',
	'#CD7054', 		'#CD69C9', 		'#CD6889',		'#CD6839',
	'#CD661D', 		'#CD6600', 		'#CD6090',		'#CD5C5C',
	'#CD5B45', 		'#CD5555', 		'#CD4F39', 		'#CD3700',
	'#CD3333', 		'#CD3278', 		'#CD2990', 		'#CD2626',
	'#CD1076',		'#CD00CD', 		'#CD0000', 		'#CCCCCC',
	'#CAFF70', 		'#CAE1FF', 		'#C9C9C9', 		'#C7C7C7',
	'#C71585', 		'#C6E2FF', 		'#C67171',		'#C5C1AA',
	'#C4C4C4', 		'#C2C2C2', 		'#C1FFC1',		'#C1CDCD','#8C50AD']

        
    def linescan_SN(self,Data,title,yRange = (-3,3),compare = 0,Spec = 0): # data_step: 代表一组数据有多少个：
    
        output_file("lines.html")
        
        cols = self.colors
        
        X1 = self.X1
        X2 = self.X2
        labels =self.labels
        x = [(x1,x2) for x1 in X1 for x2 in X2  ] # x1 最底下坐标，x2 次坐标
        

        p = figure(x_range= FactorRange(*x),y_range =yRange,plot_height=350, toolbar_location='below')
        
        NUM = len(self.X2)
        for j in range(0,Data.shape[1]):
            if compare>0:
                p.line(x=x, y=-0.5, color='red', line_width=4,line_dash = 'dashed')
                p.line(x=x, y=0.5, color='red', line_width=4,line_dash = 'dashed')
            else:
                p.line(x=x, y=Spec, color='red', line_width=4,line_dash = 'dashed')
            for i in range(len(X1)):
                p.line(x=x[NUM*i:NUM*i+NUM], y=Data[NUM*i:NUM*i+NUM,j], color=cols[j], line_width=5,legend_label = labels[j])
                
                p.scatter(x=x[NUM*i:NUM*i+NUM], y=Data[NUM*i:NUM*i+NUM,j], color=cols[j], line_width=5,legend_label= labels[j])

        p.title.text =  title
        # p.y_range.start = 0
        p.x_range.range_padding = 0.1
        # p.y_range.range_padding = 0.1
        p.xaxis.major_label_orientation = 0
        p.legend.orientation = 'horizontal'
        p.xgrid.grid_line_color = None
        p.yaxis.axis_label = self.unit
        # p.yaxis.axis_label_text_font = '90'
        p.xaxis.axis_label_text_font_size = '20pt'
        p.yaxis.axis_label_text_font_size = '20pt'
        p.xaxis.major_label_text_font_size = '15pt'
        p.yaxis.axis_label_text_font_size = '15pt'
        p.yaxis.major_label_text_font_size = '15pt'
        p.legend.location = 'bottom_center'
        # p.add_layout(Arrow(end=VeeHead(size=35), line_color="red",
        #            x_start=0.5, y_start=0.7, x_end=0, y_end=0))

        p.legend.background_fill_color ='red'
        p.legend.background_fill_alpha = 0
        p.legend.label_text_font_size = '15pt'
        p.xaxis.axis_line_dash = 'solid'
        # p.legend =9
        st.bokeh_chart(p) 
        
        
    def linescan_SN2(self,Data,title,yRange = (-3,3),compare = 0): # data_step: 代表一组数据有多少个：
# e.g  data_step =4 ： ch1,ch2,ch3,ch4
# e.g  data_step =8 ： ch1 EA on,ch1 EA off,...,ch4 EA_on, ch4 EA_off       
        output_file("lines.html")
        
        cols = self.colors
        
        X1 = self.X1
        X2 = self.X2
        labels =self.labels
        x = [(x1,x2) for x1 in X1 for x2 in X2  ] # x1 最底下坐标，x2 次坐标
        

        p = figure(x_range= FactorRange(*x),y_range =yRange,plot_weight = 500,plot_height=550, toolbar_location='below')
        

        for j in range(0,Data.shape[1]):
            if compare>0:
                p.line(x=x, y=-0.1, color='red', line_width=2,line_dash = 'dashed')
                p.line(x=x, y=0.1, color='red', line_width=2,line_dash = 'dashed')
            for i in range(len(X1)):
                if i < (len(X1)-1):
                    p.line(x=x[4*i:4*i+4], y=Data[4*i:4*i+4,j], color=cols[j], line_width=4,legend_label = labels[j])
                    
                    p.scatter(x=x[4*i:4*i+4], y=Data[4*i:4*i+4,j], color=cols[j], line_width=4,legend_label= labels[j])
                else:
                    p.line(x=x[4*i:4*i+4], y=Data[4*i:4*i+4,j], color=cols[j+4], line_width=4,legend_label = labels[j+4])
                    
                    p.scatter(x=x[4*i:4*i+4], y=Data[4*i:4*i+4,j], color=cols[j+4], line_width=4,legend_label= labels[j+4])
                    
        p.title.text =  title
        # p.y_range.start = 0
        p.x_range.range_padding = 0.1
        p.xaxis.major_label_orientation = 0
        p.legend.orientation = 'horizontal'
        p.xgrid.grid_line_color = None
        p.yaxis.axis_label = self.unit
        p.yaxis.axis_label_text_font = '40'
        # p.legend.location = 'bottom_center'
        p.legend.location = 'left'
        p.legend.orientation = 'horizontal'
        p.legend.background_fill_color ='red'
        p.legend.background_fill_alpha = 0
        st.bokeh_chart(p) 
        
        
def plot_compare(Data,Title,units,labels,X2,X1,TorR = 'T',compare_phase = ''): # 如果compare_phase = ‘’  就不进行比较

    a = Tem()
    # Title='D120004'
    # a.labels = ['ouched','Untouched','Ch0 Max','Ch1 Max','Ch2 Max','Ch3 Max']

    # a.labels =['Far Peak','Angle Balance','Position Balance','Near Peak','Near Balance Power','Post UV','Fixture Loose','Baking','TC'][-5:]
    # a.labels = ['Baking-Low Temp','Baking-High Temp','TC-Low Temp','TC-High Temp','Co-Low Temp','Co-High Temp','CoTC-Low Temp','CoTC-High Temp']
    # a.labels = ['Module','- up shell','with cover','straighten fiber','remove Cover','On Aligner']
    # a.labels = [i+temp for i in['Baking','TC','Covwe','Cover TC']]
    # a.labels = ['HK RT','HK HT','TC RT','TC HT','Co RT','Co HT','MK RT','MK HT'][-2:]
    # a.labels = ['OSA','Module']
    # a.labels = ['Lens1','Mux UV']
    # a.labels = ['HVHT','HVLT','LVHT','LVLT','RVRT']

    # a.labels= ['Pre-UV new collimator','Pre-UV old collimator']
    # a.labels = ['Vacuum on & Push','Vacuum off & Push', 'Vacuum Re-On & no Push', 'Vacuun on & no push',
                # 'Vacuum Re-On & Push','Vacuum off & push','off aligner','on shell']
    a.labels = labels
    a.unit = units[0]
    a.X1 = X1
    a.X2 = X2
    title =Title

    min_value = Data.min()
    max_value = Data.max()
    # a.linescan_SN(Data,title,yRange =  (0.6,0.9),compare = 0,Spec = 0.7)
    
    a.linescan_SN(Data,title,yRange = (min_value,1.3*max_value),compare = 0,Spec = [0.7,2.5][TorR == 'T'])
    # a.linescan_SN(Data,title,yRange =  (0,0.8),compare = 0,Spec = 0.7)
    if compare_phase !='':
        if TorR == 'T':
            Data = (np.array(np.mat(Data)-np.mat(np.tile(Data[:,compare_phase].reshape(-1,1),(1,Data.shape[1])))))
        elif TorR == 'R':
            
            Data = 10*np.log10((np.array(np.mat(Data)/np.mat(np.tile(Data[:,compare_phase].reshape(-1,1),(1,Data.shape[1]))))))
        elif TorR == 'A':
            Data = (np.array(np.mat(Data)-np.mat(np.tile(Data[:,compare_phase].reshape(-1,1),(1,Data.shape[1]))))) 
        title =r"Compare " +Title
        
        a.unit =units[1]
        
        min_value = Data.min()
        max_value = Data.max()
        a.linescan_SN(Data,title,yRange = (min_value-1,1.7*max_value),compare = 1)
    else:
        pass
    
        
        
if __name__ =='__main__':

    path = 'C:/Users/shuchao.lv/Desktop/'
    fname = path+'data_clean4.txt'
    

    coefficient_la =[1.052150464,
1.063997405,
0.96631142,
0.984240688
]
    coefficient_osa = [1.05931418,
1.040169133,
1.05877551,
1.064490446
]

    
    Data = np.loadtxt(fname)

    TorR ='T'
    # Data[:,0] = Data[:,0]*np.array(coefficient_la*12)
    # Data[:,1] = Data[:,1]*np.array(coefficient_la*12)
    # Data[:,2] = Data[:,2]*np.array(coefficient_la*12)
    # Data[:,3] = Data[:,3]*np.array(coefficient_la*12)
    # Data[:,4] = Data[:,4]*np.array(coefficient_la*12)
    
    title = {'T': 'TDECQ','R':'Rx Resp','A':'Relative Angle'}
    
    Title = '400G {} in different phase'.format(title[TorR])

    path = fname
    # units = ['dBm','dB']

    # labels = ['1st time ','2nd time','3rd time','4th time']
    # labels = ['TC','TC Shell']

    # labels = ['Pre-UV','Post-UV','Fixture Loose','Baking','TC']
    labels = ['RT-R&D', 'LT-R&D', 'HT-R&D', 'RT-Part', 'LT-Part', 'HT-Part']
    # labels = ['RT','HT']
    # labels = ['Fiter',' Fiber Holder',' Fiber Holder TC','Mudule','RT OSA Lab']
    # labels  = ['HT','LT','RT']
    # labels  = ['Pre-UV','After-UV','Baking','After TC']
    # labels = ['Fiter','RT OSA Lab']
    # units = ['Resp A/W','dB']
    # a = Tem()
    # Title='D120004'



    X2 =  {'R':['3','2','1','0'],
              'T':['1','2','3','4'],
              'A':['1','2','3','4']}



#     X1 =  [
#         '190001',
#         '190002',
#       '190003',
# '190004',

#       '190005',
# '190007',
#       '190008',
# '190009',
#       '190012',
#       '190013',
#       '190014',
#        '190016]
    # X1 = ['FR1G2-A261',
    # 'FR1G2-A272',
    # 'FR1G2-A267',
    # 'FR1G2-A280',
    # 'FR1G2-A282',
    # 'FR1G2-A277'
    #         ]
#     X1= ['210001',
#  '210002',
#  '210003',
#  '210004',
#  '210005',
#  '210006'
# ]
    # X1 =['LA04008-normal lens1 shim','LA04020-lens1 shims 20μm short ']
    X1 = ['D190011',
 'D190012',
 'D190013',
 'D190008']
    # X1 = ['D210001','D210002','D210003','D210004','D210005','D210006']
    # X1= ['A04002 normal','A04004 20 μm','A04008 normal','A04009 normal','A04010 40 μm','A04020 20 μm'] 
   #  X1 = ['190001',
   # '190002',
   # '190003',
   # '190004',
   # '190005',
   # '190007',
   # '190008',
   # '190009',
   # '190012',
   # '190013',
   # '190014',
   # '190016']
    #        X1 = ['190001',
    # '190002',
    # '190003',
    # '190004',
    # '190005',
    # '190006',
    # '190007',
    # '190008',
    # '190009',
    # '190010',
    # '190011',
    # '190012',
    # '190013',
    # '190014',
    # '190015',
    # '190016']
    # X1 = ['D190012', 'D190014']

    unit = {'R':['Resp(A/W)','dB'],
             'T':['dB','dB'],
             'A':['°','°']}

    units = unit[TorR]
    plot_compare(Data,Title,units,labels,X2[TorR],X1,TorR = TorR ,compare_phase =0)



    
    # df = pd.read_csv('C:/Users/shuchao.lv/Desktop/allRx.csv',encoding = 'gbk')
    # df2 = pd.DataFrame(columns = ['PartNumber','Resp','channels'])
    # channel_power = ['Channel_1_RSSI','Channel_2_RSSI','Channel_3_RSSI','Channel_4_RSSI']
    # for num in df.index:
    #     for i in range(4):
    #         df2.loc[4*num+i,['PartNumber']] = df.loc[num,'PartNumber']
    #         df2.loc[4*num+i,['Resp']] = df.loc[num,channel_power[i]]
    #         df2.loc[4*num+i,['channels']] = channel_power[i][:10]
                
                


    
    # fig =px.box(df2, y="Resp", x='channels', color = 'channels',
    #             points ='all',template ='seaborn',boxmode='group',notched = False,orientation= 'v',
    #             width =800,height = 800,range_y = [0.5,1],title = 'distribution')
    # st.plotly_chart(fig)
 

    
