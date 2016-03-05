#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import matplotlib 
import json

import p_lib



if __name__ == "__main__":
	
	data_file = "../results/efc/efc_1.txt"

	Data_1 = p_lib.data_parser(data_file, "FLOAT")

	with open("./usr_params.txt", "r") as df:
		line = df.read()
	usr_param_decode = json.loads(line)

	with open("./default_params.txt", "r") as df:
		line = df.read()
	default_param_decode = json.loads(line)

	p_lib.plot_hist(Data_1, usr_param_decode, default_param_decode, saving_path = "", save = False)
	#p_lib.plot_curv(Data_1, usr_param_decode, default_param_decode, saving_path = "", save = False)


