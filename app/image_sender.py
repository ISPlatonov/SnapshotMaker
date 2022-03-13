import zulip
import argparse


parser = argparse.ArgumentParser(description="Python script to send snapshots to specified Zulip channel (topic)")

parser.add_argument("--config", help="path to `.zuliprc` file")
parser.add_argument("--type", help="type of message; must be `stream` or `private`")
parser.add_argument("--channel", help="name of channel of the message")
parser.add_argument("--topic", help="name of topic of the message")
parser.add_argument("--image", "-i", help="path to image to be sent")


args = parser.parse_args()
config_path = ".zuliprc"
message_type = "stream"

if args.config:
    config_path = args.config-path
if args.type:
    message_type = args.type
if not (args.channel and args.topic and args.image):
    raise Exception("channel or topic or image path not specified")

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file=config_path)

# Upload a file
with open(args.image, "rb") as fp:
    image = client.upload_file(fp)

# Share the file by including it in a message.
client.send_message(
    {
        "type": message_type,
        "to": args.channel,
        "topic": args.topic,
        "content": "[new snapshot]({})".format(image["uri"]),
    }
)
