# This is a sample Python script.
import uvicorn
import os
import subprocess
from datetime import datetime
from loguru import logger
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path
from fastapi.responses import FileResponse

# 定义变量 trus
app = FastAPI(docs_url=None, redoc_url="/redoc")
rectangle = True
# export_path = "/Users/xiaoqi/Desktop/fontre/pffjdk11"
# chrome_path = "/Users/xiaoqi/Downloads/Google Chrome.app/Contents/MacOS/Google Chrome"

export_path = "/app/data"
chrome_path = "/usr/bin/google-chrome"

@logger.catch  # 异常记录装饰器、放到下面好像不行、应该是异步的关系。
def my_function(x, y, z):
    return [x, y, z]

# 添加首页
@app.on_event("startup")
async def startup_event():
    logger.add("logs/request.log", rotation="10 MB")


class Item(BaseModel):
    type: str = Field(..., description="导出类型 pdf png")
    windowSize: str = Field(..., description="窗口大小 1920,1080")
    url: str = Field(..., description="网址 https://www.baidu.com")
    fileSize: int = Field(..., description="文件大小 字节")
    time: int = Field(..., description="页面加载等待时间 毫秒")


@app.get("/{file_path:path}")
def download_file(file_path: Path):
    logger.info("file_path:{}", file_path)
    # 提供文件名
    file_name = file_path.name
    logger.info("file_name:{}", file_name)
    # 检查文件路径是否存在
    if not file_path.exists():
        return {"error": "File not found"}

    return FileResponse(file_path, filename=file_name)

@app.post("/api/export")
async def export(data: Item):
    logger.info("data:{}", data)
    pattern = 'print-to-pdf'
    if data.type == 'pdf':
        pattern = 'print-to-pdf'
    elif data.type == 'png':
        pattern = 'screenshot'
    file_name = post_export(data.url, export_path, chrome_path, pattern, data.windowSize, data.time, data.fileSize,data.type)
    if file_name:
        return {"path": file_name}
    return '{}'
def post_export(url, export_path, chrome_path, pattern, windowSize, time, fileSize,type):
    fpd_name = f"export_{datetime.now().strftime('%Y%m%d%H%M%S')}.{type}"
    file_name = os.path.join(export_path, fpd_name)
    try:
        chrome_args = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-sandbox",
            "--acceptSslCerts",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--virtual-time-budget={time}",
            "--ignore-certificate-errors",
            "--disable-plugins",
            f"--window-size={windowSize}",
            f"--{pattern}={file_name}",
            url
        ]
        subprocess.run(chrome_args)
        for i in range(10):
            size = os.path.getsize(file_name)
            print(size)
            if size <= fileSize:
                subprocess.run(chrome_args)
            else:
                break
    except Exception as e:
        print(f"导出失败: {e}")

    return file_name


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=12306)
