#### python

#### python 安装

1. 创建项目 django-admin startproject my_project
1. 安装指定版本  pip install django==3.0     
1. 安装项目依赖 pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r magpie/requirements.txt
1. 创建虚拟环境  python3 -m venv venv    
1. 启动项目 python manage.py runserver 
1. 指定端口号启动项目 python manage.py runserver 9527    
1. 指定ip启动项目 python manage.py runserver 192.168.31.119:9527
1. 创建hello模块 python manage.py startapp hello 

#### ORM

```
1. 创建hello模块 python manage.py startapp hello  
2. 检查models 模块的语法是否错误 python manage.py check
3. Models 对应生成同步源语  python manage.py makemigrations(迁移)
4. 执行同步，生成对应的数据库表 python manage.py migrate
```



内键  外键 复合类型 







