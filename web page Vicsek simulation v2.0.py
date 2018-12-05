
import cmath
import numpy as np
import matplotlib.pyplot as plt
import random
def vicsek(N, L, deltaT, Velocity, nsim, r, noise):
    x = np.random.uniform(0, L, N)
    y = np.random.uniform(0, L, N)   
    direction = np.random.uniform(-np.pi, np.pi, N)   
    CmassVelocity = []                      
    p = 0
    while p < nsim:
        n=0
        updatedx = []
        updatedy = []
        xvelocity = []
        yvelocity = []          
        while n < N:
            xv = Velocity *np.cos(direction[n])            
            deltaX = deltaT * Velocity *np.cos(direction[n])
            xvelocity = np.append(xvelocity, xv)
            newX = x[n] + deltaX
            if newX >= L:
                newX=newX - L
            if newX < 0:
                newX=newX + L
            yv = Velocity *np.sin(direction[n]) 
            deltaY = deltaT * Velocity *np.sin(direction[n]) 
            yvelocity = np.append(yvelocity, yv)
            newY = y[n] + deltaY
            if newY >= L:
                newY = newY - L
            if newY < 0:
                newY = newY + L
            updatedx = np.append(updatedx, newX)
            updatedy = np.append(updatedy, newY)
            n = n + 1
        updateddirection = []
        q = 0
        while q < N:
            s = 0  
            imaginary=0
            real=0                      
            AverageDirection=0
            while s < N:
                distance = np.sqrt((x[s]-x[q])**2 + (y[s]-y[q])**2)                                                                  
                if distance <= r:
                    real = real + np.cos(direction[s])                                                   
                    imaginary = imaginary + np.sin(direction[s])                                  
                s = s + 1           
            AverageDirection = cmath.phase(complex(real, imaginary)) + ((random.randint(-50, 50)/100)*noise)
            updateddirection = np.append(updateddirection, AverageDirection)           
            q=q+1
        direction=updateddirection        
        x = updatedx
        y = updatedy        
        sumYvelocity = np.sum(xvelocity)
        sumXvelocity = np.sum(yvelocity)
        modvelocity = np.sqrt((sumYvelocity**2) + (sumXvelocity**2))
        cmassvelocity = abs(modvelocity/(N*Velocity))
        CmassVelocity = np.append(CmassVelocity, cmassvelocity)                
        p = p + 1                                
    Xvelocity = []
    Yvelocity = []    
    z = 0
    while z < N:
        X = Velocity*np.cos(direction[z])
        Y = Velocity*np.sin(direction[z])
        Xvelocity = np.append(Xvelocity, X)
        Yvelocity = np.append(Yvelocity, Y)
        z = z + 1 
    plt.figure()
    plt.quiver(x, y, Xvelocity, Yvelocity)
    plt.show
    
    plt.figure()
    plt.plot(np.linspace(0, nsim*deltaT, nsim),CmassVelocity)
    plt.xlabel('Time (s)')     
    plt.ylabel('Order') 
    plt.ylim(0,1)    
