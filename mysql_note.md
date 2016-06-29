# mysql笔记
```
sudo mysql -uroot -p
CREATE DATABASE cas_test;
CREATE USER cas IDENTIFIED BY 'wwjcas';
GRANT SELECT  ON cas_test.* TO 'cas'@'%' IDENTIFIED BY 'wwjcas'; 
# 阿里云的权限是所有端口开发 默认
# 远程访问
/etc/mysql/my.cnf 注释bind-address           = 127.0.0.1，考虑安全问题
#/
mycli -h mysqlhost  -u cas  #先用127.0.0.1替代， mycli -h 127.0.0.1/  -u root 则被拒绝
```

创建表

```sql
use cas_test;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

INSERT INTO `users` (`username`, `password`) VALUES ("remote_user", "remote_password")
```

在客户端

```sql
use cas_test;
SELECT * from users; -- 1 | remote_user | remote_password
```

需要用root创建，因为cas只有select权限


# 参考
http://blog.just4fun.site/learn-mysql.html
