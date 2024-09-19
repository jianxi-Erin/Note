Git 是一种分布式版本控制系统，用于跟踪文件的更改和管理代码版本。它可以让多个开发者在一个项目上进行协作，同时提供了强大的功能来管理版本历史、分支和合并。

### 1. 配置

- **配置用户信息**：
  ```bash
  git config --global user.name "你的名字"
  git config --global user.email "你的邮箱地址"
  ```

- **查看配置**：
  ```bash
  git config --list
  ```

### 2. 仓库操作

- **初始化仓库**：
  ```bash
  git init
  ```

- **克隆仓库**：
  ```bash
  git clone <远程仓库地址>
  ```

### 3. 分支管理

- **查看分支**：
  ```bash
  git branch
  ```

- **创建新分支**：
  ```bash
  git branch <分支名>
  ```

- **切换分支**：
  ```bash
  git checkout <分支名>
  ```

- **创建并切换到新分支**：
  ```bash
  git checkout -b <分支名>
  ```

- **删除分支**：
  ```bash
  git branch -d <分支名>  # 删除本地分支
  git push origin --delete <分支名>  # 删除远程分支
  ```

- **合并分支**：
  ```bash
  git merge <分支名>
  ```

### 4. 提交与推送

- **查看当前状态**：
  ```bash
  git status
  ```

- **添加更改到暂存区**：
  ```bash
  git add <文件名>
  git add .  # 添加所有更改的文件
  ```

- **提交更改**：
  ```bash
  git commit -m "提交信息"
  ```

- **推送到远程仓库**：
  ```bash
  git push <远程仓库名> <分支名>
  ```

- **推送并设置上游分支**：
  ```bash
  git push -u <远程仓库名> <分支名>
  ```
- **推送并覆盖文件**：
  ```bash
  git push -force <远程仓库名> <分支名>
  ```
### 5. 拉取与更新

- **拉取远程仓库的更改**：
  ```bash
  git pull <远程仓库名> <分支名>
  ```

- **从远程仓库拉取并合并到当前分支**：
  ```bash
  git pull
  ```

### 6. 查看历史

- **查看提交历史**：
  ```bash
  git log
  ```

- **查看文件的提交历史**：
  ```bash
  git log <文件名>
  ```

- **查看提交历史的简洁格式**：
  ```bash
  git log --oneline
  ```

### 7. 标签管理

- **创建标签**：
  ```bash
  git tag <标签名>
  ```

- **查看标签**：
  ```bash
  git tag
  ```

- **推送标签到远程**：
  ```bash
  git push origin <标签名>
  ```

- **删除标签**：
  ```bash
  git tag -d <标签名>  # 删除本地标签
  git push origin --delete <标签名>  # 删除远程标签
  ```

### 8. 远程仓库管理

- **查看远程仓库**：
  ```bash
  git remote -v
  ```

- **添加远程仓库**：
  ```bash
  git remote add <远程名> <远程仓库地址>
  ```

- **删除远程仓库**：
  ```bash
  git remote remove <远程名>
  ```

- **修改远程仓库的 URL**：
  ```bash
  git remote set-url <远程名> <新的远程仓库地址>
  ```

### 9. 变基与撤销

- **变基操作**：
  ```bash
  git rebase <分支名>
  ```

- **撤销本地更改**：
  ```bash
  git checkout -- <文件名>  # 撤销工作区的更改
  git reset HEAD <文件名>  # 撤销暂存区的更改
  ```

- **撤销提交（不保留更改）**：
  ```bash
  git reset --hard HEAD^
  ```

- **撤销提交（保留更改）**：
  ```bash
  git reset --soft HEAD^
  ```

### 10. 解决冲突

- **查看冲突**：
  ```bash
  git status
  ```

- **手动解决冲突**，然后标记为已解决：
  ```bash
  git add <文件名>
  ```

- **继续合并**：
  ```bash
  git merge --continue
  ```

