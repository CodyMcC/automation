import time
import pychromecast
# from types import mime_types
from casting.types import mime_types

# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()
# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Office TV"])


cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()

mc = cast.media_controller
# mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
start = 0
for index, mime in enumerate(mime_types[start:]):
    if mime in ['application/vnd.apple.mpegurl', 'd/b']:
        print(f"({index + 1 + start} of {len(mime_types)}) skipping", mime)
        continue
    mc.play_media('https://dakboard.com/screen/uuid/650df1d1-11b864-3bf2-d6a8abbad51a', mime)
    # if index == 5:
    #     mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
    time.sleep(3)
    print(f"({index + 1 + start} of {len(mime_types)}) {mime}, {mc.status.idle_reason}")
    if mc.status.idle_reason != 'ERROR':
        break

# (431 of 715) application/vnd.apple.mpegurl, None


mc.block_until_active()
print(mc.status)
# MediaStatus(current_time=42.458322, content_id='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type='video/mp4', duration=596.474195, stream_type='BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state='PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)

mc.pause()
time.sleep(5)
mc.play()

# Shut down discovery
pychromecast.discovery.stop_discovery(browser)
