import numpy as np
from scipy.stats import gaussian_kde as gkde

f = 0.1

output_format = 'emcee'
nwalkers = 1024

infile = "e0.1_v8.txt"
intype = 'mn'
output_name = "gamma_test.npy"

def silver(ndim, weights):
  neff = np.sum(weights)**2/np.sum(weights**2)
  return (neff*(ndim + 2)*0.25)**(-1.0/(ndim+4))

if intype == 'mn':
  mndat = np.loadtxt(infile)
  data = mndat[:,2:]
  weights = mndat[:,0]

ndim = len(data[0,:])

if output_format == 'emcee':
  kde = gkde(data.T, bw_method=silver(ndim, weights)*f, weights=weights)
  output = np.empty((nwalkers,1,ndim))
  vals = kde.resample(nwalkers)
  output[:,0,:] = vals.T

np.save(output_name, output)
