# Flask To-Do List Application

一个简单的基于 Flask 的待办事项列表应用程序。

## 功能特性

- 查看所有任务
- 添加新任务
- 删除任务
- 响应式界面设计
- 内存存储（重启后数据会丢失）

## 安装和运行

1. 克隆仓库：
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python todo_app.py
```

4. 在浏览器中访问：`http://127.0.0.1:5000`

## 项目结构

```
.
├── todo_app.py          # 主应用文件
├── requirements.txt     # Python 依赖
└── README.md           # 项目说明
```

## 技术栈

- Python 3.x
- Flask 2.3.3
- HTML/CSS (内嵌)

## 注意事项

- 任务数据存储在内存中，应用重启后会丢失
- 这是一个演示项目，不适合生产环境使用