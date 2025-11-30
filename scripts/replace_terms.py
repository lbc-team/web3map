#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import traceback
from pathlib import Path

MAX_LINKS_PER_TERM = 2  # 每个术语在同一文档中最多出现2次链接


def extract_terms_and_links(termlink_path):
    """从 termlink.md 文件中提取术语和对应的链接"""
    terms_dict = {}

    try:
        with open(termlink_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 使用正则表达式匹配 markdown 链接格式: [术语](链接)
        pattern = r'\[(.*?)\]\((.*?)\)'
        matches = re.findall(pattern, content)

        # 将匹配结果存入字典
        for term, link in matches:
            terms_dict[term] = link

    except Exception as e:
        print(f"Error in extract_terms_and_links at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise

    return terms_dict


def is_in_code_block(text, pos):
    """检查位置是否在代码块中"""
    before_text = text[:pos]
    # 计算三个反引号的数量
    triple_backticks = before_text.count('```')
    # 如果数量为奇数，说明在代码块中
    return triple_backticks % 2 == 1


def is_in_inline_code(text, pos):
    """检查位置是否在行内代码中"""
    # 向前查找最近的单个反引号
    start = text.rfind('`', 0, pos)
    if start == -1:
        return False

    # 检查这个反引号是否是三个反引号的一部分
    if start >= 2 and text[start-2:start+1] == '```':
        return False
    if start >= 1 and text[start-1:start+2] == '```':
        return False
    if start <= len(text) - 3 and text[start:start+3] == '```':
        return False

    # 向后查找配对的反引号
    end = text.find('`', pos)
    if end == -1:
        return False

    # 检查配对的反引号是否是三个反引号的一部分
    if end >= 2 and text[end-2:end+1] == '```':
        return False
    if end >= 1 and text[end-1:end+2] == '```':
        return False
    if end <= len(text) - 3 and text[end:end+3] == '```':
        return False

    return True


def is_in_link(text, pos, term_len):
    """检查术语是否在链接中（包括链接文本部分和URL部分）"""
    # 向前查找，看是否在 [...] 中
    before = text[:pos]
    # 查找最近的 [ 和 ]
    last_bracket_open = before.rfind('[')
    last_bracket_close = before.rfind(']')

    # 如果在 [...] 中
    if last_bracket_open != -1 and (last_bracket_close == -1 or last_bracket_open > last_bracket_close):
        return True

    # 向前查找，看是否在 (...) 中的URL部分
    last_paren_open = before.rfind('(')
    last_paren_close = before.rfind(')')

    # 如果在 (...) 中，且前面紧挨着 ]
    if last_paren_open != -1 and (last_paren_close == -1 or last_paren_open > last_paren_close):
        # 检查 ( 前面是否是 ]
        if last_paren_open > 0 and text[last_paren_open-1] == ']':
            return True

    return False


def is_in_url(text, pos):
    """检查是否在URL中"""
    # 向前查找，看是否在 http:// 或 https:// 之后
    before = text[:pos]
    # 查找最近的空格或行首
    last_space = max(before.rfind(' '), before.rfind('\n'), before.rfind('\t'))
    if last_space != -1:
        word = before[last_space+1:]
        if word.startswith('http://') or word.startswith('https://'):
            return True
    else:
        # 从行首开始
        if before.startswith('http://') or before.startswith('https://'):
            return True
    return False


def is_in_related_concepts_section(text, pos):
    """检查位置是否在'相关概念'部分"""
    before_text = text[:pos]

    # 查找最后一个三级或以上标题
    # 支持 ### 相关概念, ### 相关链接 等
    pattern = r'###\s*相关'
    matches = list(re.finditer(pattern, before_text))

    if not matches:
        return False

    # 获取最后一个"相关"标题的位置
    last_related_pos = matches[-1].start()

    # 检查在这之后是否还有其他同级或更高级的标题
    after_related = before_text[last_related_pos:]
    # 查找是否有 ## 或 ### (不包括相关)
    next_section = re.search(r'\n##\s', after_related)

    if next_section:
        # 如果找到了下一个章节，说明不在相关概念部分
        return False

    # 在相关概念部分
    return True


def remove_all_term_links(content, term_links):
    """移除所有术语链接，还原为纯文本"""
    result = content

    for term, link in term_links.items():
        # 匹配 [term](link) 格式
        pattern = re.compile(r'\[' + re.escape(term) + r'\]\(' + re.escape(link) + r'\)')
        result = pattern.sub(term, result)

    return result


def add_links_to_content(content, term_links):
    """为内容添加术语链接，每个术语最多替换2次"""
    # 首先移除所有已存在的术语链接
    result = remove_all_term_links(content, term_links)

    for term, link in term_links.items():
        link_count = 0  # 当前术语已添加的链接数
        markdown_link = f'[{term}]({link})'

        # 使用正则表达式查找所有匹配的术语
        # 使用单词边界 \b 确保只替换完整的词，而不是词的一部分
        # 对于包含特殊字符的术语（如 web3.js），需要特殊处理
        if re.search(r'[a-zA-Z]', term):
            # 如果术语包含英文字母，使用单词边界
            pattern = re.compile(r'\b' + re.escape(term) + r'\b')
        else:
            # 对于纯中文或其他字符，直接匹配
            pattern = re.compile(re.escape(term))
        matches = list(pattern.finditer(result))

        # 从后向前替换，避免位置偏移问题
        for match in reversed(matches):
            pos = match.start()

            # 检查是否在相关概念部分
            in_related_section = is_in_related_concepts_section(result, pos)

            # 如果在相关概念部分，总是添加链接（不计入限制）
            if in_related_section:
                if (not is_in_code_block(result, pos) and
                    not is_in_inline_code(result, pos) and
                    not is_in_link(result, pos, len(term)) and
                    not is_in_url(result, pos)):
                    result = result[:pos] + markdown_link + result[pos + len(term):]
                continue

            # 如果不在相关概念部分，应用链接数量限制
            if link_count >= MAX_LINKS_PER_TERM:
                continue

            # 检查是否应该跳过这个匹配
            if (is_in_code_block(result, pos) or
                is_in_inline_code(result, pos) or
                is_in_link(result, pos, len(term)) or
                is_in_url(result, pos)):
                continue

            # 替换为链接
            result = result[:pos] + markdown_link + result[pos + len(term):]
            link_count += 1

    return result


def replace_terms_in_file(file_path, terms_dict):
    """在文件中替换术语为对应的超链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 使用改进的链接添加函数
        new_content = add_links_to_content(content, terms_dict)

        # 如果内容有变化，写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False

    except Exception as e:
        print(f"Error in replace_terms_in_file at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise


def process_directory(directory, terms_dict):
    """处理目录下的所有 markdown 文件"""
    updated_count = 0
    skipped_count = 0
    total_count = 0

    try:
        # 递归获取所有 .md 文件
        for file_path in Path(directory).rglob('*.md'):
            total_count += 1
            try:
                if replace_terms_in_file(file_path, terms_dict):
                    updated_count += 1
                    print(f"✓ 已更新: {file_path}")
                else:
                    skipped_count += 1
            except Exception as e:
                print(f"✗ 错误 {file_path}: {e}")
                skipped_count += 1
                continue

    except Exception as e:
        print(f"Error in process_directory at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise

    print(f'\n处理完成！')
    print(f'  更新: {updated_count} 个文件')
    print(f'  跳过: {skipped_count} 个文件')
    print(f'  总计: {total_count} 个文件')


def main():
    try:
        # 设置路径
        script_dir = Path(__file__).parent
        termlink_path = script_dir / 'termlink.md'
        target_dir = script_dir.parent / 'solana'  # 默认处理 solana 目录

        # 确保目录存在
        if not target_dir.exists():
            raise FileNotFoundError(f"Directory {target_dir} does not exist")

        # 提取术语和链接
        terms_dict = extract_terms_and_links(termlink_path)
        print(f"从 termlink.md 中找到 {len(terms_dict)} 个术语")

        # 处理目录下的文件
        process_directory(target_dir, terms_dict)

    except Exception as e:
        print(f"Error in main at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
