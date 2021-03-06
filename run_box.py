import yaml
from dandelion import Box
from dandelion.utils import create_id
import os


if __name__ == '__main__':
    ROOT_DIR = os.environ["ROOT_DIR"] = os.path.dirname(__file__)
    # Load config file
    f = open(os.path.join(ROOT_DIR, "config.yaml"), "r")
    config = yaml.safe_load(f)
    try:
        base_dir = config["BASE_DIRECTORY"]
    except KeyError:
        base_dir = "/tmp"
    # Get box id
    id = ''
    try:
        f = open(os.path.join(base_dir, "box-id.txt"), "r")
        id = f.read()
        f.close()
    except IOError:
        pass
    if not id or id[:4] != "box-":
        id = create_id("box")
        f = open(os.path.join(base_dir, "box-id.txt"), "w")
        f.write(id)
        f.close()
    print("Your ID: %s" % id)
    redis_address = (config["REDIS_HOST"], config["REDIS_PORT"])
    box = Box(id,
              server_ip=config["BOX_SERVER_IP"],
              client_ip=None,
              port=config["BOX_PORT"],
              proxy_port=config["BOX_SERVER_PROXY_PORT"],
              entrance_urls=config["ENTRANCE_URLS"],
              redis_address=redis_address,
              redis_db=config["DB"],
              server_redis_minsize=config["SERVER_REDIS_MINSIZE"],
              server_redis_maxsize=config["SERVER_REDIS_MAXSIZE"],
              client_redis_minsize=config["CLIENT_REDIS_MINSIZE"],
              client_redis_maxsize=config["CLIENT_REDIS_MAXSIZE"],
              ping_entrance_freq=config["BOX_PING_ENTRANCE_FREQ"],
              base_directory=config["BASE_DIRECTORY"])
    box.start()
