import numpy as np
from scipy.stats import loggamma as logg
from ultranest.integrator import warmstart_from_similar_file
from ultranest import ReactiveNestedSampler

ndim = 10
twothirds = 2.0/3.0

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

posterior_upoints_file = "e0.1_v8_unit.txt"

parameters = []
for i in range(10): parameters.append(str(i))

aux_paramnames, aux_log_likelihood, aux_prior_transform, vectorized = warmstart_from_similar_file(posterior_upoints_file, parameters, logl, prior)

sampler = ReactiveNestedSampler(aux_paramnames, aux_log_likelihood, aux_prior_transform, vectorized=vectorized, log_dir="chains")
res = sampler.run()
