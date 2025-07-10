# 二手车销售平台（Used-car-sales）

## 1. 项目简介  
> 一个基于 python Django 的二手车销售，可用于毕业设计。
> 
## 2. 功能特性  
- ✅ 账户操作记录（注册记录，登录记录...）  
- ✅ 用户收藏
- ✅ 用户购买 
- ✅ 车辆搜索 
- ✅ 公告展示  

## 3. 快速启动
```bash
#进入目录
cd CarSales

#创建迁移文件
python manage.py makemigrations

#执行迁移文件
python manage.py migrate

#数据导入数据库
python .\Utils\dataUtils.py

#运行项目
python manage.py runserver
```

![车辆信息截图](https://github.com/shiyuan-0629/Used-car-sales/blob/master/images/car.png?raw=true)
![个人收藏截图](https://github.com/shiyuan-0629/Used-car-sales/blob/master/images/favorites.png?raw=true)
![登录信息截图](https://github.com/shiyuan-0629/Used-car-sales/blob/master/images/logininfo.png?raw=true)