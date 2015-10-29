'''
Created on 28/02/2011
@author: root
'''
import numpy as np
import matplotlib.pyplot as plt
'''
#*****************************************************************************80
# EM applies the Euler-Maruyama method to a linear SDE with additive noise.
#  Discussion:
#    The SDE is 
#    dX = lambda * X dt + mu*dW,   
#    X(0) = Xzero,
#    where 
#
#      lambda = 1,
#      mu = 1,
#      Xzero = 1.
#
#   The discretized Brownian path over [0,1] uses
#   a stepsize dt = 2^(-8).
#
#   The Euler-Maruyama method uses a larger timestep Dt = R*dt,
#   where R is an integer.  For an SDE of the form
#
#   dX = f(X(t)) dt + dW(t)
#   it has the form
#   X(j) = X(j-1) + f(X(j-1)) * Dt + X(j-1) * ( W(j*Dt) - W((j-1)*Dt) )
#            Modified:
#
#    28/Feb/20011
#
#  Author:
#    Saul Diaz Infante Velasco. Code base in 
#    Desmond Higham
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546
#
#*******************************************************************************************************  
#%  Set problem parameters.
'''
class SDEtest:
	def graficaEM(self):
		
		w = 1.0
		fig_width_pt = 397 * w					# Get this from LaTeX using \showthe\columnwidth
		inches_per_pt = 1.0 / 72.27					# Convert pt to inch
		golden_mean = (np.sqrt(5) - 1.0) / 2.0		# Aesthetic ratio
		fig_width = fig_width_pt * inches_per_pt	# width in inches
		fig_height = fig_width * golden_mean		# height in inches
		fig_size =  [fig_width, fig_height]
		params={
				#'backend': 'WXAgg',
				'backend': 'ps',
				'axes.labelsize': 10,
				'text.fontsize': 10,
				'legend.fontsize': 8,
				'xtick.labelsize': 8,
				'ytick.labelsize': 8,
				'text.usetex': True,
				'figure.figsize': fig_size
			}
		plt.rcParams.update(params)
		#
		plt.figure()
		plt.axes([0.095,0.1,.87,.87])
		plt.ylim((self.Xemm.min()-0.5, self.Xemm.max()+0.5))
		plt.plot(self.t[0:np.int(self.N+1):self.P],self.Xt,'k-',alpha=0.7,lw=1,ms=7,label=r'$y(t)$')
		plt.step(
			self.t[0:np.int(self.N):8*self.R],
			self.Xemm[0:-1:8],
			where='post',
			ls=':',
			color='gray',
			marker='o',
			ms=5,
			lw=2,
			alpha=.7,
			mfc='none',
			label=r'$X_{\eta(t)}$'
		)
		plt.plot(
			self.t[0:np.int(self.N+1):self.R],
			self.Xemm,
			ls='-',
			c='red',
			lw=1,
			alpha=1.0,
			mfc='none',
			label=r'$\overline{X}(t)$'
		)
		plt.xlabel(r'$t$')
		plt.ylabel('sample paths')
		#plt.grid(True)
		plt.legend(shadow=True,loc=0)
		strFileName = 'ContinuousExtension.eps'
		plt.savefig(strFileName)
		plt.show()
		return
	def phi(self,h):
		phi_h=(np.exp(self.Lambda*h)-1)/self.Lambda
		return phi_h
    #Seting the problem
	def InitializeProblem(self,Lambda,mu,Xzero):
		self.Lambda=Lambda
		self.mu=mu
		self.Xzero=Xzero
