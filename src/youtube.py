#!/usr/bin/env python
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=NX3YmSJSNyc']

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')


def download_m4a(urls):
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'format': 'm4a/bestaudio/best',
        # See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'm4a',
                        }]
    }    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    download_m4a(URLS)