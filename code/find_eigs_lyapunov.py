#! /usr/bin/env python

# Given inputs h and gamma this script will find an appropriate k to ensure that:
# (i) The linear system created as the angle errors (alpha, theta) approaches (0,0)
# is critically damped meaning that the two eigenvalues are the same.
# (ii) The negative of the eigenvalue is greater than gamma meaning that the angle
# errors will converge before the distance error.

from scipy import * # For eig()
from numpy import * # For array()
import sys # For argv

if len(sys.argv) < 2:
    print 'Usage is ./findEigsLyapunov.py <gamma> <h> or ./findEigsLyapunov.py <gamma> <h> <k>'
    sys.exit(1)

if len(sys.argv) > 4:
    print 'Usage is ./findEigsLyapunov.py <gamma> <h> or ./findEigsLyapunov.py <gamma> <h> <k>'
    sys.exit(1)

gamma = float(sys.argv[1])
h = float(sys.argv[2])

if len(sys.argv) == 3:
    k = 2*gamma*sqrt(h)

if len(sys.argv) == 4:
    k = float(sys.argv[3])

print 'k =', k
A = array([[-1*k, -1*h*gamma],[gamma, 0]])
print 'A =', A
V,D = linalg.eig(A)
zeta = V[0].real/V[1].real
print 'alpha eig =', V[0], 'and theta eig =', V[1]
sigma = -V[0].real

if zeta.real == 1:
    print 'System is critically damped since zeta =', zeta

if zeta.real > 1:
    print 'System is overdamped since zeta =', zeta

if zeta.real < 1:
    print 'System is underdamped since zeta =', zeta

if sigma < gamma.real:
    print 'Distance converges FASTER than angles since sigma =', sigma, '<', gamma.real

if sigma > gamma.real:
    print 'Distance converges SLOWER than angles since sigma =', sigma, '>', gamma.real
