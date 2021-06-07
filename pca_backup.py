# importing dataset
from sklearn.datasets import .... as fetch_olivetti_faces

faces = fetch_olivetti_faces()

img = faces.images
M = 400
N = 4096

img2 = np.array([[0 for i in range(N)] for j in range(M)])

# visage moyen = vm
vm = [0 for i in range(N)]

for a in img:
    img2 = a.flatten()
    vm = vm + img2
vm1 = vm / 400
vm2 = vm1.reshape(64, 64)
plt.imshow(vm2, amap='gray')
