# Auto-Channel configuration file

MAX_CONSECUTIVE_RETRIES = 3 # TODO: If several consecutive files fail, exit program
MAX_SAME_FILE_RETRIES 	= 5 # Number of times to attempt playing a file before giving up

PLAYOUT_FILE    = 'playout.ini'
OUTPUT_LOCATION = 'rtmp://localhost/live/stream'

SCHEDULER_UPNEXT_VIDEO_FOLDER = 'upnext/video'
SCHEDULER_UPNEXT_AUDIO_FOLDER = 'upnext/audio'
SCHEDULER_UPNEXT_WISDOM_FILE  = 'upnext/wisdom.txt'

SERV_DRAWTEXT_X             = 25
SERV_DRAWTEXT_Y             = 25
SERV_DRAWTEXT_SHADOW_X      = 2
SERV_DRAWTEXT_SHADOW_Y      = 2
SERV_DRAWTEXT_SHADOW_COLOR  = 'black'
SERV_DRAWTEXT_FONT_FILE     = 'fonts/hc-too5.ttf'
SERV_DRAWTEXT_FONT_SIZE     = 52
SERV_DRAWTEXT_FONT_COLOR    = 'white'

SERV_OUTPUT_ASPECT  = "600:480"
SERV_OUTPUT_CRF     = 28
SERV_OUTPUT_PRESET  = 'ultrafast'

CLIENT_VIDEO_SCALE = '640x480'

CLIENT_DRAWTEXT_X = 25
CLIENT_DRAWTEXT_Y = 113
CLIENT_DRAWTEXT_SHADOW_X = 2
CLIENT_DRAWTEXT_SHADOW_Y = 2
CLIENT_DRAWTEXT_SHADOW_COLOR = 'black'
CLIENT_DRAWTEXT_FONT_FILE = 'fonts/hc-too5.ttf'
CLIENT_DRAWTEXT_FONT_SIZE = 32
CLIENT_DRAWTEXT_FONT_COLOR = 'white'

CLIENT_VCODEC			= 'h264'
CLIENT_ASPECT 			= '640:480'
CLIENT_FLAGS  			= '+cgop'
CLIENT_G 				= 30
CLIENT_ACODEC 			= 'aac'
CLIENT_STRICT 			= 1
CLIENT_AUDIO_BITRATE 	= '168k'
CLIENT_AUDIO_RATE 		= 44100
CLIENT_PRESET 			= 'ultrafast'
CLIENT_HLS_ALLOW_CACHE 	= 0
CLIENT_HLS_LIST_SIZE 	= 5
CLIENT_HLS_TIME			= 0.1
CLIENT_FORMAT			= 'hls'
CLIENT_PIX_FMT			= 'yuv444p'