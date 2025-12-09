# 标签导出脚本使用说明

## 功能说明

这个脚本用于从MySQL数据库导出标签数据，并按主标签分组整理。

## 安装依赖

```bash
cd scripts
pip install -r requirements.txt
```

## 配置数据库

1. 复制环境变量配置文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的数据库连接信息：
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=your_database_name
```

## 运行脚本

```bash
python export_tags.py
```

## 输出文件

脚本会在 `output/` 目录下生成以下文件：

1. **tags_raw_YYYYMMDD_HHMMSS.json** - 原始SQL查询结果
   - 包含所有标签的原始数据
   - 包含主标签名称、父标签名称、使用次数等信息

2. **tags_organized_YYYYMMDD_HHMMSS.json** - 按主标签分组整理后的数据
   - 按主标签分组
   - 每个分组包含标签列表、统计信息
   - 包含元数据和Top10活跃分组

3. **tags_organized_latest.json** - 最新的整理数据（覆盖式）
   - 始终指向最新一次导出的整理数据
   - 方便其他程序引用最新数据

## 数据结构示例

### 整理后的数据结构

```json
{
  "metadata": {
    "total_tags": 1234,
    "total_main_tags": 50,
    "export_time": "2025-12-09T10:30:00",
    "group_by": "main_tag",
    "top_groups": [...]
  },
  "groups": {
    "ERC20": {
      "main_tag_id": 123,
      "tags": [
        {
          "id": 456,
          "name": "ERC-20",
          "parent_tag_name": "Token",
          "parent_id": 789,
          "category_id": 1,
          "usage_count": 1500,
          "followers": 300
        }
      ],
      "total_count": 10,
      "total_usage": 15000,
      "total_followers": 3000
    }
  }
}
```

## 数据说明

- **main_id**: 主标签的ID（例如：ERC-20的主标签是ERC20）
- **parent_id**: 父标签的ID（例如：ERC20的父标签是Token）
- **usage_count**: 标签被使用的次数（通过ask_taggables表统计）
- **followers**: 标签的关注者数量

## 标签层级关系示例

```
Token (父标签)
  └── ERC20 (主标签)
        └── ERC-20 (标签)
```

## 故障排除

### 连接数据库失败
- 检查 `.env` 文件中的数据库配置是否正确
- 确认数据库服务是否运行
- 检查数据库用户权限

### 找不到SQL文件
- 确保 `tag.sql` 文件在 scripts 目录下

### 缺少依赖
- 运行 `pip install -r requirements.txt` 安装依赖
