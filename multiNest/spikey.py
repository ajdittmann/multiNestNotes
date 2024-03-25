import numpy as np
from pymultinest.solve import solve
from scipy.interpolate import UnivariateSpline as spline

amp = 0.5
np.random.seed(0)
N = 100000
noise = amp*np.random.uniform(-1,1, N)
nx = np.linspace(-20,20, N)
fit = spline(nx, noise, k=1, s=0)
np.random.seed()

def runsim(ndim, nlive, eff, tol, outname):

  sig = np.linspace(0.1, 0.5, ndim)
  ubounds = np.ones(ndim)*20
  lbounds = -20*np.ones(ndim)
  diff = ubounds-lbounds

  def prior(theta):
    x = lbounds + diff*theta
    return x

  def logl(x):
    ns = []
    for i in range(ndim): ns.append(fit(x[i]))
    like = -0.5*np.sum((x/sig)**2.0) + np.sum(np.array(ns))
    return like

  results = solve(LogLikelihood = logl, Prior = prior, n_dims = ndim, outputfiles_basename=outname, n_live_points = nlive, sampling_efficiency=eff, verbose=True, importance_nested_sampling=False, evidence_tolerance=tol)

ndim = 10
nlive = 1000
eff = 0.1
tol = 0.01
outname = "test"

runsim(ndim, nlive, eff, tol, outname)
