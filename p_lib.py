#! /usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import matplotlib 

import json



def data_parser(file_path = "", value_type = "INT"):
	'''
	In:		file_path = "/directory/to/file.txt"
			value = "INT" or "FLOAT"
	Out:	data = [ [values] ]
	''' 
	with open(file_path, "r") as df:
		lines = df.readlines()
		data_str = [line.strip("\n").split(" ") for line in lines]
	if value_type == "INT":
		data = [[int( float(number) ) for number in d] for d in data_str]
	elif value_type == "FLOAT":
		data = [[float(number) for number in d] for d in data_str]
	return data



def plot_hist(data, usr_params, default_params, saving_path, save = False):
	"plot histograms"
	fig, ax = plt.subplots()
	x_axis = np.arange( len(data) ) 
	bar_width = 0.25
	opacity = 0.8
	error_config = {'ecolor': '0.3'}

	rects = [ 
				plt.bar(x_axis+(i*bar_width), [d[i] for d in data], bar_width,
          		       	alpha=opacity,
           		      	color=default_params["Colours"][i],
            	  	   	error_kw=error_config,
            	  	   	label=usr_params["Histos"][i])
				for i in range( len(data[0]) )  
			]

	plt.ylim( ( 0 , int(1.5 * max(max(data)) ) ) )
	#plt.ylim( ( 0 , 10 ) )

	plt.xlabel(usr_params["X_Axis"], fontsize=int(default_params["X_font"]) )
	plt.ylabel(usr_params["Y_Axis"], fontsize=int(default_params["Y_font"]) )

	plt.xticks(fontsize=int(default_params["X_axis_font"]) )
	plt.yticks(fontsize=int(default_params["Y_axis_font"]) )

	plt.xticks(x_axis + 1*bar_width, x_axis, fontsize=int(default_params["X_axis_font"]) )
	plt.legend(prop={'size': int(default_params["Legend_font"]) } )
	plt.title(usr_params["Title"], fontsize = int(default_params["Title_font"]) )
	
	if save:
		plt.savefig(saving_path, bbox_inches='tight')
	else:
		plt.show()



def plot_curv(data, usr_params, default_params, saving_path, save = False):
	"plot curves"
	fig, ax = plt.subplots()
	x_axis = np.arange( len(data) ) 

	plt.ylim((0, 2*int( max(max(data)) ) ))
	plt.xlabel(usr_params["X_Axis"], fontsize=int(default_params["X_font"]))
	plt.ylabel(usr_params["Y_Axis"], fontsize=int(default_params["Y_font"]))

	plt.xticks(fontsize=int(default_params["X_axis_font"]))
	plt.yticks(fontsize=int(default_params["Y_axis_font"]))
	
	Ps = [ plt.plot(x_axis, [d[i] for d in data], default_params["Colours"][i]+default_params["Shapes"][i], label=usr_params["Histos"][i], markersize=15, linewidth = 3.0)  for i in range(len(data[0])) ]	
	
	plt.legend(prop={'size':20})

	fig.suptitle(usr_params["Title"], fontsize = int(default_params["Title_font"]) )
	plt.subplots_adjust(top=0.92)
	if save:
		plt.savefig(saving_path, bbox_inches='tight')
	else:
		plt.show()


