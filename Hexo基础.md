Hexo 是一个快速、简洁且功能强大的静态博客框架，常用于生成静态网站。以下是 Hexo 的一些常用命令及其功能：

### 1. 初始化项目
```bash
hexo init <folder>
```
- **说明**: 初始化一个新的 Hexo 项目。

### 2. 安装依赖
```bash
npm install
```
- **说明**: 在初始化 Hexo 项目后安装所需的依赖。

### 3. 生成静态文件
```bash
hexo generate
```
或者简写：
```bash
hexo g
```
- **说明**: 生成静态页面，输出到 `public` 文件夹中。

### 4. 启动本地服务器
```bash
hexo server
```
或者简写：
```bash
hexo s
```
- **说明**: 启动本地服务器，默认地址为 `http://localhost:4000/`。

### 5. 部署网站
```bash
hexo deploy
```
或者简写：
```bash
hexo d
```
- **说明**: 根据 `_config.yml` 中的部署配置，将生成的静态文件部署到指定平台（如 GitHub Pages）。

### 6. 清理缓存和生成文件
```bash
hexo clean
```
- **说明**: 清理 Hexo 生成的缓存文件和 `public` 文件夹，用于确保下次生成的文件没有缓存问题。

### 7. 新建文章
```bash
hexo new post "你的文章标题"
```
或者简写：
```bash
hexo n "你的文章标题"
```
- **说明**: 创建一个新的博客文章，会生成一个包含基本结构的 Markdown 文件。

### 8. 新建页面
```bash
hexo new page "你的页面名称"
```
- **说明**: 创建一个新页面，如 `about` 页面。

### 9. 列出帮助命令
```bash
hexo help
```
或者简写：
```bash
hexo h
```
- **说明**: 列出所有可用的命令及其简要说明。

### 10. 查看 Hexo 版本
```bash
hexo version
```
或者简写：
```bash
hexo v
```
- **说明**: 查看 Hexo 当前版本。

### 常用命令简表

| 命令                         | 简写      | 功能说明                           |
|------------------------------|-----------|------------------------------------|
| `hexo init <folder>`          | 无        | 初始化 Hexo 项目                  |
| `npm install`                 | 无        | 安装项目依赖                      |
| `hexo generate`               | `hexo g`  | 生成静态文件                      |
| `hexo server`                 | `hexo s`  | 启动本地服务器                    |
| `hexo deploy`                 | `hexo d`  | 部署网站                          |
| `hexo clean`                  | 无        | 清理缓存和生成文件                |
| `hexo new post <title>`       | `hexo n`  | 新建文章                          |
| `hexo new page <page-name>`   | 无        | 新建页面                          |
| `hexo help`                   | `hexo h`  | 查看帮助                          |
| `hexo version`                | `hexo v`  | 查看 Hexo 版本                    |

这些命令能够帮助你轻松管理 Hexo 项目。