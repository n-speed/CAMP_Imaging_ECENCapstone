import matplotlib.pyplot as plt
import numpy as np

def graphLoss(epochs,train_hist,test_hist):
    x = np.linspace(1,epochs,epochs)
    plt.plot(x,train_hist,scalex=True, label="Training loss")
    plt.plot(x,test_hist, label="Test loss")
    plt.legend()
    plt.show()
    return 0