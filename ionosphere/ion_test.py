from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

from dionpy import IonFrame

# Date of observation (UTC)
dt = datetime(year=2022, month=10, day=6, hour=15, minute=0)

# Instrument position: latitude [deg], longitude [deg], altitude [m]
pos = (37.871, 122.273, 0)

# Define a model
model = IonFrame(dt, pos)

# Define frequency of observation in [MHz]
freq = 40

# Plot ionospheric attenuation
model.plot_atten(freq, title=r"Attenuation factor $f_a$")
plt.show()

# Plot ionospheric refraction
model.plot_refr(freq, title=r"Refraction angle $\delta \theta$")
plt.show()

