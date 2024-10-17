以下是一些常用的 `pip` 命令，`pip` 是 Python 的包管理工具，用于安装和管理 Python 包：

### 1. 安装包
```bash
pip install <package_name>
```
- **功能**: 安装指定的 Python 包。

### 2. 卸载包
```bash
pip uninstall <package_name>
```
- **功能**: 卸载已安装的包。

### 3. 查看已安装包列表
```bash
pip list
```
- **功能**: 列出所有已安装的包和它们的版本。

### 4. 更新包
```bash
pip install --upgrade <package_name>
```
- **功能**: 更新指定的包到最新版本。

### 5. 查看包的详细信息
```bash
pip show <package_name>
```
- **功能**: 显示某个已安装包的详细信息。

### 6. 查看过期包
```bash
pip list --outdated
```
- **功能**: 列出所有可以更新的包。

### 7. 安装指定版本的包
```bash
pip install <package_name>==<version>
```
- **功能**: 安装指定版本的包。

### 8. 冻结当前环境中的包
```bash
pip freeze > requirements.txt
```
- **功能**: 将当前环境中的包及其版本写入 `requirements.txt` 文件，方便迁移或重现环境。

### 9. 从文件安装包
```bash
pip install -r requirements.txt
```
- **功能**: 根据 `requirements.txt` 文件中的内容安装所有列出的包。

### 10. 检查是否有新版本的 pip
```bash
pip install --upgrade pip
```
- **功能**: 将 `pip` 更新到最新版本。

### 11. 搜索包
```bash
pip search <package_name>
```
- **功能**: 在 PyPI 上搜索与包名相关的包。

### 12. 检查依赖项
```bash
pip check
```
- **功能**: 检查已安装的包是否有任何不兼容的依赖项。

这些是常用的 `pip` 命令，可以帮助你管理 Python 的包和依赖。