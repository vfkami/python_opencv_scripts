from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import cv2

def centroid_histrogram(clt):
    # number of clusters
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    # histrogram of the number of pixels
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histrogram, such that it sums to one'
    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_color(hist, centroids):
    # init the rectable size
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each color cluster and the color of eahc cluster
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    return bar

def valid_imshow_data(data):
    data = np.asarray(data)
    if data.ndim == 2:
        return True
    elif data.ndim == 3:
        if 3 <= data.shape[2] <= 4:
            return True
        else:
            print('The "data" has 3 dimensions but the last dimension '
                  'must have a length of 3 (RGB) or 4 (RGBA), not "{}".'
                  ''.format(data.shape[2]))
            return False
    else:
        print('To visualize an image the data must be 2 dimensional or '
              '3 dimensional, not "{}".'
              ''.format(data.ndim))
        return False

image = cv2.imread("luffy.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

clusters = 10
# cluster the color in the image
clt = KMeans(n_clusters=clusters)
clt.fit(image)

hist = centroid_histrogram(clt)
bar = plot_color(hist, clt.cluster_centers_)

# display
plt.figure()
plt.axis("off")
valid_imshow_data(bar)
plt.imshow(bar)
plt.show()
