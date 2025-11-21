import streamlit as st
import random

# 세션 상태 초기화
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "tries" not in st.session_state:
    st.session_state.tries = 0

st.title("🎮 UP & DOWN 게임")

st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 숫자 입력
user_input = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)

if st.button("제출"):
    st.session_state.tries += 1

    if user_input < st.session_state.number:
        st.warning("🔼 UP! 더 큰 숫자입니다.")
    elif user_input > st.session_state.number:
        st.warning("🔽 DOWN! 더 작은 숫자입니다.")
    else:
        st.success(f"🎉 정답입니다! 시도 횟수: {st.session_state.tries}")
        st.balloons()
        # 게임 리셋 버튼 표시
        if st.button("다시 시작"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.tries = 0

