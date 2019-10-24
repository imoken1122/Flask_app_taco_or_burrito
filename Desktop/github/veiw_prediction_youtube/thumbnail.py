import subprocess
from tqdm import tqdm
import json
import shlex
def _get_thumbnail():
    with open("./json_file/items.json","r") as f:
        list_id = json.load(f)    
    # print(list_id)
        for id_ in tqdm(list_id):
            cmd = f"wget https://img.youtube.com/vi/{id_}/mqdefault.jpg -O ./image/{id_}.jpg"
            tokens = shlex.split(cmd)
            subprocess.run(tokens)
if __name__ == "__main__":
    _get_thumbnail()