import json
from pathlib import Path
from datetime import date

import pandas as pd
import streamlit as st

DATA_FILE = Path("records.json")


def load_records() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_records(records: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


st.set_page_config(page_title="記帳工具", page_icon="💰")
st.title("💰 Streamlit 記帳工具")
st.write("在這裡新增你的支出或收入，資料會存在 records.json。")

if "records" not in st.session_state:
    st.session_state.records = load_records()

with st.form("add_record_form"):
    amount = st.number_input("金額", min_value=0.0, step=1.0, format="%.2f")
    category = st.text_input("分類", placeholder="例如：餐飲、交通、薪水")
    note = st.text_input("備註", placeholder="可不填")
    record_date = st.date_input("日期", value=date.today())

    submitted = st.form_submit_button("新增記錄")

if submitted:
    if not category.strip():
        st.warning("請先輸入分類。")
    else:
        new_record = {
            "金額": float(amount),
            "分類": category.strip(),
            "備註": note.strip(),
            "日期": record_date.isoformat(),
        }
        st.session_state.records.append(new_record)
        save_records(st.session_state.records)
        st.success("新增成功！")

st.subheader("所有記帳資料")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    st.dataframe(df, use_container_width=True)
else:
    st.info("目前沒有資料，先新增第一筆記錄吧！")

st.subheader("分類統計")
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    summary = (
        df.groupby("分類", as_index=False)["金額"]
        .sum()
        .sort_values("金額", ascending=False)
    )
    st.dataframe(summary, use_container_width=True)
    st.bar_chart(summary.set_index("分類"))
else:
    st.info("目前沒有可統計的資料。")
