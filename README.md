## Build docker image
docker build --no-cache -t ubuntu_chrome_export .

##容器目录 /app/data
##宿主机访问文件 需要挂载



#使用方式
##参数说明
class Item(BaseModel):
    type: str = Field(..., description="导出类型 pdf png")
    windowSize: str = Field(..., description="窗口大小 1920,1080")
    url: str = Field(..., description="网址 https://www.baidu.com")
    fileSize: int = Field(..., description="文件大小 字节")
    time: int = Field(..., description="页面加载等待时间 毫秒


###ip改成内网ip 端口容器自定义端口
curl --location 'http://127.0.0.1:12306/api/export' \
--header 'Content-Type: application/json' \
--header 'Cookie: SESSION=3003ec8b-5690-418e-9a49-152a5ba12a84' \
--data '{
  "type": "pdf",
  "windowSize": "1920,1080",
  "url": "https://www.baidu.com",
  "fileSize": 1000,
  "time": 1000
}'


###返回值
{
    "path": "data/export_20231221174816.pdf"
}