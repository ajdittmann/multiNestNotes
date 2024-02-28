import numpy as np
import emcee
from scipy.stats import loggamma as logg

filename = "gamma_test.npy"

ndim = 10
nwalkers = 1024

twothirds = 2.0/3.0
sig = 10.0**np.linspace(-2.0,  -1.3, ndim)

ubounds = np.ones(ndim)*2
lbounds = -10*np.ones(ndim)

def logp(x):
  count = np.sum(x<lbounds)+np.sum(x>ubounds)
  if count>0: return -np.inf
  return 0.0

def lndi(xi, i):
  return logg.logpdf(xi, c=1.0, loc = twothirds, scale = sig[i])

def logl(x):
  like = sum([lndi(xi, i) for i, xi in enumerate(x)])
  return like

def logprob(x):
  return logl(x) + logp(x)

sampler = emcee.EnsembleSampler(nwalkers, ndim, logprob)

iters = 10
adnauseum = 1000

while(adnauseum>0):
  chain = np.load(filename)
  init = chain[:,-1,:]

  for p, lnprob, lnlike in sampler.sample(init,iterations=iters):
    pass
  print("Mean acceptance fraction:",np.mean(sampler.acceptance_fraction))
  pchain = sampler.chain

  chain = np.append(chain,pchain,axis=1)
  print(chain.shape)
  np.save(filename,chain)
  sampler.reset()
  adnauseum = adnauseum-1


