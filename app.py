import streamlit as st
import pandas as pd
import datetime
import os

st.title("📷 WORK TALK - 위험성평가 입력")
st.markdown("사진 1장 업로드 ➝ 질문 4개 응답 ➝ 저장 ➝ 다음 사진 순서대로 진행해 주세요.")

with st.form("entry_form", clear_on_submit=True):
    name = st.text_input("이름")
    department = st.text_input("부서")
    uploaded_file = st.file_uploader("작업 사진 업로드", type=["jpg", "jpeg", "png"])
    q1 = st.text_input("1. 어떤 작업을 하고 있는 건가요?")
    q2 = st.text_input("2. 이 작업은 왜 위험하다고 생각하나요?")
    q3 = st.radio("3. 이 작업은 얼마나 자주 하나요?", ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"])
    q4 = st.radio("4. 이 작업은 얼마나 위험하다고 생각하나요?", [
        "약간의 위험: 일회용 밴드 치료 필요 가능성 있음",
        "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식",
        "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음",
        "매우 위험: 불가역적 장애 또는 사망 가능성 있음"
    ])
    submitted = st.form_submit_button("저장하기")

if submitted:
    if uploaded_file and name and department and q1 and q2:
        date = datetime.datetime.now().strftime("%Y%m%d")
        filename = f"응답결과_{department}_{name}_{date}.xlsx"
        save_path = os.path.join("/mnt/data", filename)

        df = pd.DataFrame([{
            "이름": name,
            "부서": department,
            "작업내용": q1,
            "위험요인": q2,
            "작업빈도": q3,
            "위험수준": q4
        }])
        df.to_excel(save_path, index=False)
        st.success("저장 완료! 다음 사진을 입력해 주세요.")
    else:
        st.warning("모든 항목을 입력해 주세요.")
