import streamlit as st
import numpy as np

# === AI 가중치 세팅 ===
freq_data = {
    1:38, 2:37, 3:51, 4:39, 5:28, 6:50, 7:48, 8:33, 9:39, 10:35,
    11:40, 12:49, 13:49, 14:45, 15:42, 16:47, 17:42, 18:48, 19:43, 20:40,
    21:49, 22:47, 23:40, 24:43, 25:35, 26:42, 27:42, 28:41, 29:41, 30:45,
    31:41, 32:43, 33:46, 34:47, 35:50, 36:42, 37:47, 38:52, 39:45, 40:40,
    41:38, 42:43, 43:38, 44:45, 45:47
}

numbers = list(freq_data.keys())
weights = list(freq_data.values())
total_weight = sum(weights)
probabilities = [w / total_weight for w in weights]

def ai_lotto_pick():
    return sorted(np.random.choice(numbers, size=6, replace=False, p=probabilities))

def get_color(number):
    if number <= 10:
        return '#FFD700'
    elif number <= 20:
        return '#1E90FF'
    elif number <= 30:
        return '#FF4500'
    elif number <= 40:
        return '#32CD32'
    else:
        return '#228B22'

# 세션 상태 초기화
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

st.title("🎯 AI 로또 추천기")

col1, col2 = st.columns(2)

# 추천번호 추가 버튼
if col1.button("로또번호 추가생성"):
    if len(st.session_state.recommendations) < 10:
        st.session_state.recommendations.append(ai_lotto_pick())
    else:
        st.warning("최대 10세트까지만 생성 가능합니다!")

# 초기화 버튼
if col2.button("초기화"):
    st.session_state.recommendations = []

# 추천번호 출력
for i, pick in enumerate(st.session_state.recommendations):
    st.write(f"**추천 {i+1}번 세트:**")
    html = "<div style='display:flex; gap:10px; justify-content:center;'>"
    for num in pick:
        color = get_color(num)
        html += f"""
            <div style='background-color:{color}; color:white; font-size:30px;
            border-radius:50%; width:60px; height:60px; display:flex;
            align-items:center; justify-content:center;'>{num}</div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
