import numpy as np
from pymultinest.solve import solve

def runsim(ndim, nlive, eff, outname):

  sig = np.linspace(0.1, 0.5, ndim)
  ubounds = np.ones(ndim)*20
  lbounds = -20*np.ones(ndim)
  diff = ubounds-lbounds

  norm = np.log((2.0*np.pi)**(ndim*0.5)*np.prod(sig))

  def prior(theta):
    x = lbounds + diff*theta
    return x

  def logl(x):
    like = -0.5*np.sum((x/sig)**2.0) - norm
    return like

  results = solve(LogLikelihood = logl, Prior = prior, n_dims = ndim, outputfiles_basename=outname, n_live_points = nlive, sampling_efficiency=eff, verbose=True, importance_nested_sampling=False, evidence_tolerance=0.00001)


ndim = 3
nlive = 1000
eff = 0.1
outname = "test"

runsim(ndim, nlive, eff, outname)
