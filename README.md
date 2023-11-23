# Bulk-deletion-of-Cloudflare-DNS-records

这个 Python 脚本允许用户列出并批量删除特定 Cloudflare Zone ID 下的 DNS 记录。

<img width="1489" alt="image" src="https://github.com/ymyuuu/Bulk-deletion-of-Cloudflare-DNS-records/assets/135582157/67702e1c-8d6d-4a9a-abce-f03a0afe2979">


## 如何使用

### 在 Replit 上运行

1. 点击 [项目链接](https://replit.com/@ymyuuu/Pi-Liang-Shan-Chu-Cloudflare-DNS-Ji-Lu) 在 Replit 上运行这个脚本。
2. 在终端中按照提示输入 Cloudflare 的 Zone ID 和 API Key。
3. 列出 DNS 记录后，根据提示选择要删除的记录的序号或类型进行删除。

### 运行在本地环境

1. 克隆项目到本地环境。
2. 安装 `requests` 库（如果未安装）：`pip install requests`。
3. 在终端中运行 `python script.py`。
4. 输入 Cloudflare 的 Zone ID 和 API Key，按照提示完成删除操作。

## 注意事项

- **谨慎操作：** 删除 DNS 记录前请确保你知道自己在做什么，以免造成不可恢复的损失。
- **Cloudflare API Key：** 请勿将 API Key 泄露到公共环境，确保只在安全的地方使用。

## 免责声明

本项目是为了方便批量删除 Cloudflare DNS 记录而开发，但使用本项目涉及到一定的风险和责任。在使用本项目之前，请务必注意以下内容：

- **风险承担：** 使用本项目可能会对您的网络配置产生影响，包括但不限于删除重要的 DNS 记录。请谨慎操作，并确保您知晓操作的后果。
- **数据丢失风险：** 删除 DNS 记录可能导致网站或服务不可用。请在操作之前备份重要记录，并确认删除操作不会影响您的业务。
- **Cloudflare API Key 安全：** 请确保在安全的环境下使用 Cloudflare API Key，并避免将其泄露给未经授权的人员或公共场所。

**免责声明：** 本项目的开发者和贡献者不对任何直接或间接使用本项目造成的损失或问题负责。使用者应自行承担使用本项目的全部风险和责任。

在使用本项目之前，请仔细阅读并理解以上免责声明。如果您对项目的功能或安全性有任何疑问，请勿使用或寻求专业建议。

## 许可证

本项目采用 MIT 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。

感谢你的使用！如果你对这个项目有任何改进或建议，也欢迎贡献代码或提出问题。
