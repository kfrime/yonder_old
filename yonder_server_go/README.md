# yonder
    server and frontend of yonder blog 

## blog_mini_server_go
    mini server of blog implemented by golang
    
## 部署
    1. 创建配置文件，并填入个人密码等敏感信息
    `cp config.example.json config.json`
    
    2. 运行脚本
    `./run.sh`
    
## todo
    log 
    分页
    搜索
    Archive页
    数据库备份

## packages
    github.com/jinzhu/gorm
    github.com/gin-gonic/gin
    github.com/garyburd/redigo/redis

    // It protects sites from XSS attacks
    github.com/microcosm-cc/bluemonday

## changes
    connect to mysql
    connect to redis
    注册登陆
    分类CRUD
    文章CRUD