#
	def InitializeMesh(self,k,p,r,T0,T):#Stensil of the mesh
		self.k=k
		self.p=p
		self.r=r
		self.T0=T0
		self.N=2**k
		self.P=2**p
		self.R=2**r
		self.T=T
		self.dt = self.T/np.float(self.N)
		self.IndexN=np.arange(self.N+1)#set of index to Ito integral
		self.tau=self.IndexN[0:self.N+1:self.P]
		self.t=np.linspace(0,self.T,self.N+1)
		self.Dt = self.R * self.dt;
		self.L = self.N / self.R;
	#%  Compute the Brownian increments, and the discretized Brownian path.
		self.DistNormal=np.random.randn(np.int(self.N))
		self.dW = np.sqrt(self.dt)*self.DistNormal
		self.W = np.cumsum(self.dW)
		self.W = np.concatenate(([0], self.W))
	#compute the Brownian path using phi(h)
		self.dWphi = np.sqrt(self.phi(self.dt))*self.DistNormal
		self.Wphi = np.cumsum(self.dWphi)
		self.Wphi = np.concatenate(([0], self.Wphi))#N+1 increments
	#Compute an approximation for the exact solution
	def StoInt(self,tk):#function to compute the stochastic integral
		xtemp=0.0
		for j in np.arange(self.P-1):
			f=np.exp(-self.Lambda*self.t[self.tau[tk]+j])
			Winc=self.W[self.tau[tk]+j+1]-self.W[self.tau[tk]+j]
			xtemp=xtemp+f*Winc
		return xtemp
	def Xtau(self,tk,Xtau_tk):#Compute the solution in [Xtau+1,Xtau]
		h=self.t[self.tau[tk+1]]-self.t[self.tau[tk]]
		Xtemp=self.mu*np.exp(Lambda*self.t[self.tau[tk+1]])*self.StoInt(tk)
		Xtau_tm=np.exp(self.Lambda*h)*Xtau_tk+Xtemp
		return Xtau_tm
	def ExactSolution(self):
		self.Xt=np.zeros(self.tau.shape[0])
		self.Xt[0]=self.Xzero
		print("\t\tExact solution X_t")
		for j in np.arange(self.tau.shape[0]-1):
			print('Xt[%d]: %2.7f '%(j,self.Xt[j]))
			self.Xtauj=self.Xtau(j,self.Xt[j])
			self.Xt[j+1]=self.Xtauj
	def EMM(self):
		#%  Preallocate Xem for efficiency.
		self.Xem = np.zeros(self.L+1)
		self.Xemm = np.zeros(self.L+1)
		self.DeltaW=np.zeros(self.L)
		self.DeltaWphi=np.zeros(self.L)
		self.Xem[0]=self.Xzero
		self.Xemm[0]=self.Xzero
		self.phiDt=self.phi(self.Dt)
		self.XtR=self.Xt[0::self.R]
		for j in np.arange(self.L):
			self.Winc = np.sum(self.dW[self.R*(j):self.R*(j+1)])
			self.WincPhi = np.sum(self.dWphi[self.R*(j):self.R*(j+1)]) 
			self.Xemm[j+1] = self.Xemm[j]*(1+self.Lambda*self.phiDt) + self.mu * self.WincPhi
			self.Xem[j+1] = self.Xem[j]*(1+self.Lambda*self.Dt) + self.mu * self.Winc
			self.DeltaW[j]=self.Winc
			self.DeltaWphi[j]=self.WincPhi
		self.emerr =np.abs(self.Xem[-1]-self.Xt[-1])
		self.emmerr =np.abs(self.Xemm[-1]-self.Xt[-1])
		#print '[%d] ||Xt-Xem||= %2.7f \t ||Xt-Xemm||= %2.7f \tXt[%d]=%2.7f'%(j,np.abs(XtR[j]-Xem[j]),np.abs(XtR[j]-Xemm[j]),j,XtR[j])
#
	def PrintResume(self):
		print '****************************************************************************'
		print '\t\t\tResumen de los metodos:'
		print '****************************************************************************'
		print '\tError:\tEuler-Mayurama \tEuler- Mayurama Mickens'
		print '\t\t %2.7f \t\t %2.7f'%(self.emerr,self.emmerr)        
		print '****************************************************************************'
		print '\t\t\tParametros de mayado'
		print '\t=================================================================='
		print '\t\t     dt \t    Dt \t \t Condicion'
		print '\t=================================================================='
		print '\t\t %2.7f \t %2.7f \t|1+lambda h|=%2.7f '%(self.dt,self.Dt,np.abs(1+self.Lambda*self.Dt) )  
	#
	def SaveData(self):
		'''
			Method to save the numerical solutions and parameters of Van der Pol ODE.
		'''
		#t=self.t[0:-1:self.R].reshape([self.t[0:-1:self.R].shape[0],1])
		t = self.t[0:np.int(self.N+1):self.R]
		tr = self.dt * self.tau
		Uem1 = self.Xem
		Ustk1 = self.Xemm
		Uex = self.Xt
		tagPar = np.array([
		'k=',
		'r=',
		'T0=',
		'N=',
		'R=',
		'T=',
		'dt=',
		'Dt=',
		'L=',
		'x0=',
		'lambda',
		'mu'
		])
		ParValues = np.array([
		self.k,
		self.r,
		self.T0,
		self.N,
		self.R,
		self.T,
		self.dt,
		self.Dt,
		self.L,
		self.Xzero,
		self.Lambda,
		self.mu
		])
		strPrefix = str(self.Dt)
		name1 = 'Parameters' + strPrefix + '.txt'
		name2 = 'Solution' + strPrefix + '.txt'
		name3 = 'refSolution'+str(self.dt)+'.txt'
		PARAMETERS = np.column_stack((tagPar, ParValues))
		np.savetxt(name1, PARAMETERS, delimiter=" ", fmt="%s")
		np.savetxt(name2,
			np.transpose(
				(
					t, Uem1
				)
			), fmt='%1.8f', delimiter='\t')
		strPrefix = str(self.Dt)
		np.savetxt(name3,
			np.transpose(
				(
					tr, Uex
				)
			), fmt='%1.8f', delimiter='\t')
#####Main
#problem Parameters
Lambda = -10.0
mu=2
Xzero = 1.0
#%  Set stepping parameters.
k=16
p=4
r=8
T = 1.0#ime in  [T0,T]
T0=0.0
SDE=SDEtest()
SDE.InitializeProblem(Lambda,mu,Xzero)
SDE.InitializeMesh(k,p,r,T0,T)
SDE.ExactSolution()
SDE.EMM()
SDE.graficaEM()
#SDE.PrintResume()
SDE.SaveData()

