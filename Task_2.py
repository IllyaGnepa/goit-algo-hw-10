import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(f, a, b, n_points=10000):
    x_random = np.random.uniform(a, b, n_points)
    y_random = np.random.uniform(0, f(b), n_points)
    under_curve = y_random < f(x_random)
    integral = (b - a) * f(b) * np.mean(under_curve)
    return integral

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)
print("Інтеграл методом Монте-Карло: ", monte_carlo_result)

# Аналітичне обчислення інтеграла за допомогою функції quad
quad_result, error = spi.quad(f, a, b)
print("Інтеграл методом quad: ", quad_result, " з похибкою: ", error)

# Графік функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Висновок
print(f"Різниця між методами: {abs(monte_carlo_result - quad_result)}")