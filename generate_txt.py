import os
import re
import requests

# TV编号与频道名称映射表（省略部分，只展示前几个，完整表和之前一样）
tv_map = {
    "TV01": "三立iNEWS",
    "TV09": "中視新聞",
    "TV17": "民視新聞",
    "TV25": "台視新聞台",
    "TV31": "TVBS NEWS",
    "TV70": "鏡新聞",
    "TV93": "華視新聞",
}

# 外部仓库原始文件地址
BASE_URL = "https://raw.githubusercontent.com/ChiSheng9/iptv/master/"

def fetch_m3u8(tv_id):
    """下载指定 TVxx.m3u8 文件"""
    url = f"{BASE_URL}{tv_id}.m3u8"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    return None

def extract_url(content):
    """从 m3u8 文件内容提取 YouTube 播放链接"""
    if not content:
        return None
    match = re.search(r"https?://[^\s]+", content)
    return match.group(0) if match else None

def main():
    output_lines = []
    for tv_id, name in tv_map.items():
        print(f"正在处理 {tv_id} ...")
        content = fetch_m3u8(tv_id)
        if content:
            url = extract_url(content)
            if url:
                output_lines.append(f"{name}，{url}")
            else:
                output_lines.append(f"{name}，未找到链接")
        else:
            output_lines.append(f"{name}，文件不存在")

    with open("iptv.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
