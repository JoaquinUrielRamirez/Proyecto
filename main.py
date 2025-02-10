import matplotlib.pyplot as plt
from revenue import revenues
from price_sim import price_simulation
from price_pdf import price_pdf_

lam = 50
k = 10
n = 10000
p0 = 51
i = 0.4


prices = price_simulation(lam, k, n)

plt.figure()
plt.xlabel('Precio')
plt.ylabel('Volumen')
plt.hist(prices)
plt.title('Distribución Weibull del Precio')
plt.show()

pdfs = []
for price in prices:
    pdfs_ = price_pdf_(price, k, lam)
    pdfs.append(pdfs_)

