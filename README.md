# Uplaod-Pictures-VPS-Publuc

上传⏫图片到 VPS 服务器

上传图片的后端账号和密码都是：admin<br>

要修改，请修改 /app/main.py 文件。

```python
# 把文件中这一行的代码中的 admin 改为你想要的密码就行

if credentials.username != "admin" or credentials.password != "admin":
```

所需环境请到 [搭建在线 Blog](http://localhost:4000/2021/11/22/%E6%90%AD%E5%BB%BA%E5%9C%A8%E7%BA%BF%E7%BC%96%E8%BE%91Blog/) & [超详细配置](https://www.sanzro.xyz/2021/08/13/Docker-CentOS-7-Anaconda-FastAPI-PostgreSQL-%E8%B6%85%E8%AF%A6%E7%BB%86%E9%85%8D%E7%BD%AE-%E5%87%BA%E9%94%99%E8%A7%A3%E5%86%B3/) 进行查阅<br><br>

*** 另外还需要在 /app/ 路径的同级下创建一个 /blog/assets/ 文件夹📂路径，以放上传的图片 ***<br><br>

安装好所需要的包之后，请运行以下命令进行 FastAPI 的运行
```bash
uvicorn main:app --host 0.0.0.0 --port 8011 --reload

# 其中 8011 为 main.py 中设置的 端口。
```

如果不需要使用 Nginx 的话，请在浏览器中输入（0.0.0.0为你的 VPS 的 IP）：http://0.0.0.0:8011/api/docs<br>

假设你做 Nginx 的配置，那么地址是：http://www.xxx.xxx/api/docs<br><br>

附上我的 Nginx 关键配置部分
```bash
       server {
           listen       80;
           listen       [::]:80;
           server_name  www.xxx.xxx;
           root         /usr/share/nginx/html;

           include /etc/nginx/default.d/*.conf;

           error_page 404 /404.html;
                location = /404.html {
           }

           error_page 500 502 503 504 /50x.html;
                location = /50x.html {
           }

            # fastapi 此处的 8011 是 Upload-Pitures-VPS-Public 中 /app/main.py 文件里配置好的 端口号
           location /api/docs {
               proxy_pass http://127.0.0.1:8011;
           }

           location /openapi.json {
               proxy_pass http://127.0.0.1:8011/openapi.json;
           }

           location /api/pictures {
               proxy_pass http://127.0.0.1:8011/api/pictures;
           }
       }
    }
```

*** 注：我没有编写删除图片的 API，可以仿照 ``/app/api/v1/Pictures/Pictures.py`` 中的方法进行编写，不然就要手动登录上 VPS 使用 ``rm -rf xxx.png`` 进行删除。 ***<br><br>

另：时间仓促，没有做很好的登录校验，以及很好的前端页面去解析这个接口，以后有机会的话再细化了。
