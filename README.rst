http-upload-file
=================

vim, sublime文本编辑起可以直接上传到服务器配置路径

server install
---------------

server使用flask框架开发,推荐使用guicorn运行

安装依赖::

    pip install -r requirements.txt.

启动::

    gunicorn -w 2 -b 0.0.0.0:8888 file_upload:app

在浏览器访问 http://ip:port/ 出现test则可以访问

处于安全, 会限制上传的ip,
在文件 file\_upload.py 修改限制或者去除限制::

    @app.before_request
    def before_request():
        #可以做一些权限限制, 比如限制IP
        if not request.headers.getlist('X-Forwarded-For'):
            ip = request.remote_addr
        else:
            ip = request.headers.getlist('X-Forwarded-For')[0]
        if ip not in ['可以上传文件的ip']:
            return 'no permission - %s' % ip

如果使用supervisor启动, 像下面配置(替换成自己的路径): file-upload-server.ini

.. code-block:: guess

    [program:file-upload-server]
    environment=PATH="/home/ubuntu/.virtualenvs/file-upload-server/bin/"
    user=ubuntu
    command=python /var/code/file-upload-server/tornado_app.py
    autostart=true

Sublime Text插件
-----------------

Sublime Text插件 FileUpload_.

.. _FileUpload: https://github.com/wasw100/FileUpload


vim插件
-------

复制file-upload.vim 到 $HOME/.vim/plugin/ 文件夹下

.vimrc中可以添加如下配置提高上传体验: set cmdheight=2

插件配置
--------

vim的配置, key是配置的一个名字, 随便起, 最下面可以设置快捷上传命令

.. code-block::

    'test'{
        'upload_url': 'http://{server ip}:{server port}/',
        'local_prefix': '{local path prefix}',
        'remote_prefix': '{server path prefix}',
    },

sublime的设置, 在插件Menu下设置, 可以复制Default的配置到User中修改, 重新安装插件, 配置不消失
