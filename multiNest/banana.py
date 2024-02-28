import numpy as np
from pymultinest.solve import solve

#based on https://arxiv.org/abs/1903.09556

a = 2.0

def runsim(n1, n2, nlive, eff, outname):
  ndim = (n1 - 1)*n2 + 1
  bs = 0.01*10.0**np.linspace(2.0, 3.0, ndim - 1)
  ubounds = np.ones(ndim)*50
  lbounds = -50*np.ones(ndim)
  diff = ubounds-lbounds

  norm = np.sqrt(a)/np.sqrt(np.pi**ndim)
  for i in range(1, n1):
    for j in range(0, n2):
      ind = j*(n1-1)+i-1
      norm = norm*np.sqrt(bs[ind])
  norm = np.log(norm)

  def prior(theta):
    x = lbounds + diff*theta
    return x

  def logl(x):
    val = 0.0
    for ji in range(0,n2):
      for ii in range(1,n1):
        ind = ji*(n1-1)+ii-1
        val += bs[ind]*(x[ind] - x[ind-1]**2)**2.0
    like = -a*x[0]**2 - val + norm
    return like

  results = solve(LogLikelihood = logl, Prior = prior, n_dims = ndim, outputfiles_basename=outname, n_live_points = nlive, sampling_efficiency=eff, verbose=True, importance_nested_sampling=False, evidence_tolerance=0.00001, max_modes = 1000)

nlive = 300
n1 = 2
n2 = 1
eff = 0.1
outname = "test"

runsim(n1, n2, nlive, eff, outname)
