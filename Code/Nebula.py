import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

class Nebula:
	def __init__(self):
		pass

	def from_prior(self):
		self.N = 100
		self.x = rng.randn(self.N)
		self.y = rng.randn(self.N)
		self.w = rng.randn(self.N)
		self.f = rng.randn(self.N)

		prob = rng.rand()
		scale = -np.log(1. - rng.rand())
		for i in xrange(0, self.N):
			if rng.rand() <= prob:
				which = rng.randint(self.N)
				self.x[i] += self.x[which]
				self.y[i] += self.y[which]
				self.w[i] += self.w[which]
				self.f[i] += self.w[which]

		self.w = np.exp(self.w)
		self.f = np.exp(self.f)

	def evaluate(self, xx, yy):
		result = 0.*xx
		for i in xrange(0, self.N):
			result += self.f[i]/(self.w[i]*np.sqrt(2.*np.pi))*np.exp(-0.5*((xx - self.x[i])**2 + (yy - self.y[i])**2)/self.w[i]**2)
		return result

if __name__ == '__main__':
	x = np.linspace(-10., 10., 1001)
	y = np.linspace(-10., 10., 1001)
	[x, y] = np.meshgrid(x, y)
	y = y[::-1, :]

	n = Nebula()

	plt.ion()
	plt.hold(False)
	for i in xrange(0, 100):
		n.from_prior()
		plt.imshow(n.evaluate(x, y), extent=[x.min(), x.max(), y.min(), y.max()],
				interpolation='nearest')
		plt.title((i+1))
		plt.draw()

	plt.ioff()
	plt.show()

