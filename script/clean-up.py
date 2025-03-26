import os
import shutil
import subprocess

def clean_git():
    """刪除 .git 目錄並重新初始化 Git（跨平台支援）"""

    # 確保當前目錄存在 .git
    if os.path.exists(".git"):
        print("🔄 正在刪除 `.git` 目錄...")
        shutil.rmtree(".git")  # ✅ 跨平台刪除資料夾
        print("✅ `.git` 目錄已刪除")
    else:
        print("⚠ `.git` 目錄不存在，跳過刪除")

    # 重新初始化 Git
    print("🔄 重新初始化 Git...")
    subprocess.run(["git", "init"], check=True)
    print("✅ Git 初始化完成")

    # 可選：建立新的 Commit
    print("🔄 建立初始 Commit...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit after cleanup"], check=True)
    print("✅ 初始 Commit 完成")

    # 可選：提示設定遠端倉庫
    print("\n🚀 如果要重新設置遠端倉庫，請執行：")
    print("   git remote add origin <your-repo-url>")
    print("   git push -u origin main")

if __name__ == "__main__":
    clean_git()
