from flask import Flask, jsonify, request, redirect
import requests
import subprocess
import os

app = Flask(__name__)

# 設定自訂目錄
USE_CUSTOM_DIRECTORY = False  # 是否使用自訂目錄(預設為False)
CUSTOM_DIRECTORY = '/home/hongyihank/skin/'  # 自訂目錄路徑

# 獲取XUID
def get_xuid(bedrock_username):
    try:
        # 根據布林值決定是否使用自訂目錄
        script_path = os.path.join(CUSTOM_DIRECTORY, 'get_xuid.js') if USE_CUSTOM_DIRECTORY else 'get_xuid.js'
        
        # 調用Node.js 腳本獲取XUID
        result = subprocess.run(
            ['node', script_path, bedrock_username.lstrip(".")],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

# 獲取texture_id
def get_bedrock_texture_id(xuid):
    url = f'https://api.geysermc.org/v2/skin/{xuid}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('texture_id')
    else:
        return None

# 獲取玩家頭像之圖片URL
def get_skin_head_url(uuid, is_bedrock=False):
    if is_bedrock:
        xuid = get_xuid(uuid)
        if not xuid:
            return None
        texture_id = get_bedrock_texture_id(xuid)
        if not texture_id:
            return None
        #可通過更改此處url以更換skin樣式
        # 基岩
        return f'https://mc-heads.net/head/{texture_id}'
    else:
        # Java
        return f'https://mc-heads.net/head/{uuid}'

# 重定向至mc-heads
@app.route('/skin/<uuid>', methods=['GET'])
def render_skin_head(uuid):
    if not uuid:
        return jsonify({'error': 'UUID is required'}), 400

    # 判斷是否為基岩玩家
    is_bedrock = uuid.startswith('.')
    skin_url = get_skin_head_url(uuid, is_bedrock)
    if not skin_url:
        return jsonify({'error': 'Skin not found'}), 404

    return redirect(skin_url)

# 更改監聽位置與連接埠
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
