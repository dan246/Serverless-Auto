# Serverless-Auto
nuclio 自動化控制工具

[english version](https://github.com/dan246/Serverless-Auto/blob/main/README_en.md)

[中文版本](https://github.com/dan246/Serverless-Auto/edit/main/README.md)
# Nuclio 函數管理工具

這個專案提供了一組 Python 腳本，用於管理和部署 [Nuclio](https://nuclio.io/) Serverless 函數。可以透過這些腳本快速獲取 Nuclio 項目和函數的列表，並部署新的函數。

## 功能

- 獲取 Nuclio 函數和項目的列表。
- 部署新的 Serverless 函數。
- 獲取特定函數的詳細信息。

## 如何使用

1. 確保環境中已安裝 Python 和 `requests` 庫。
2. 配置 `nuclio_dashboard_url` 變數，指向 Nuclio 儀表板。
3. 運行腳本，根據需要調用不同的函數。

## 安裝需求

請確保系統中安裝了以下項目：

- Python 3.6+
- `requests` 庫

可以透過以下命令安裝 `requests`：

```bash
pip install requests
```

## 未來的優化計劃

- 增加錯誤處理機制，使腳本在遇到 API 調用問題時更加健壯。
- 提供更豐富的參數配置選項，使腳本更靈活。
- 增強用戶介面，提供命令行工具或圖形界面供用戶選擇。
- 實施安全性增強，例如支持 HTTPS 連接和 API 密鑰管理。

## 聯絡方式

若有任何問題或建議，請通過 GitHub Issues 與我聯繫。

## 參考資料

[Nuclio Github](https://github.com/nuclio/nuclio)
