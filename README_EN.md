
# *HMC-SkinAPI(Translated by GPT-4o)*
[Discord MC Chat](https://github.com/Xujiayao/Discord-MC-Chat) Supported player textures query, so the update is stopped.
****

🔤[**English readme**](https://github.com/HongyiHank/HMC-SkinAPI/blob/main/README_EN.md)<br>
You can call the API using https://api.hhdoubleh.us.to/skin/USERNAME (this is a sample website, it is recommended to set up your own)<br>

**Introduction to TydiumCraft Skin API**<br>
The TydiumCraft Skin API automatically sends the Minecraft username or UUID to the GeyserMC API to obtain the texture ID, then sends the texture ID to mc-heads to get the Minecraft skin image of the user.

**Introduction to HMC-SkinAPI**<br>
Due to the recent instability of the [TydiumCraft Skin API](https://tydiumcraft.net/docs/skinapi), a temporary alternative has been created. However, it cannot fully replace the TydiumCraft Skin API at the moment due to the following missing features:

- Unable to switch skin styles by changing the URL (can be resolved by changing `https://mc-heads.net/head/`)
- Unable to request the API using UUID (unknown solution)

This API first queries the Xbox XUID of Bedrock Edition players. <br>
The query method can either use an external API or the [xbox-query](https://github.com/XiYang6666/xbox-query) for the query. <br>
The external API version is easier to use but slower, while using xbox-query is the opposite.<br>
(The HMC-SkinAPI example website uses the external API method for querying)

📕 A little story: I initially did not know that the implementation method of the TydiumCraft Skin API was documented on their official website, so I thought for a long time about how to implement it. The current implementation is my own idea, so it may differ a bit from the TydiumCraft Skin API.

# Installation and Configuration

1. External API (playerdb.co)<br>
**Dependency Installation**<br>
`Requires: Python >=3.8`<br>
Install dependencies using `pip install -r https://raw.githubusercontent.com/HongyiHank/HMC-SkinAPI/refs/heads/main/requirements.txt`<br>
or `pip install Flask requests`<br>
(If you encounter errors, try replacing pip with pip3)<br>
**Usage**<br>
Run using `python HMC_SkinAPI.py`<br>
(If you encounter errors, try replacing python with python3)<br>

2. Xbox-query<br>
**Dependency Installation**<br>
Same as the first point, but you need to refer to the [xbox-query](https://github.com/XiYang6666/xbox-query) README to install xbox-query and log in (it is recommended to create a new Microsoft account)<br>
**Usage**<br>
Ensure that get_xuid.js and HMC_SkinAPI_xq.py are in the same directory.<br>
(If you want to use different directories, set `USE_CUSTOM_DIRECTORY` to `True` in HMC_SkinAPI_xq.py and specify the directory in the next line)<br>
Then run using `python HMC_SkinAPI_xq.py`<br>
(If you encounter errors, try replacing python with python3)<br>

> Note: get_xuid.js will automatically run after calling the API once, no need to run it manually<br>
> Note: To change the listening address or port, modify `app.run(host='0.0.0.0', port=5000, debug=True)`

# Implementation Method<br>

First, detect whether the player is a Bedrock Edition player. The detection method is to determine that if there is a dot (.) in front of the player’s name, they are classified as a Bedrock player; otherwise, they are classified as a JAVA player.<br>
If they are a JAVA player, they are directly redirected to mc-heads. If they are a Bedrock player, first use playerdb.co or xbox-query to obtain the player’s Xbox XUID.<br>
Then send the obtained Xbox XUID to `https://api.geysermc.org/v2/skin/` to retrieve the player’s texture ID.<br>
Finally, send the texture ID to mc-heads.

# Using External APIs

1. `https://api.geysermc.org/v2/skin/`<br>
2. `https://playerdb.co/api/player/xbox/` (optional)

# My Usage Scenario

My personal Minecraft server uses [GeyserMC](https://geysermc.org/) and [Discord MC Chat](https://github.com/Xujiayao/Discord-MC-Chat)<br>
Discord MC Chat supports using Webhooks and allows defining avatarAPI, but the default provided API does not support GeyserMC, so I changed the API to TydiumCraft Skin API.<br>
However, the TydiumCraft Skin API has not been very stable lately (it may also be down), so I developed an alternative.<br>
Note that if you are also using Discord MC Chat, you need to set useUuidInsteadOfName to False to use the player name to call the API.<br>
Currently, the API does not support UUID calls, and I cannot think of a solution, so if you know how to modify it, please email: admin@hhdoubleh.us.to or send a Pull Request.
