import streamlit as st

def simulate_job_application(input_iq):
    original_iq = 85
    hiring_threshold = 91
    undetectable_range = 15

    if input_iq < hiring_threshold:
        return "Вас не взяли на работу."
    elif input_iq > original_iq + undetectable_range:
        cost = 3 * (input_iq - original_iq)
        return f"Вы были уволены. Вы потратили {cost} рублей."
    else:
        earnings = 100 - 3 * (input_iq - original_iq)
        return f"Вас взяли на работу. Ваш доход составил {earnings} рублей."

# Заголовок приложения
st.title("Симуляция приема на работу")
st.header("Ваше IQ: 85")

# Использование сессии для хранения попытки
if "attempt_made" not in st.session_state:
    st.session_state.attempt_made = False

# Если попытка еще не была сделана
if not st.session_state.attempt_made:
    # Ввод уровня IQ
    input_iq = st.number_input("Введите уровень IQ, который вы укажете на собеседовании:", min_value=50, max_value=150, step=1)

    # Кнопка для проверки результата
    if st.button("Проверить результат"):
        # Вычисление результата
        result = simulate_job_application(input_iq)
        # Отображение результата
        st.write(result)
        # Устанавливаем флаг, чтобы запретить повторный ввод
        st.session_state.attempt_made = True
else:
    st.write("Вы уже использовали свою попытку.")
