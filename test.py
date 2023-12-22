import subprocess
import shlex



def work03():
    # 执行CMD命令
    command = ["/Users/xiaoqi/Downloads/Google\ Chrome.app/Contents/MacOS/Google\ Chrome", "--headless", "--disable-gpu",
               "--hide-scrollbars", "--no-sandbox", "--acceptSslCerts", "--no-pdf-header-footer",
               "--virtual-time-budget=7000",
               "--ignore-certificate-errors", "--disable-plugins", "--window-size=1920,1080",
               "--screenshot=/Users/xiaoqi/Desktop/fontre/pffjdk11/22.jpg",
               "https://cloud.tencent.com/developer/article/2218767?areaSource=102001.11&traceId=xUNlBd4TFXXr2FtWrGE6C"]

    cmd = "/Users/xiaoqi/Downloads/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --hide-scrollbars --no-sandbox --no-pdf-header-footer " \
          "--run-all-compositor-stages-before-draw --virtual-time-budget=5000 --ignore-certificate-errors --disable-plugins --window-size=1920,1080 " \
          "--screenshot=/Users/xiaoqi/Desktop/fontre/pffjdk11/22.jpg https://www.baidu.com"

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    print("标准输出:", result.stdout)
    print("标准错误:", result.stderr)
    print("返回码:", result.returncode)

if __name__ == '__main__':
    work03()