import streamlit as st
import pandas as pd
from datetime import datetime

def simulate_job_application(input_iq):
    original_iq = 85
    hiring_threshold = 91
    undetectable_range = 15

    if input_iq < hiring_threshold:
        return "Вас не взяли на работу.", 0
    elif input_iq > original_iq + undetectable_range:
        cost = 3 * (input_iq - original_iq)
        return f"Вы были уволены. Вы потратили {cost} рублей.", -cost
    else:
        earnings = 100 - 3 * (input_iq - original_iq)
        return f"Вас взяли на работу. Ваш доход составил {earnings} рублей.", earnings

def save_result_to_csv(name, input_iq, result, earnings, language):
    # Создание или добавление данных в CSV-файл
    df = pd.DataFrame([[name, input_iq, result, earnings, language, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                      columns=["Имя / Name", "IQ", "Результат / Result", "Доход / Earnings", "Язык / Language", "Время / Time"])
    df.to_csv("results.csv", mode='a', index=False, header=not pd.io.common.file_exists("results.csv"))

# Заголовок приложения
st.title("Симуляция приема на работу / Job Application Simulation")

# Выбор языка
language = st.selectbox("Выберите язык / Choose Language", ["Русский", "English"])

# Поле для ввода имени
name = st.text_input("Введите ваше имя / Enter your name")

# Использование сессии для хранения попытки
if "attempt_made" not in st.session_state:
    st.session_state.attempt_made = False

# Кнопка для сброса попытки
if st.button("Сбросить попытку / Reset Attempt"):
    st.session_state.attempt_made = False

# Если попытка еще не была сделана и имя введено
if not st.session_state.attempt_made and name:
    # Ввод уровня IQ
    input_iq = st.number_input("Введите уровень IQ / Enter your IQ:", min_value=50, max_value=150, step=1)

    # Кнопка для проверки результата
    if st.button("Проверить результат / Check Result"):
        # Вычисление результата
        if language == "Русский":
            result, earnings = simulate_job_application(input_iq)
        else:
            result, earnings = simulate_job_application(input_iq)

        # Отображение результата
        st.write(result)

        # Сохранение результата в CSV
        save_result_to_csv(name, input_iq, result, earnings, language)

        # Устанавливаем флаг, чтобы запретить повторный ввод
        st.session_state.attempt_made = True
else:
    st.write("Вы уже использовали свою попытку / You have already used your attempt.")
