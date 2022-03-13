import zulip
import argparse


def send_image(channel, topic, image_path, config_path=".zuliprc", message_type="stream"): 
    # Pass the path to your zuliprc file here.
    client = zulip.Client(config_file=config_path)

    # Upload a file
    with open(image_path, "rb") as fp:
        image = client.upload_file(fp)
    #print(zip(image))
    # Share the file by including it in a message.
    client.send_message(
        {
            "type": message_type,
            "to": channel,
            "topic": topic,
            "content": "[new snapshot]({})".format(image["uri"]),
        }
    )

'''
parser = argparse.ArgumentParser(description="Python script to send snapshots to specified Zulip channel (topic)")

parser.add_argument("--config", help="path to `.zuliprc` file")
parser.add_argument("--type", help="type of message; must be `stream` or `private`")
parser.add_argument("--channel", help="name of channel of the message")
parser.add_argument("--topic", help="name of topic of the message")
parser.add_argument("--image", "-i", help="path to image to be sent")


args = parser.parse_args()
config_path = ".zuliprc"
message_type = "stream"
channel = args.channel
topic = args.topic
image_path = args.image

if args.config:
    config_path = args.config
if args.type:
    message_type = args.type
#if (args.channel and args.topic and args.image):
#    send(config_path, message_type, channel, topic, image_path)
'''

#if __name__ == "__main__":
#    result = send_image(channel, topic, image_path, config_path, message_type)
    #print(result)

