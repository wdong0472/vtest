# Total Productive Management System
==================================

Markdown

一、开发环境配置步骤
--------------------------------------------------------------------------------------

1.python setup (勾选安装环境变量\安装Pip)

2.安装Virtualenv
```javascript
$ pip install virtualenv
```
3.virtualenv xxx 如：vtest

4.cd xxx/bin  source activate 或者 windows下  cd  xxx/Scripts 执行 activate 进入虚拟环境

5.（vtest）：pip install django==1.11.3 django-suit==0.2.25

6.svn checkout https://kmopt_server.kmopt.com:8443/svn/Qrik

7.安装wingide，并打开Qrik 工程，保存工程文件到Qrik同级目录中

8.Fuck IT!

--------------------------------------------------------------------------------------
二、Django 常用命令
--------------------------------------------------------------------------------------
1.django-amdin startproject xxx
2.python manage.py startapp xxx
3.python manage.py makemigrations
4.python manage.py migrate
5.python manage.py flush


三、WingIDE使用技巧
--------------------------------------------------------------------------------------
[wingide]部分快捷键
orangleliu orangleliu 2013-04-12 22:28:00
WingIde的快捷键
    tab：自动补全
    Alt+1：打开所有折叠
    Alt+2：折叠所有classes
    Alt+3：折叠所有函数和类
    Alt+Backspace：删除光标所在单词的光标前的部分 
    Alt+括号：打印出整个括号
    Alt+↑或者Alt+↓：关闭或者打开光标所在的一个折叠
    Alt+←或者Alt+→：切换光标上一个下一个位置
    Alt+Home：关闭所有折叠
    Alt+End: 关闭所有折叠
    Alt+F3：打开搜索模式
    Alt+F5：运行当前的文件
    Shift+Enter：向上新建一行
    Shift+Enter：向下新建一行
--------------------------------------------------------------------------------------

三、工程文件夹说明
--------------------------------------------------------------------------------------
1.qrik_data： 基础数据定义模块

  描述：该模块使用默认Admin后台进行数据的维护管理，不做开发
  
  只需定义好model，admin，用于管理数据字典、系统参数等公共基础数据维护

2.qrik_libs：基础类库

  描述：该模块为库、基类、辅助函数等工具库的定义，用于集中管理公共方法

3.qrik_tools：开发配置工具
  
  描述：该模块为开发人员辅助开发、基础配置工具，用于界面UI参数配置管理，使用Admin进行数据的维护管理，不做开发

4.qrik_ui：共用UI
   
  描述：该模块为登录页面、主界面、UI组件等共用UI界面的集中管理
  
5.qrik_test: 测试
 
  描述：测试开发框架中的功能模块
  
6.qrik_widgets: 公用组件构建代码

  描述：供其他页面调用
  
7.qrik_demo: 示例

  描述：常用类库、widgets使用方法、异常处理规范等实例

5.static：静态资源文件夹

  描述：用于发布部署时，将各模块静态资源文件集中到该文件夹，托管给Web Server进行管理，通过Web server缓存，提供浏览器加载性能

6.templates:UI模板文件夹

  描述：用于发布部署时，将各模块模板页面集中到该文件夹，便于统一发布管理

7.tpm:工程主应用模块

  描述：全局配置管理模块  

8.tpm_info：设备基础信息管理模块

9.tpm_spare_parts:设备备品备件管理模块

10.tpm_standard: 设备标准管理模块

11.tpm_scheme：设备方案管理模块

12.tpm_preventive：预防维修管理模块

13.tpm_falut：缺陷维修管理模块

14.tpm_failure：应急维修管理模块

15.tpm_query：综合查询统计模块

16.tpm_services：设备接口管理模块

17.tpm_spot：设备点检管理模块

18.tpm_bi:设备信息发布展示


--------------------------------------------------------------------------------------

