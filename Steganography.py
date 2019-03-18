import cv2
import numpy as np

imgpath = "" #path of image 1
img1 = cv2.imread(imgpath)
imgpath1 = "" #path of image 2
img2 = cv2.imread(imgpath1)

#Check if the two images are of same size.
if img2.shape != img1.shape:    
        raise ValueError('Image 1 and Image 2 should be of same size!')

m,n,o = img1.shape
B1 = img1[:,:,0] #Array of Blue of image 1
G1 = img1[:,:,1] #Array of Green of image 1
R1 = img1[:,:,2] #Array of Red of image 1

B2 = img2[:,:,0] #Array of Blue of image 2
G2 = img2[:,:,1] #Array of Green of image 2
R2 = img2[:,:,2] #Array of Red of image 2

#creating arrays for storing the pixel values of the new merged image.
B3 = np.zeros((m,n),dtype=np.uint8) #Blue
G3 = np.zeros((m,n),dtype=np.uint8) #Green
R3 = np.zeros((m,n),dtype=np.uint8) #Red

##Merging both the images
#Merge Function that merges the 2 images.
for i in range(0,m): #iterating through rows
    for j in range(0,n): #iterating through columns
        #converting the integer values of image 1 into binary format(i.e, 8-bits)
        Bb1 = '{0:08b}'.format(B1[i,j]) 
        Gb1 = '{0:08b}'.format(G1[i,j])
        Rb1 = '{0:08b}'.format(R1[i,j])
        #converting the integer values of image 2 into binary format(i.e, 8-bits)
        Bb2 = '{0:08b}'.format(B2[i,j])
        Gb2 = '{0:08b}'.format(G2[i,j])
        Rb2 = '{0:08b}'.format(R2[i,j])
        #Taking the 1st 4-bits of image 1 and appending the last 4-bits of image 2.
        a = Bb1[:4] + Bb2[:4]
        b = Gb1[:4] + Gb2[:4]
        c = Rb1[:4] + Rb2[:4]
        #converting the new binary values to integer values.
        B3[i,j] = int(a,2)
        G3[i,j] = int(b,2)
        R3[i,j] = int(c,2)
#Array for storing the new image. 
img3 = np.zeros((m,n,o),dtype=np.uint8)
#Assigning those new values to the new image.
img3[:,:,0] = B3
img3[:,:,1] = G3
img3[:,:,2] = R3

##Unmerging both the images
img4 = np.zeros((m,n,o),dtype=np.uint8)
B4 = np.zeros((m,n),dtype=np.uint8) #Blue
G4 = np.zeros((m,n),dtype=np.uint8) #Green
R4 = np.zeros((m,n),dtype=np.uint8) #Red
for i in range(0,m): #iterating through rows
    for j in range(0,n): #iterating through columns
        Bb = '{0:08b}'.format(B3[i,j])
        Gb = '{0:08b}'.format(G3[i,j])
        Rb = '{0:08b}'.format(R3[i,j])
        x = Bb[4:] + '1111'
        y = Gb[4:] + '1111'
        z = Rb[4:] + '1111'
        B4[i,j] = int(x,2)
        G4[i,j] = int(y,2)
        R4[i,j] = int(z,2)
img4[:,:,0] = B4
img4[:,:,1] = G4
img4[:,:,2] = R4
        
#Image 1
cv2.imshow('img 1',img1)
#Image 2
cv2.imshow('img 2',img2)
#Image 3
cv2.imshow('img 3(Merged Image)',img3)
#Image 4
cv2.imshow('img 4(Hidden Information)',img4)
