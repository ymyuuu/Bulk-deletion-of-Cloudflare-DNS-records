import requests


print("\n欢迎关注 Mingyu 的 GitHub 仓库 https://github.com/ymyuuu")
print("感谢大家支持！\n\n")


def list_dns_records(zone_id, api_key):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            records = response.json()["result"]
            print("找到以下记录：")
            print("序号\t类型\t名称\t\t\t内容")
            for i, record in enumerate(records, start=1):
                # 使用ljust()方法填充列，保持相同的宽度
                print(f"{i}\t{record['type']}\t{record['name'].ljust(24)}{record['content']}")
            return records
        else:
            print("获取 DNS 记录失败。")
            return []
    except Exception as e:
        print(f"发生异常：{e}")
        return []

def delete_dns_record(records, zone_id, api_key):
    while True:
        selected_input = input("请输入需要删除的记录的序号或类型 (多个序号或类型用空格分隔,直接回车则退出程序): ")

        if not selected_input.strip():  # 如果输入为空，则退出程序
		print("已退出,感谢支持")
            break

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        selected_ids = selected_input.split()
        for index in selected_ids:
            try:
                index = int(index)
                record_id = records[index - 1]['id']
                delete_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
                delete_response = requests.delete(delete_endpoint, headers=headers)
                if delete_response.status_code == 200:
                    # 获取要删除的记录的详细信息
                    record = records[index - 1]
                    print(f"记录 {record['type']} {record['name']} - {record['content']} 删除成功！")
                else:
                    print(f"记录 ID {record_id} 删除失败。")
            except (ValueError, IndexError):
                print(f"序号 {index} 无效，请输入有效的序号。")

# 用户输入 Zone ID 和 Cloudflare API Key
zone_id = input("请输入您的 Zone ID: ")
api_key = input("请输入您的 Cloudflare API Key: ")

# 列出 DNS 记录
records = list_dns_records(zone_id, api_key)

if records:
    # 删除 DNS 记录
    delete_dns_record(records, zone_id, api_key)
