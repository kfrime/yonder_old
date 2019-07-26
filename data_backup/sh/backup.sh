#!/bin/bash

#
# 数据备份
# 

# Mysql数据库配置
HOST=localhost
PORT=3306
USER=root
PASSWORD=root
DB=yonder

# 备份目录
BACKUP_ROOT=.

set -x

# 备份命令
mysqldump -h${HOST} -P${PORT} -u${USER} -p${PASSWORD} -B ${DB} > ${BACKUP_ROOT}/${DB}.sql

# 数据恢复命令
# mysql -h${HOST} -P${PORT} -u${USER} -p${PASSWORD} -B ${DB} < ${BACKUP_ROOT}/${DB}.sql
