import streamlit as st

# Заголовок приложения
st.title("Простое приложение на Streamlit")

# Ввод чисел пользователем
number1 = st.number_input("Введите первое число", value=0)
number2 = st.number_input("Введите второе число", value=0)

# Вычисление суммы
result = number1 + number2

# Отображение результата
st.write(f"Сумма: {result}")
