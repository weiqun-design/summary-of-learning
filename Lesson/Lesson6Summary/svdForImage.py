from PIL import Image
from scipy.linalg import svd
import matplotlib.pyplot as plt
import numpy as np




def get_image_feature(s, k):
    s_temp = np.zeros(s.shape[0])
    s_temp[0:k] = s[0:k]
    s = s_temp * np.identity(s.shape[0])
    temp = np.dot(p,s)
    temp = np.dot(temp,q)
    plt .imshow(temp, cmap=plt.cm.get_cmap('gray'), interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    image1 = Image.open('./256.bmp')
    A = np.array(image1)
    plt.imshow(A, cmap=plt.cm.get_cmap('gray'), interpolation='nearest')
    plt.show()
    p,s,q = svd(A, full_matrices=False)
    print(s.shape)
    get_image_feature(s, 5)
    get_image_feature(s, 50)
    get_image_feature(s, 500)
