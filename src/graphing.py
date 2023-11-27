import matplotlib.pyplot as plt
import training
import numpy as np

x = np.linspace(1,training.num_epochs,training.num_epochs)
plt.plot(x,training.train_hist,scalex=True, label="Training loss")
plt.plot(x,training.test_hist, label="Test loss")
plt.legend()
plt.show()

#########
