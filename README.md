# 依赖安装方法
这个项目我是用了[Poetry](https://github.com/python-poetry/poetry)进行依赖管理。如果，你也可以像我一样，那我觉得这件事情，泰裤辣!
所以，在已经成功安装poetry工具的情况下，请直接运行以下命令进行依赖安装
```
poetry install
```

# 运行程序的方法
请在保证poetry创建的环境生效的情况下，在项目根目录下运行下列命令，然后按照termial的提示点开网页链接即可。
```
uvicorn --reload fastapi_tutorial.main:app
```