import matplotlib.pyplot as plt
from revenue import revenues
from revenue import weibull
from price_sim import p_inf_s
from optimiza import optimizar
import numpy as np
from revenue import weibull_pdf

lam = 50
k = 10
n = 1000
p0 = 51
i = 0.4
a = p0 + p0*1.1
b = p0 - p0*0.9

s = np.linspace(0,100, n)

sol = optimizar(a,b)
a,b = sol.x

print(sol)
print(a, b)


prices = weibull(s, lam, k)

plt.figure()
plt.xlabel('Price')
plt.ylabel('Expected Revenue')
plt.plot(s, prices)
plt.title('Weibull Price Distribution')
plt.show()

s = np.linspace(0,6,n)
u_l = s
u_i = -s

ex_value_liquid = u_l * (1 - i)
ex_value_informed = s * (1 - i) * p_inf_s(s)

plt.figure(figsize=(7, 5))
plt.plot(s, u_l, label="Liquid", color="green")
plt.plot(s, ex_value_liquid, label="Liquid - Informed", color="orange")
plt.plot(s, ex_value_informed, label="Informed",  color="red")
plt.xlabel('SPREAD')
plt.ylabel('REVENUE')
plt.grid(True)
plt.title('Bid-Ask SPREAD')
plt.legend()
plt.show()

# Resultados
if sol.success:
    a, b = sol.x
    ingresos_maximos = -sol.fun
    print("Optimización exitosa:")
    print(f"Precio de compra óptimo (a): {a}")
    print(f"Precio de venta óptimo (b): {b}")
    print(f"Ingresos máximos esperados: {ingresos_maximos}")

    # Graficar la Optimización
    p_range = np.linspace(0, 100, 500)
    plt.plot(p_range, weibull_pdf(p_range, k, lam))
    plt.xlabel("Price")
    plt.ylabel("Volume")
    plt.title("Optimal Price")
    plt.axvline(a, color='r', linestyle='--', label=f"Ask: {a:.2f}")
    plt.axvline(b, color='g', linestyle='--', label=f"Bid: {b:.2f}")
    plt.legend()
    plt.show()

else:
    print("Error en la optimización:")
    print(sol.message)