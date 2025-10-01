import streamlit as st
import random

def generate_number(length):
    digits = list(range(0, 10))
    random.shuffle(digits)
    return digits[:length]  # 원하는 자리수 숫자 생성

# 난이도 선택
st.title("⚾ 숫자야구 게임")
level = st.radio("난이도를 선택하세요:", ["3자리", "4자리", "5자리"])

level_map = {"3자리": 3, "4자리": 4, "5자리": 5}
length = level_map[level]

# 세션 상태 관리
if "answer" not in st.session_state or "current_length" not in st.session_state or st.session_state.current_length != length:
    st.session_state.answer = generate_number(length)
    st.session_state.history = []
    st.session_state.game_over = False
    st.session_state.current_length = length

st.write(f"중복 없는 {length}자리 숫자를 맞혀보세요!")

# 입력 받기
guess = st.text_input(f"숫자 입력 (예: {'123' if length==3 else '1234' if length==4 else '12345'})", max_chars=length)

if st.button("확인") and not st.session_state.game_over:
    if len(guess) != length or not guess.isdigit():
        st.warning(f"{length}자리 숫자를 입력해주세요!")
    else:
        guess_digits = [int(d) for d in guess]
        answer = st.session_state.answer

        strike = sum([guess_digits[i] == answer[i] for i in range(length)])
        ball = sum([(d in answer) for d in guess_digits]) - strike

        if strike == length:
            st.success(f"🎉 정답! {guess} 맞혔습니다!")
            st.session_state.history.append((guess, f"{strike}S {ball}B"))
            st.session_state.game_over = True
        else:
            st.session_state.history.append((guess, f"{strike}S {ball}B"))

# 기록 출력
if st.session_state.history:
    st.subheader("📜 시도 기록")
    for g, result in st.session_state.history:
        st.write(f"{g} → {result}")

# 새 게임 시작
if st.button("새 게임 시작"):
    st.session_state.answer = generate_number(length)
    st.session_state.history = []
    st.session_state.game_over = False
    st.info(f"새로운 {length}자리 숫자가 생성되었습니다. 도전해보세요!")
