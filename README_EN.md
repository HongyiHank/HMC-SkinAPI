
# *HMC-SkinAPI(Translated by GPT4)*
**Introduction to TydiumCraft Skin API**<br>
The TydiumCraft Skin API automatically sends a Minecraft username or UUID to the GeyserMC API to obtain a texture ID, then sends this texture ID to mc-heads to retrieve the player's Minecraft skin image.

**Introduction to HMC-SkinAPI**<br>
Due to recent instability with the [TydiumCraft Skin API](https://tydiumcraft.net/docs/skinapi), a temporary alternative was created. However, it currently lacks the following features, preventing it from fully replacing the TydiumCraft Skin API:<br>

- Cannot change skin style by modifying the URL (this can be resolved by changing `https://mc-heads.net/head/`).<br>
- Unable to request the API using UUID (solution unknown).<br>

This API first queries the Xbox XUID of Bedrock Edition players.<br>
Query methods include using an external API or [xbox-query](https://github.com/XiYang6666/xbox-query).<br>
The external API version is simpler to use but slower, whereas using xbox-query is faster.<br>
(The demo site of HMC-SkinAPI uses the external API method.)

📕 Story: Initially, I didn’t know the TydiumCraft Skin API implementation was documented on the official website, so I spent a long time figuring out my own method. The current implementation is my own design, so it might differ slightly from the TydiumCraft Skin API.
# Installation

1. External API<br>
   **Requirements Installation**<br>
   `Requires: Python >=3.8`<br>
   Install dependencies with `pip install -r https://raw.githubusercontent.com/HongyiHank/HMC-SkinAPI/refs/heads/main/requirements.txt`<br>
   or `pip install Flask requests`<br>
   (If an error occurs, try replacing `pip` with `pip3`.)<br>
   **Usage**<br>
   Run with `python HMC_SkinAPI.py`<br>
   (If an error occurs, try replacing `python` with `python3`.)<br>
2. xbox-query API<br>
   **Requirements Installation**<br>
   Same as the first method, but refer to the [xbox-query](https://github.com/XiYang6666/xbox-query) README to install xbox-query and log in (it’s recommended to create a new Microsoft account).<br>
   **Usage**<br>
   Ensure `get_xuid.js` and `HMC_SkinAPI_xq.py` are in the same directory.<br>
   (To use a different directory, set `USE_CUSTOM_DIRECTORY` to `True` in `HMC_SkinAPI_xq.py` and specify the path in the following line.)<br>
   Then, run with `python HMC_SkinAPI_xq.py`<br>
   (If an error occurs, try replacing `python` with `python3`.)<br>

> Note: `get_xuid.js` will run automatically after calling the API once; no need to run it manually.<br>
> Note: To change the listening address or port, modify `app.run(host='0.0.0.0', port=5000, debug=True)`.
