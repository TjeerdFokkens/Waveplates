import numpy as np
from math import sqrt

H=np.matrix( [[1],[0]] )
V=np.matrix( [[0],[1]] )
D=np.matrix( [[0.5*sqrt(2)],[0.5*sqrt(2)]] )
A=np.matrix( [[0.5*sqrt(2)],[-0.5*sqrt(2)]] )
R=np.matrix( [[0.5*sqrt(2)],[1j*0.5*sqrt(2)]] )
L=np.matrix( [[0.5*sqrt(2)],[-1j*0.5*sqrt(2)]] )
SetList2=[-22.5,0,22.5,45]
SetList4=[-45,0,45]

def firstset(S):
	for T in SetList2:
		for U in SetList4:
			tr=Lambda2(T)*Lambda4(U)*StatetoMate(S)
			Proj=np.abs(np.dot(np.array(tr.T)[0],H))
			if np.abs(np.abs(Proj)-1.0)<0.0001:
				return [U,T]
			else: continue

def secondset(S,U,T):
	for V in SetList2:
		for W in SetList4:
			tr=Lambda2(V)*Lambda4(W)*Lambda2(T)*Lambda4(U)*StatetoMate(S)
			Proj=np.abs(np.dot(np.array(tr.T)[0],H))
			if np.abs(np.abs(Proj)-1.0)<0.0001:
				return [W,V]
			else: continue

def Lambda2(T):
	t=3.1415*(float(T)+90)/180.0
	return np.matrix( [[np.cos(2*t),np.sin(2*t)],[np.sin(2*t),-np.cos(2*t)]] )
def Lambda4(T):
	T=3.1415*(float(T)+90)/180.0
	return np.matrix( [[((1+1j)/sqrt(2))*(((np.cos(T))**2+1j*(np.sin(T))**2)),((1+1j)/sqrt(2))*((1-1j)*(np.sin(T))*(np.cos(T)))],[((1+1j)/sqrt(2))*((1-1j)*(np.sin(T))*(np.cos(T))),((1+1j)/sqrt(2))*((np.sin(T))**2+1j*(np.cos(T))**2)]] )

def func(S1,S2,A,B,C,D):
	S1=StatetoMate(S1)
	S2=StatetoMate(S2)
	Vec1=(Lambda2(B)*Lambda4(A)*S1)
	Vec2=(Lambda2(D)*Lambda4(C)*Lambda2(B)*Lambda4(A)*S2)
	L=[Vec1,Vec2]
	return L

def StatetoMate(S):
	H=np.matrix( [[1],[0]] )
	V=np.matrix( [[0],[1]] )
	D=np.matrix( [[0.5*sqrt(2)],[0.5*sqrt(2)]] )
	A=np.matrix( [[0.5*sqrt(2)],[-0.5*sqrt(2)]] )
	R=np.matrix( [[0.5*sqrt(2)],[1j*0.5*sqrt(2)]] )
	L=np.matrix( [[0.5*sqrt(2)],[-1j*0.5*sqrt(2)]] )
	if S=='H': S=H
	elif S=='V': S=V
	elif S=='D': S=D
	elif S=='A': S=A
	elif S=='R': S=R
	elif S=='L': S=L
	return S

while True:
	Inp=input("State to be measured:")
	s1 = Inp[0]
	s2 = Inp[1]
	ang1=firstset(s1)[0]
	ang2=firstset(s1)[1]
	ang3=secondset(s2,ang1,ang2)[0]
	ang4=secondset(s2,ang1,ang2)[1]

	print("The first Lambda4-plate must be set to:", ang1,"degrees.")
	print("The first Lambda2-plate must be set to:", ang2,"degrees.")
	print("The second Lambda4-plate must be set to:", ang3,"degrees.")
	print("The second Lambda2-plate must be set to:", ang4,"degrees.")
