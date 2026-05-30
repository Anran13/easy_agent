## 注意重點

1. API key 建立後還需要綁定信用卡才能使用
2. 要執行agent時，需要將路徑回到根目錄`cd ..`
3. `adk web` 執行agent

## wsl
```
# 檢查您電腦裡有哪些 Linux 系統
wsl -l -v

# 指定進入正確的 Linux 環境
wsl -d Ubuntu

# 退出Ubuntu環境
exit

# 把 Ubuntu 設回預設值
wsl --set-default Ubuntu
```

## docker
```
在 Docker Desktop 開啟 WSL 2
1. 打開 Windows 桌面上的 Docker Desktop 軟體。
2. 點擊右上角的 齒輪圖標 (Settings) 進入設定。
3. 在左側選單中點選 General，確認 "Use the WSL 2 based engine" 已經被勾選。
4. 接著點選左側選單的 Resources -> WSL integration。
5. 在畫面中會看到 "Enable integration with my default WSL distro"，請將它勾選（Turn on）。
6. 如果下方有出現您剛才建立的 Ubuntu 獨立開關，也請一併將它打開（藍色狀態）。
7. 點擊右下角的 Apply & restart 儲存並重啟 Docker。
In wsl
docker run [映像檔名稱]：從無到有，下載範本並建立一個新容器。（就像拿光碟裝新遊戲）。
docker start [容器名稱]：喚醒一個已經存在但關閉中的容器。（就像讀取舊的遊戲存檔）。
```

在 WSL 或一般的 Linux 環境中，最常使用的 Ubuntu 指令可以依照功能分類為以下幾大類。

為了方便您未來在開發（特別是配合 Docker、Python 開發）時快速查閱，我將最實用的指令整理如下：

---

# Linux

## 一、 檔案與目錄操作（最基礎）

* **`ls`**：列出當前目錄下的檔案與資料夾。
* `ls -l`：顯示詳細資料（權限、大小、修改時間）。
* `ls -a`：顯示所有檔案（包含開頭為 `.` 的隱藏檔，如 `.bashrc`、`.dockerignore`）。


* **`cd`**：切換目錄。
* `cd ..`：回到上一層目錄。
* `cd ~`：回到目前使用者的家目錄（Home）。


* **`pwd`**：顯示目前所在的完整路徑（Print Working Directory）。
* **`mkdir [資料夾名]`**：建立新的資料夾。
* **`rm [檔名]`**：刪除檔案。
* `rm -rf [資料夾名]`：**強制**刪除整個資料夾及其內所有內容（使用時請務必小心！）。


* **`cp [來源] [目的地]`**：複製檔案。
* `cp -r [來源資料夾] [目的地]`：複製整個資料夾。


* **`mv [來源] [目的地]`**：移動檔案，或是用來**重新命名**。

---

## 二、 檔案內容查看與編輯

* **`cat [檔名]`**：在終端機畫面上一次印出檔案的全部內容。
* **`less [檔名]`**：分頁查看大檔案的內容（按 `Q` 鍵可以退出）。
* **`tail -f [檔名]`**：**即時追蹤**並印出檔案最新寫入的內容（常用來看日誌/Log 檔）。
* **`nano [檔名]`**：Ubuntu 內建最簡單好用的文字編輯器（適合快速改一下 Dockerfile 或設定檔）。
* **`vim [檔名]`**：進階文字編輯器（功能強大，但需要學習成本）。

---

## 三、 系統權限與套件管理（需要管理員權限）

在 Ubuntu 中，安裝軟體或修改系統檔需要管理員（Root）權限，必須在指令前加上 `sudo`。

* **`sudo apt update`**：更新軟體源清單（檢查有哪些軟體可以升級）。
* **`sudo apt upgrade`**：正式將系統內所有舊版軟體升級到最新版。
* **`sudo apt install [套件名稱]`**：安裝新軟體（例如：`sudo apt install git`）。
* **`sudo apt remove [套件名稱]`**：解除安裝軟體。

---

## 四、 系統狀態與進程（Process）查詢

* **`df -h`**：檢查硬碟磁碟空間剩餘容量（以人類易讀的 GB/MB 顯示）。
* **`free -h`**：檢查目前記憶體（RAM）的使用狀況。
* **`top`** 或 **`htop`**：即時查看系統的 CPU、記憶體消耗狀況與正在執行的進程（類似 Linux 版工作管理員，`htop` 畫面較漂亮，需先 `sudo apt install htop`）。
* **`ps aux`**：列出目前系統上所有正在執行的進程。
* 常用組合：`ps aux | grep python`（找出所有跟 Python 相關的進程）。


* **`kill -9 [PID]`**：強制關閉某個指定的進程（PID 可以透過 `ps` 或 `top` 查到）。

---

## 五、 網路相關指令

* **`ping [網址或IP]`**：測試網路是否能連通該伺服器。
* **`curl [網址]`**：在終端機發送網路請求（常用來測試 API 或下載檔案，例如 `curl -O https://example.com/file.tar.gz`）。
* **`ifconfig`** 或 **`ip a`**：查詢目前 Linux 環境的網卡、IP 位址等網路設定。

---

### 💡 終端機操作小技巧

1. **Tab 鍵（自動補齊）**：輸入檔名、資料夾名或指令時，按一下 `Tab` 會自動幫你補齊，按兩下會列出所有符合的選項。
2. **方向鍵（上/下）**：可以快速調出之前輸入過的歷史指令。
3. **`clear`**（或快捷鍵 `Ctrl + L`）：清空當前終端機螢幕，讓畫面恢復乾淨。
4. **`history`**：列出你這台電腦過去輸入過的所有指令紀錄。