import matplotlib.pyplot as plt
from revenue import revenues
from price_sim import price_simulation
from price_pdf import price_pdf_
from optimiza import optimo
from b_a import bid_ask

lam = 50
k = 10
n = 100
p0 = 51
i = 0.4

optimo = optimo(revenues)

print(optimo)

prices = price_simulation(lam, k, n)

plt.figure()
plt.xlabel('Precio')
plt.ylabel('Volumen')
plt.hist(prices)
plt.title('Distribución Weibull del Precio')
plt.show()