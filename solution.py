import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu

chat_id = 531503618 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    U1, p = mannwhitneyu(males, females, method="exact")
    alpha = 0.03
    return (alpha>p)
