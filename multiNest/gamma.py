import numpy as np
from pymultinest.solve import solve
from scipy.stats import loggamma as logg

twothirds = 2.0/3.0
def runsim(ndim, nlive, eff, outname):

  sig = 10.0**np.linspace(-2.0,  -1.3, ndim)
  ubounds = np.ones(ndim)*2
  lbounds = -10*np.ones(ndim)
  diff = ubounds-lbounds

  def prior(theta):
    x = lbounds + diff*theta
    return x

  def lndi(xi, i):
    return logg.logpdf(xi, c=1.0, loc = twothirds, scale = sig[i])

  def logl(x):
    like = sum([lndi(xi, i) for i, xi in enumerate(x)])
    return like

  results = solve(LogLikelihood = logl, Prior = prior, n_dims = ndim, outputfiles_basename=outname, n_live_points = nlive, sampling_efficiency=eff, verbose=True, importance_nested_sampling=False, evidence_tolerance=0.00001, max_modes=4000)


ndim = 3
nlive = 1000
eff = 0.1
outname = "test"

runsim(ndim, nlive, eff, outname)
