# 管理员系统 (Admin System)

基于 Django 的管理员系统框架，提供用户管理、权限控制、操作日志等功能。

## 功能特性

- **用户认证**: 管理员登录/登出
- **仪表盘**: 系统数据统计概览
- **用户管理**: 用户的增删改查（CRUD）
- **权限控制**: 基于角色的权限管理（超级管理员/管理员/普通用户）
- **个人资料**: 用户个人信息管理
- **操作日志**: 记录所有管理操作

## 技术栈

- Python 3.12+
- Django 5.0+
- Bootstrap 5.3
- SQLite（默认，可切换为 PostgreSQL/MySQL）

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 创建超级管理员

```bash
python manage.py createsuperuser
```

### 4. 启动开发服务器

```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000/ 即可进入管理系统。

## 项目结构

```
admin_system/
├── admin_system/       # 项目配置
│   ├── settings.py     # 项目设置
│   ├── urls.py         # 根 URL 配置
│   └── wsgi.py         # WSGI 入口
├── accounts/           # 账号管理应用
│   ├── models.py       # 用户模型、操作日志模型
│   ├── views.py        # 登录、用户 CRUD、日志视图
│   ├── forms.py        # 表单定义
│   ├── urls.py         # 路由配置
│   └── admin.py        # Django Admin 注册
├── dashboard/          # 仪表盘应用
│   ├── views.py        # 仪表盘视图
│   └── urls.py         # 路由配置
├── templates/          # 模板文件
│   ├── base.html       # 基础布局（侧边栏 + 顶栏）
│   ├── accounts/       # 账号相关模板
│   └── dashboard/      # 仪表盘模板
├── static/             # 静态资源
│   └── css/style.css   # 自定义样式
├── requirements.txt    # 依赖列表
└── manage.py           # Django 管理命令
```

## 默认账户

首次使用需通过 `createsuperuser` 命令创建超级管理员账户。

## 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `DJANGO_SECRET_KEY` | Django 密钥 | 开发用默认值 |
| `DJANGO_DEBUG` | 调试模式 | `True` |
| `DJANGO_ALLOWED_HOSTS` | 允许的主机 | `*` |
