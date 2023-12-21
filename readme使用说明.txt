本文件压缩包下载地址
https://wwbs.lanzouv.com/ixa7B1ikdcuf
密码:a6bx
https://wws.lanzoub.com/b00w7rwsh
https://cdn.npmmirror.com/binaries/chromedriver/102.0.5005.61/chromedriver_win32.zip
所有文件解压后放到同一个文件夹内（参考 目录.png）
修改config.txt内2-3行用户名和密码
运行 一键登录.exe
结束后，运行 2开机自启+定时启动（右键管理员运行）.bat


打包命令
pyinstaller 一键登录.py
一键登录.spec 修改环境，完整地址修改
datas=[('C:/Users/work/Desktop/Py/F8一键登录/venv/Lib/site-packages/onnxruntime/capi/onnxruntime_providers_shared.dll','onnxruntime//capi'),('C:/Users/work/Desktop/Py/F8一键登录/venv/Lib/site-packages/ddddocr/common.onnx','ddddocr'),('C:/Users/work/Desktop/Py/F8一键登录/venv/Lib/site-packages/ddddocr/common_old.onnx','ddddocr')],
二次注入
pyinstaller 一键登录.spec
打包默认使用系统路径的驱动，需要版本一致