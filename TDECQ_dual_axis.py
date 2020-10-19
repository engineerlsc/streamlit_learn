# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:57:04 2020

@author: shuchao.lv
"""
# C:\Users\shuchao.lv\Desktop\pywork\TDECQ dual axis.py
from numpy import pi, arange, sin, linspace
from bokeh.plotting import output_file, figure, show
from bokeh.models import LinearAxis, Range1d,Title
import streamlit as st
import pandas as pd
import numpy as np


def tdecq_dual_axis(title_text,Data):
    
    hist, bin_edges = np.histogram(Data,density=True)
    # bin_edges =  bin_edges[0:-1]
    hist_normal = hist * np.diff(bin_edges)
    hist_cumsum = np.cumsum(hist_normal)
    
    output_file("dual axis.html")
    title = title_text
    p = figure(plot_width = 500, plot_height = 350,y_range=(0,hist_normal.max()+0.1), toolbar_location = "below")
    p.title.text =  title
    bin_edges =  bin_edges[0:-1]
    p.circle(bin_edges, hist_normal, size = 11,color="red")
    p.line(bin_edges, hist_normal,line_width = 6,line_color="red")
    p.yaxis.axis_line_color = 'red'
    p.yaxis.major_tick_line_color='red'
    p.yaxis.minor_tick_line_color='red'
    p.axis.major_label_text_font_size = '15pt'
    
    p.extra_y_ranges = {"foo": Range1d(start=0, end=1.1)}
    p.circle(bin_edges, hist_cumsum, color="blue", size = 11,y_range_name="foo")
    p.line(bin_edges, hist_cumsum,line_width = 6,line_color="blue",y_range_name="foo")
    p.add_layout(LinearAxis(y_range_name="foo",axis_line_color = 'blue',major_tick_line_color='blue',major_label_text_font_size = '15pt',minor_tick_line_color='blue'), 'right')
    
    
    p.add_layout(Title(text="Distribution_cumsum", align="center",text_color= 'blue'), "right")
    p.add_layout(Title(text="Distribution", align="center",text_color = 'red'), "left")
    
    st.bokeh_chart(p) 
    
    


if __name__ == "__main__":
    Data = pd.read_csv('C:/Users/shuchao.lv/Desktop/1156 tracking error.csv',encoding = 'gbk')
    # for k in [ 'linearity', 'AvgPower','outerER', 'TDECQ', 'OMA', 'OMA-TDECQ', 'LDI(Ma)', 'EA_V(V)',
    #    'EA_I(mA)']:
        
    #     data =Data[k].to_numpy()
    #     tdecq_dual_axis(k,data)
    SN_inuse = Data['ModuleSerialNum'].unique().tolist()
    CHANNEL_inuse = Data['ChannelNumber'].unique().tolist()
    CORNER_inuse =  ['25G1C', '25G3C', '25G1H', '25G3H', '25G2R']
    savefile = 'C:/Users/shuchao.lv/Desktop/data_clean5.txt'
    f = open(savefile,'w')

    Data_inuse = []
    for sn in SN_inuse:
        for channel in CHANNEL_inuse:
            f.write(sn+'\t')
            f.write(str(channel)+'\t')
            for corner in CORNER_inuse:
                data = Data.loc[(Data['ModuleSerialNum']==sn) & (Data['ChannelNumber']==channel) & (Data['CornerID']==corner),'ModuleTxPower']

                
                for value in list(data):
                    f.write(str(value)+'\t')
            f.write('\n')
    f.close()
    
        
    

