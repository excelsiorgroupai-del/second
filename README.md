# Streamlit 記帳工具

這是一個給初學者使用的網頁版記帳工具，功能包含：

- 新增記帳資料（金額、分類、備註、日期）
- 用表格查看所有記錄
- 依分類統計總金額
- 資料儲存在 `records.json`

## 啟動方式

1. 安裝套件：

```bash
pip install -r requirements.txt
```

2. 啟動網頁：

```bash
streamlit run app.py
```

3. 開啟瀏覽器後，就可以直接在網頁上操作記帳工具。

## 檔案說明

- `app.py`：主程式（Streamlit 網頁）
- `requirements.txt`：需要安裝的套件
- `records.json`：執行後自動建立，用來儲存記帳資料
