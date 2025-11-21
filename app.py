import streamlit as st
import random

# 세션 상태 초기화
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

if "tries" not in st.session_state:
    st.session_state.tries = 0

if "history" not in st.session_state:
    st.session_state.history = []   # 이전 기록 저장


st.title("🎮 UP & DOWN 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 입력 UI
user_input = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)

# 제출 버튼
if st.button("제출"):
    st.session_state.tries += 1

    # 메시지 생성
    if user_input < st.session_state.number:
        msg = f"{user_input} → 🔼 UP"
    elif user_input > st.session_state.number:
        msg = f"{user_input} → 🔽 DOWN"
    else:
        msg = f"🎉 정답 {user_input}! (시도 {st.session_state.tries}회)"

    # 기록 저장
    st.session_state.history.append(msg)

    # 정답일 경우
    if user_input == st.session_state.number:
        st.success(msg)
        st.balloons()
        if st.button("다시 시작"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.tries = 0
            st.session_state.history = []
    else:
        st.warning(msg)

# 히스토리 출력
st.write("### 📜 시도 기록")
for h in st.session_state.history:
    st.write("- ", h)


