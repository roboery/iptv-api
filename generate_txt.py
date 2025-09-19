import os
import re

# TV编号与频道名称映射表
tv_map = {
    "TV01": "三立iNEWS",
    "TV09": "中視新聞",
    "TV17": "民視新聞",
    "TV25": "台視新聞台",
    "TV28": "中天電視",
    "TV31": "TVBS NEWS",
    "TV32": "三立新聞台",
    "TV70": "鏡新聞",
    "TV82": "TVBS NEWS",
    "TV93": "華視新聞",
}

def extract_url_from_m3u8(file_path):
    """提取 m3u8 文件里的 YouTube 播放链接"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"https?://[^\s]+", content)
    return match.group(0) if match else None

def main():
    output_lines = []
    for tv_id, name in tv_map.items():
        file_name = f"{tv_id}.m3u8"
        if os.path.exists(file_name):
            url = extract_url_from_m3u8(file_name)
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
