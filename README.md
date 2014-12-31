Ananse - A true cross platform downloader base on [youtube-dl](https://github.com/rg3/youtube-dl)

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [FEATURES](#features)
- [OPTIONS](#options)
- [OUTPUT TEMPLATE](#output-template)
- [VIDEO SELECTION](#video-selection)
- [DEVELOPER INSTRUCTIONS](#developer-instructions)
- [CONTRIBUTING]()
- [BUGS](#bugs)
- [COPYRIGHT](#copyright)

# INSTALLATION

**Still under development** but if you want to try it right away 
refer to the developer instructions below for how to check out and work with the git repository. 

# DESCRIPTION
**Ananse** is a download manager in every sense of the word allowing you to download videos 
and files from multiple sites including Youtube.com. It requires the Python interpreter, version
2.6, 2.7, or 3.2+, and it is not platform specific. It should work on
your Unix box, on Windows or on Mac OS X. It is released to the public domain,
which means you can modify it, redistribute it or use it however you like.
It is build on [youtube-dl](http://rg3.github.io/youtube-dl), Although it has been restructured
to provide the features below, it is still compatible with youtube-dl

# FEATURES

1.  **GUI Support (not implemented)** 
See all your downloads and set downloading options for all downloads without typing a single thing at the command line
2.  **Command Line Usage** 
Use Ananse from the command line as you will use any other command line application
3.  **Browser Integration (not implemented)**
Integrates into any internet application to take over downloads using easily understood and implemented APIs
4.  **Video Grabber (not implemented)** 
Easily downloads streaming videos with only one click
5.  **Support Many types of Protocols and Proxy Servers**
Provide support for many types of protocols and proxy server like ftp, http/https, rtmp etc
6.  **Download Categorization (not implemented)** 
Automatically organize all your downloads using defined download categories to make locating downloaded files easy
7.  **Download Acceleration (not implemented)** 
Speeds up downloading by up to  5 time due to intelligent dynamic file segmentation technology
8.  **Download Resume**
Ananse will resume unfinished download from the place where they left off. 
Comprehensive error recovery and resume capability will restart broken or interrupted downloads 
due to lost or dropped connections, network problems, computer shutdowns, or unexpected power outages.

For any feature not included open an issues and label it as a feature request

# OPTIONS

Since we are restructuring the application not all options will work as expected for now

    -h, --help                       print this help text and exit
    --version                        print program version and exit
    -U, --update                     update this program to latest version. Make
                                     sure that you have sufficient permissions
                                     (run with sudo if needed)
    -i, --ignore-errors              continue on download errors, for example to
                                     skip unavailable videos in a playlist
    --abort-on-error                 Abort downloading of further videos (in the
                                     playlist or the command line) if an error
                                     occurs
    --dump-user-agent                display the current browser identification
    --list-extractors                List all supported extractors and the URLs
                                     they would handle
    --extractor-descriptions         Output descriptions of all supported
                                     extractors
    --proxy URL                      Use the specified HTTP/HTTPS proxy. Pass in
                                     an empty string (--proxy "") for direct
                                     connection
    --socket-timeout None            Time to wait before giving up, in seconds
    --default-search PREFIX          Use this prefix for unqualified URLs. For
                                     example "gvsearch2:" downloads two videos
                                     from google videos for  youtube-dl "large
                                     apple". Use the value "auto" to let
                                     youtube-dl guess ("auto_warning" to emit a
                                     warning when guessing). "error" just throws
                                     an error. The default value "fixup_error"
                                     repairs broken URLs, but emits an error if
                                     this is not possible instead of searching.
    --ignore-config                  Do not read configuration files. When given
                                     in the global configuration file /etc
                                     /youtube-dl.conf: Do not read the user
                                     configuration in ~/.config/youtube-
                                     dl/config (%APPDATA%/youtube-dl/config.txt
                                     on Windows)
    --flat-playlist                  Do not extract the videos of a playlist,
                                     only list them.

## Video Selection:
    --playlist-start NUMBER          playlist video to start at (default is 1)
    --playlist-end NUMBER            playlist video to end at (default is last)
    --match-title REGEX              download only matching titles (regex or
                                     caseless sub-string)
    --reject-title REGEX             skip download for matching titles (regex or
                                     caseless sub-string)
    --max-downloads NUMBER           Abort after downloading NUMBER files
    --min-filesize SIZE              Do not download any videos smaller than
                                     SIZE (e.g. 50k or 44.6m)
    --max-filesize SIZE              Do not download any videos larger than SIZE
                                     (e.g. 50k or 44.6m)
    --date DATE                      download only videos uploaded in this date
    --datebefore DATE                download only videos uploaded on or before
                                     this date (i.e. inclusive)
    --dateafter DATE                 download only videos uploaded on or after
                                     this date (i.e. inclusive)
    --min-views COUNT                Do not download any videos with less than
                                     COUNT views
    --max-views COUNT                Do not download any videos with more than
                                     COUNT views
    --no-playlist                    If the URL refers to a video and a
                                     playlist, download only the video.
    --age-limit YEARS                download only videos suitable for the given
                                     age
    --download-archive FILE          Download only videos not listed in the
                                     archive file. Record the IDs of all
                                     downloaded videos in it.
    --include-ads                    Download advertisements as well
                                     (experimental)

## Download Options:
    -r, --rate-limit LIMIT           maximum download rate in bytes per second
                                     (e.g. 50K or 4.2M)
    -R, --retries RETRIES            number of retries (default is 10)
    --buffer-size SIZE               size of download buffer (e.g. 1024 or 16K)
                                     (default is 1024)
    --no-resize-buffer               do not automatically adjust the buffer
                                     size. By default, the buffer size is
                                     automatically resized from an initial value
                                     of SIZE.
    --playlist-reverse               Download playlist videos in reverse order

## Filesystem Options:
    -a, --batch-file FILE            file containing URLs to download ('-' for
                                     stdin)
    --id                             use only video ID in file name
    -o, --output TEMPLATE            output filename template. Use %(title)s to
                                     get the title, %(uploader)s for the
                                     uploader name, %(uploader_id)s for the
                                     uploader nickname if different,
                                     %(autonumber)s to get an automatically
                                     incremented number, %(ext)s for the
                                     filename extension, %(format)s for the
                                     format description (like "22 - 1280x720" or
                                     "HD"), %(format_id)s for the unique id of
                                     the format (like Youtube's itags: "137"),
                                     %(upload_date)s for the upload date
                                     (YYYYMMDD), %(extractor)s for the provider
                                     (youtube, metacafe, etc), %(id)s for the
                                     video id, %(playlist_title)s,
                                     %(playlist_id)s, or %(playlist)s (=title if
                                     present, ID otherwise) for the playlist the
                                     video is in, %(playlist_index)s for the
                                     position in the playlist. %(height)s and
                                     %(width)s for the width and height of the
                                     video format. %(resolution)s for a textual
                                     description of the resolution of the video
                                     format. %% for a literal percent. Use - to
                                     output to stdout. Can also be used to
                                     download to a different directory, for
                                     example with -o '/my/downloads/%(uploader)s
                                     /%(title)s-%(id)s.%(ext)s' .
    --autonumber-size NUMBER         Specifies the number of digits in
                                     %(autonumber)s when it is present in output
                                     filename template or --auto-number option
                                     is given
    --restrict-filenames             Restrict filenames to only ASCII
                                     characters, and avoid "&" and spaces in
                                     filenames
    -A, --auto-number                [deprecated; use  -o
                                     "%(autonumber)s-%(title)s.%(ext)s" ] number
                                     downloaded files starting from 00000
    -t, --title                      [deprecated] use title in file name
                                     (default)
    -l, --literal                    [deprecated] alias of --title
    -w, --no-overwrites              do not overwrite files
    -c, --continue                   force resume of partially downloaded files.
                                     By default, youtube-dl will resume
                                     downloads if possible.
    --no-continue                    do not resume partially downloaded files
                                     (restart from beginning)
    --no-part                        do not use .part files - write directly
                                     into output file
    --no-mtime                       do not use the Last-modified header to set
                                     the file modification time
    --write-description              write video description to a .description
                                     file
    --write-info-json                write video metadata to a .info.json file
    --write-annotations              write video annotations to a .annotation
                                     file
    --write-thumbnail                write thumbnail image to disk
    --load-info FILE                 json file containing the video information
                                     (created with the "--write-json" option)
    --cookies FILE                   file to read cookies from and dump cookie
                                     jar in
    --cache-dir DIR                  Location in the filesystem where youtube-dl
                                     can store some downloaded information
                                     permanently. By default $XDG_CACHE_HOME
                                     /youtube-dl or ~/.cache/youtube-dl . At the
                                     moment, only YouTube player files (for
                                     videos with obfuscated signatures) are
                                     cached, but that may change.
    --no-cache-dir                   Disable filesystem caching
    --rm-cache-dir                   Delete all filesystem cache files

## Verbosity / Simulation Options:
    -q, --quiet                      activates quiet mode
    --no-warnings                    Ignore warnings
    -s, --simulate                   do not download the video and do not write
                                     anything to disk
    --skip-download                  do not download the video
    -g, --get-url                    simulate, quiet but print URL
    -e, --get-title                  simulate, quiet but print title
    --get-id                         simulate, quiet but print id
    --get-thumbnail                  simulate, quiet but print thumbnail URL
    --get-description                simulate, quiet but print video description
    --get-duration                   simulate, quiet but print video length
    --get-filename                   simulate, quiet but print output filename
    --get-format                     simulate, quiet but print output format
    -j, --dump-json                  simulate, quiet but print JSON information.
                                     See --output for a description of available
                                     keys.
    -J, --dump-single-json           simulate, quiet but print JSON information
                                     for each command-line argument. If the URL
                                     refers to a playlist, dump the whole
                                     playlist information in a single line.
    --newline                        output progress bar as new lines
    --no-progress                    do not print progress bar
    --console-title                  display progress in console titlebar
    -v, --verbose                    print various debugging information
    --dump-intermediate-pages        print downloaded pages to debug problems
                                     (very verbose)
    --write-pages                    Write downloaded intermediary pages to
                                     files in the current directory to debug
                                     problems
    --print-traffic                  Display sent and read HTTP traffic

## Workarounds:
    --encoding ENCODING              Force the specified encoding (experimental)
    --no-check-certificate           Suppress HTTPS certificate validation.
    --prefer-insecure                Use an unencrypted connection to retrieve
                                     information about the video. (Currently
                                     supported only for YouTube)
    --user-agent UA                  specify a custom user agent
    --referer URL                    specify a custom referer, use if the video
                                     access is restricted to one domain
    --add-header FIELD:VALUE         specify a custom HTTP header and its value,
                                     separated by a colon ':'. You can use this
                                     option multiple times
    --bidi-workaround                Work around terminals that lack
                                     bidirectional text support. Requires bidiv
                                     or fribidi executable in PATH

## Video Format Options:
    -f, --format FORMAT              video format code, specify the order of
                                     preference using slashes: -f 22/17/18 .  -f
                                     mp4 , -f m4a and  -f flv  are also
                                     supported. You can also use the special
                                     names "best", "bestvideo", "bestaudio",
                                     "worst", "worstvideo" and "worstaudio". By
                                     default, youtube-dl will pick the best
                                     quality. Use commas to download multiple
                                     audio formats, such as -f
                                     136/137/mp4/bestvideo,140/m4a/bestaudio.
                                     You can merge the video and audio of two
                                     formats into a single file using -f <video-
                                     format>+<audio-format> (requires ffmpeg or
                                     avconv), for example -f
                                     bestvideo+bestaudio.
    --all-formats                    download all available video formats
    --prefer-free-formats            prefer free video formats unless a specific
                                     one is requested
    --max-quality FORMAT             highest quality format to download
    -F, --list-formats               list all available formats
    --youtube-skip-dash-manifest     Do not download the DASH manifest on
                                     YouTube videos

## Subtitle Options:
    --write-sub                      write subtitle file
    --write-auto-sub                 write automatic subtitle file (youtube
                                     only)
    --all-subs                       downloads all the available subtitles of
                                     the video
    --list-subs                      lists all available subtitles for the video
    --sub-format FORMAT              subtitle format (default=srt) ([sbv/vtt]
                                     youtube only)
    --sub-lang LANGS                 languages of the subtitles to download
                                     (optional) separated by commas, use IETF
                                     language tags like 'en,pt'

## Authentication Options:
    -u, --username USERNAME          login with this account ID
    -p, --password PASSWORD          account password
    -2, --twofactor TWOFACTOR        two-factor auth code
    -n, --netrc                      use .netrc authentication data
    --video-password PASSWORD        video password (vimeo, smotri)

## Post-processing Options:
    -x, --extract-audio              convert video files to audio-only files
                                     (requires ffmpeg or avconv and ffprobe or
                                     avprobe)
    --audio-format FORMAT            "best", "aac", "vorbis", "mp3", "m4a",
                                     "opus", or "wav"; "best" by default
    --audio-quality QUALITY          ffmpeg/avconv audio quality specification,
                                     insert a value between 0 (better) and 9
                                     (worse) for VBR or a specific bitrate like
                                     128K (default 5)
    --recode-video FORMAT            Encode the video to another format if
                                     necessary (currently supported:
                                     mp4|flv|ogg|webm|mkv)
    -k, --keep-video                 keeps the video file on disk after the
                                     post-processing; the video is erased by
                                     default
    --no-post-overwrites             do not overwrite post-processed files; the
                                     post-processed files are overwritten by
                                     default
    --embed-subs                     embed subtitles in the video (only for mp4
                                     videos)
    --embed-thumbnail                embed thumbnail in the audio as cover art
    --add-metadata                   write metadata to the video file
    --xattrs                         write metadata to the video file's xattrs
                                     (using dublin core and xdg standards)
    --prefer-avconv                  Prefer avconv over ffmpeg for running the
                                     postprocessors (default)
    --prefer-ffmpeg                  Prefer ffmpeg over avconv for running the
                                     postprocessors
    --exec CMD                       Execute a command on the file after
                                     downloading, similar to find's -exec
                                     syntax. Example: --exec 'adb push {}
                                     /sdcard/Music/ && rm {}'

# OUTPUT TEMPLATE

The `-o` option allows users to indicate a template for the output file names. The basic usage is not to set any template arguments when downloading a single file, like in `ananse -o funny_video.flv "http://some/video"`. However, it may contain special sequences that will be replaced when downloading each video. The special sequences have the format `%(NAME)s`. To clarify, that is a percent symbol followed by a name in parenthesis, followed by a lowercase S. Allowed names are:

 - `id`: The sequence will be replaced by the video identifier.
 - `url`: The sequence will be replaced by the video URL.
 - `uploader`: The sequence will be replaced by the nickname of the person who uploaded the video.
 - `upload_date`: The sequence will be replaced by the upload date in YYYYMMDD format.
 - `title`: The sequence will be replaced by the video title.
 - `ext`: The sequence will be replaced by the appropriate extension (like flv or mp4).
 - `epoch`: The sequence will be replaced by the Unix epoch when creating the file.
 - `autonumber`: The sequence will be replaced by a five-digit number that will be increased with each download, starting at zero.
 - `playlist`: The name or the id of the playlist that contains the video.
 - `playlist_index`: The index of the video in the playlist, a five-digit number.

The current default template is `%(title)s-%(id)s.%(ext)s`.

In some cases, you don't want special characters such as 中, spaces, or &, such as when transferring the downloaded filename to a Windows system or the filename through an 8bit-unsafe channel. In these cases, add the `--restrict-filenames` flag to get a shorter title:

```bash
$ ananse --get-filename -o "%(title)s.%(ext)s" BaW_jenozKc
ananse test video ''_ä↭𝕐.mp4    # All kinds of weird characters
```

```bash
$ ananse --get-filename -o "%(title)s.%(ext)s" BaW_jenozKc --restrict-filenames
ananse_test_video_.mp4          # A simple file name
```

# VIDEO SELECTION

Videos can be filtered by their upload date using the options `--date`, `--datebefore` or `--dateafter`, they accept dates in two formats:

 - Absolute dates: Dates in the format `YYYYMMDD`.
 - Relative dates: Dates in the format `(now|today)[+-][0-9](day|week|month|year)(s)?`
 
Examples:

####Download only the videos uploaded in the last 6 months
`$ ananse --dateafter now-6months`
#### Download only the videos uploaded on January 1, 1970
```bash
$ ananse --date 19700101
$ # will only download the videos uploaded in the 200x decade
$ ananse --dateafter 20000101 --datebefore 20091231`
```

# DEVELOPER INSTRUCTIONS

To run Ananse as a developer, you don't need to build anything either. Simply execute

    python -m ananse

To run the test, simply invoke your favorite test runner, or execute a test file directly; any of the following work:

    python -m unittest discover
    python test/test_download.py
    nosetests --verbose

If you want to create a build of ananse yourself, you'll need

* python
* make
* pandoc
* zip
* nosetests

### Adding support for a new site

**Coming soon.** 
But any extractor that works in [youtube-dl](https://github.com/rg3/youtube-dl/) will work here

# CONTRIBUTING

See the [CONTRIBUTING file]()
# BUGS

See [CONTRIBUTING]()
# COPYRIGHT

Ananse is released into the public domain by the copyright holders.

**This README file is adapted from [youtube-dl](https://github.com/rg3/youtube-dl)**