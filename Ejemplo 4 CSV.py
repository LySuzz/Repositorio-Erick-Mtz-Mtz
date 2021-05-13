import numpy as np 
list_rows = [ ['ABC', 'COE', '2', '9.0'],['TUV', 'COE', '2', '9.1'], ['XYZ', 'IT', '2', '9.3'],['PQR', 'SE', '1', '9.5']]  
np.savetxt("numpy_test.csv", list_rows, delimiter =",",fmt ='% s')