# Nested Sampling test problems
Some simple test problems for nested sampling codes (or other Bayesian sampling methods). These include multidimensional normal distributions, [generalized Rosenbrock](https://arxiv.org/abs/1903.09556) distributions, and multidimensional [log-gamma](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loggamma.html) distributions. 

Python scripts to perform each test using MultiNest can be found in the `multiNest` directory. 

The `emcee` directory includes and example MultiNest output, a script to initialize an emcee analysis based of of nested sampling outputs, and a script to run the log-gamma problem using [emcee](https://emcee.readthedocs.io/en/stable/). 

The `ultraNest` directory includes and example MultiNest output and a script to run the log-gamma problem, utilizing the [warm starting](https://johannesbuchner.github.io/UltraNest/example-warmstart.html) feature of the [UltraNest](https://johannesbuchner.github.io/UltraNest/readme.html) sampler.

Results for these test problems are collected in [https://arxiv.org/abs/2404.16928](https://arxiv.org/abs/2404.16928).
