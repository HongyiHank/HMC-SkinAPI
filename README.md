

# *HMC-SkinAPI*
[Discord MC Chat](https://github.com/Xujiayao/Discord-MC-Chat) 支援了player textures查詢，故本專案停止更新
****

🔤[**English readme**](https://github.com/HongyiHank/HMC-SkinAPI/blob/main/README_EN.md)<br>

可使用https://api.hhdoubleh.us.to/skin/USERNAME 來調用api(此為示例網站，建議自行架設)<br>

**TydiumCraft Skin API介紹**<br>
TydiumCraft Skin API 會自動將Minecraft 使用者名稱或UUID 發送至GeyserMC API以獲取texture ID，接著將texture ID 發送至mc-heads以獲取使用者之Minecraft Skin 圖片。

**HMC-SkinAPI介紹**<br>
由於近期[TydiumCraft Skin API](https://tydiumcraft.net/docs/skinapi) 不太穩定，所以做了一個臨時替代品
但目前因以下功能缺失而無法成為TydiumCraft Skin API之完全替代品

 - 無法通過更改url切換skin樣式(可通過更改`https://mc-heads.net/head/`來解決)
 - 無法通過UUID請求API(未知曉解決方法)

此API會先查詢基岩版玩家之XBOX XUID <br>
查詢方法分為使用外部API查詢與使用[xbox-query](https://github.com/XiYang6666/xbox-query) 查詢。<br>
外部API版本使用方式簡單，但獲取速度慢，而使用xbox-query 則反之<br>
(HMC-SkinAPI 示例網站使用外部API方法查詢)

📕小故事：我一開始不知道TydiumCraft Skin API 的實現方法有寫在官網上，所以我還想了很久要怎麼實現。目前的實現方是我自己想出來的，所以跟TydiumCraft Skin API 可能有一點不一樣。
# 安裝與配置

 1. 外部API(playerdb.co)<br>
**依賴安裝**<br>
`Requires: Python >=3.8`<br>
使用`pip install -r https://raw.githubusercontent.com/HongyiHank/HMC-SkinAPI/refs/heads/main/requirements.txt`<br>
或 `pip install Flask requests` 安裝依賴<br>
(如果報錯可嘗試將pip 替換為pip3)<br>
**使用方法**<br>
使用`python HMC_SkinAPI.py` 即可運行<br>
(如果報錯可嘗試將python 替換為 python3)<br>
 2. xbox-query<br>
 **依賴安裝**<br>
與第一點相同，但需要先參考[xbox-query](https://github.com/XiYang6666/xbox-query) 之readme 安裝xbox-query 並登錄(建議創一個新的Microsoft帳號)<br>
**使用方式**<br>
確保get_xuid.js 與HMC_SkinAPI_xq.py 在相同目錄<br>
(如果要使用相異目錄，請將HMC_SkinAPI_xq.py 中的`USE_CUSTOM_DIRECTORY` 設定為`True` 並在下一行設定目錄)<br>
接著使用使用`python HMC_SkinAPI_xq.py` 即可運行<br>
(如果報錯可嘗試將python 替換為 python3)<br>

> 備註：get_xuid.js 會在調用一次API後自動運行，不需手動運行<br>
> 備註：如果要更改監聽地址或端口，可以更改`app.run(host='0.0.0.0', port=5000, debug=True)`
# 實現方法<br>

首先偵測玩家是否為基岩版玩家，偵測方式為如果玩家名稱前方有.，則判定為基岩玩家，否則判定為JAVA玩家<br>
如果是JAVA玩家則直接重定向至mc-heads。如果是基岩玩家則先使用playerdb.co或xbox-query獲取玩家Xbox xuid<br>
接著將獲取到的Xbox xuid 發送至`https://api.geysermc.org/v2/skin/`以獲取玩家之texture ID<br>
最後將texture ID 發送至mc-heads。
# 使用之外部API

1. `https://api.geysermc.org/v2/skin/`<br>
2. `https://playerdb.co/api/player/xbox/`(可選)
# 我的使用情況

我個人的Minecraft Server 使用了[GeyserMC](https://geysermc.org/) 與[Discord MC Chat](https://github.com/Xujiayao/Discord-MC-Chat)<br>
Discord MC Chat 支援使用Webhook且可字定義avatarAPI，不過預設提供的API並不支援GeyserMC，所以我將API改為了TydiumCraft Skin API<br>
但最近TydiumCraft Skin API不是很穩定(也有可能掛了)，所以就開發了一個替代品出來<br>
要注意的是，如果你也使用Discord MC Chat，要把useUuidInsteadOfName改為False，這樣才會使用玩家名稱調用API<br>
目前API尚未支持使用UUID調用，而且我想不出解決方法，所以如果你知道如何修改，歡迎寄Email:admin@hhdoubleh.us.to 或發送至Pull Request
