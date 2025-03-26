## 複製基底
3. Clone 這個 Angular 模板
```javascript=1
// ssh
git clone git@github.com:jack755051/base_template.git
 // https
https://github.com/jack755051/base_template.git
```
2. 進入新專案資料夾
```javascript
cd my-new-project
```
3. 刪除 .git 目錄
```javascript
rm -rf .git
```
4. 重新初始化 Git
````javascript
git init
````
3-1. 或執行`yarn clean-git`

--------
## 設定調整簡介
### angular.json
- prefix：
  - 組件生成前綴
- assets： 
  - 負責靜態資源會將指定檔案夾複製到`/dist`。
  - 不會自動載入(需要手動`src="/public/xxx"`)到應用程式。
  - 簡化圖片調用路徑。
  - 與`src/assets`不同，`src/assets`是開發時的靜態檔案夾。
  - 需將開發時的靜態圖像資料夾加入`angular.json`的`assets`
- styles：
  - 負責全域樣式
  - 可以設定多個scss/css，會依照順序載入

### tsconfig.json
- path 設定import別名
```javascript
  "paths": {
    "@services/*": ["src/app/services/*"],
    "@components/*": ["src/app/components/*"]
  }

import { UserService } from "@services/user.service";
import { ButtonComponent } from "@components/button.component";
```
---
## 關於yarn

|功能|Yarn| NPM |
|---|---|-----|
|速度	|🚀 更快（並行安裝）|🐢 較慢（逐步安裝）|
|鎖定機制	|✅ yarn.lock 確保版本一致	|✅ package-lock.json 但比 yarn.lock 大|
|離線模式	|✅ 支援離線安裝	|❌ 需連線下載|
|可靠性	|✅ yarn 內建校驗機制	⚠️ |npm 可能因網路問題失敗|
|Monorepo	|✅ 支援 Workspaces|	⚠️ npm 7+ 開始支援|

