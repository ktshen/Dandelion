from dandelion import Entrance
import uuid
import yaml
import os

if __name__ == '__main__':
    ROOT_DIR = os.environ["ROOT_DIR"] = os.path.dirname(__file__)
    f = open(os.path.join(ROOT_DIR, "entrance-config.yaml"), "r")
    config = yaml.safe_load(f)
    try:
        base_dir = config["BASE_DIRECTORY"]
    except KeyError:
        base_dir = "/tmp"
    id = ''
    try:
        f = open(os.path.join(base_dir, "entrance-id.txt"), "r")
        id = f.read()
        f.close()
    except IOError:
        pass
    if not id or "entrance-" not in id:
        id = "entrance-" + uuid.uuid4().hex
        f = open(os.path.join(base_dir, "entrance-id.txt"), "w")
        f.write(id)
        f.close()
    print("Your ID: %s" % id)

    redis_address = (config["REDIS_HOST"], config["REDIS_PORT"])
    entrance = Entrance(id=id, ip=config["ENTRANCE_IP"], port=config["ENTRANCE_PORT"],
                        redis_address=redis_address,
                        redis_db=config["DB"],
                        redis_minsize=config["ENTRANCE_REDIS_MINSIZE"],
                        redis_maxsize=config["ENTRANCE_REDIS_MAXSIZE"],
                        expire_box_time=config["ENTRANCE_EXPIRE_BOX_TIME"],
                        amount_of_boxes_per_request=config["AMOUNT_OF_BOXES_PER_REQUEST"],
                        proxy_port=config["ENTRANCE_SERVER_PROXY_PORT"],
                        other_entrances_urls=config["ENTRANCE_OTHER_URLS"],
                        mysql_host=config["ENTRANCE_MYSQL_HOST"],
                        mysql_password=config["ENTRANCE_MYSQL_PASSWORD"],
                        mysql_db=config["ENTRANCE_MYSQL_DB"],
                        mysql_user=config["ENTRANCE_MYSQL_USER"],
                        mysql_port=config["ENTRANCE_MYSQL_PORT"],
                        )
    entrance.serve_forever()
