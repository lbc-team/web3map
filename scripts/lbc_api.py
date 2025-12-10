import os
import sys
import json
from dotenv import load_dotenv
import requests
from typing import Optional,TypedDict, List, Optional


load_dotenv(".env")


BASE_URL = os.getenv("LBC_SERVER_URL")
API_KEY = os.getenv("LBC_API_KEY")
print(BASE_URL, API_KEY)

headers = {"x-api-key": API_KEY}


def setmain_tag(main_tag_name: str, sub_tag_names: str) -> Optional[str]:

    tag_params = {
        "main_tag": main_tag_name,
        "sub_tags": sub_tag_names,
    }

    url = f"{BASE_URL}/api/tag/setting"

    response = requests.post(url, json=tag_params, headers=headers)

    if response.ok:
        data = response.json()
        if data.get("code") == 0:
            print(f"设置 {main_tag_name} 为主标签成功")
            return True
        else:
            print(f"设置 {main_tag_name} 为主标签失败 - 错误代码: {data}")
            return False
    else:
        print(f"设置 {main_tag_name} 为主标签失败 - HTTP状态码: {response.status_code}, 错误信息: {response.text}")
        return False

    return False

def update_tag(name: str, description: str, summary: str) -> Optional[str]:

    tag_params = {
        "name": name,
        "description": description,
    }

    if summary:
        tag_params["summary"] = summary

    # print(tag_params)

    url = f"{BASE_URL}/api/update/tag"

    response = requests.post(
        url, json=tag_params, headers=headers
    )

    if response.ok:
        data = response.json()
        if data.get("code") == 0:
            print(f"提交 {name} ok ")
        else:
            print(data)
    else:
        print(f"更新TAG信息失败 - HTTP状态码: {response.status_code}, 错误信息: {response.text}")


def get_tag_info(tag_name: str) -> Optional[str]:
    tag_info = None   
    try:
        response = requests.get(f"{BASE_URL}/api/get/tag/{tag_name}", headers=headers)

        if response.ok:
            data = response.json()
            if data.get("code") == 0:
                tag_info = data.get("tag", None)
            else:
                print(f"获取TAG信息失败 - 错误代码: {data}")
        else:
            print(
                f"获取TAG信息失败 - HTTP状态码: {response.status_code}, 错误信息: {response.text}"
            )
    except Exception as e:
        print(f"获取TAG信息异常 - 错误详情: {str(e)}")

    return tag_info


def update_video_info(video_id: str, fields: dict):
    success = False
    
    try:
        response = requests.post(f"{BASE_URL}/api/update/video/{video_id}", json=fields, headers=headers)

        if response.ok:
            data = response.json()
            if data.get("code") == 0:
                print(
                    f"更新TAG信息成功 - message: {data.get('message', '')}"
                )
                success = True
            else:
                print(f"更新TAG信息失败 - 错误代码: {data}")
        else:
            print(
                f"更新TAG信息失败 - HTTP状态码: {response.status_code}, 错误信息: {response.text}"
            )
    except Exception as e:
        print(f"获取TAG信息异常 - 错误详情: {str(e)}")

    return success


if __name__ == "__main__":
    tag_name = "EVM"
    tag_info = get_tag_info(tag_name)
    print(tag_info)

