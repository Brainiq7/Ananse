# coding: utf-8
from __future__ import unicode_literals

import json
import random
import re

from .common import InfoExtractor
from ..compat import (
    compat_str,
)


class EightTracksIE(InfoExtractor):
    IE_NAME = '8tracks'
    _VALID_URL = r'https?://8tracks\.com/(?P<user>[^/]+)/(?P<id>[^/#]+)(?:#.*)?$'
    _TEST = {
        "name": "EightTracks",
        "url": "http://8tracks.com/ytdl/ananse-test-tracks-a",
        "info_dict": {
            'id': '1336550',
            'display_id': 'ananse-test-tracks-a',
            "description": "test chars:  \"'/\\ä↭",
            "title": "ananse test tracks \"'/\\ä↭<>",
        },
        "playlist": [
            {
                "md5": "96ce57f24389fc8734ce47f4c1abcc55",
                "info_dict": {
                    "id": "11885610",
                    "ext": "m4a",
                    "title": "youtue-dl project<>\"' - ananse test track 1 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "4ab26f05c1f7291ea460a3920be8021f",
                "info_dict": {
                    "id": "11885608",
                    "ext": "m4a",
                    "title": "ananse project - ananse test track 2 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "d30b5b5f74217410f4689605c35d1fd7",
                "info_dict": {
                    "id": "11885679",
                    "ext": "m4a",
                    "title": "ananse project as well - ananse test track 3 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "4eb0a669317cd725f6bbd336a29f923a",
                "info_dict": {
                    "id": "11885680",
                    "ext": "m4a",
                    "title": "ananse project as well - ananse test track 4 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "1893e872e263a2705558d1d319ad19e8",
                "info_dict": {
                    "id": "11885682",
                    "ext": "m4a",
                    "title": "PH - ananse test track 5 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "b673c46f47a216ab1741ae8836af5899",
                "info_dict": {
                    "id": "11885683",
                    "ext": "m4a",
                    "title": "PH - ananse test track 6 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "1d74534e95df54986da7f5abf7d842b7",
                "info_dict": {
                    "id": "11885684",
                    "ext": "m4a",
                    "title": "phihag - ananse test track 7 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            },
            {
                "md5": "f081f47af8f6ae782ed131d38b9cd1c0",
                "info_dict": {
                    "id": "11885685",
                    "ext": "m4a",
                    "title": "phihag - ananse test track 8 \"'/\\\u00e4\u21ad",
                    "uploader_id": "ytdl"
                }
            }
        ]
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        playlist_id = mobj.group('id')

        webpage = self._download_webpage(url, playlist_id)

        json_like = self._search_regex(
            r"(?s)PAGE.mix = (.*?);\n", webpage, 'trax information')
        data = json.loads(json_like)

        session = str(random.randint(0, 1000000000))
        mix_id = data['id']
        track_count = data['tracks_count']
        first_url = 'http://8tracks.com/sets/%s/play?player=sm&mix_id=%s&format=jsonh' % (session, mix_id)
        next_url = first_url
        entries = []
        for i in range(track_count):
            api_json = self._download_webpage(
                next_url, playlist_id,
                note='Downloading song information %d/%d' % (i + 1, track_count),
                errnote='Failed to download song information')
            api_data = json.loads(api_json)
            track_data = api_data['set']['track']
            info = {
                'id': compat_str(track_data['id']),
                'url': track_data['track_file_stream_url'],
                'title': track_data['performer'] + ' - ' + track_data['name'],
                'raw_title': track_data['name'],
                'uploader_id': data['user']['login'],
                'ext': 'm4a',
            }
            entries.append(info)
            next_url = 'http://8tracks.com/sets/%s/next?player=sm&mix_id=%s&format=jsonh&track_id=%s' % (
                session, mix_id, track_data['id'])
        return {
            '_type': 'playlist',
            'entries': entries,
            'id': compat_str(mix_id),
            'display_id': playlist_id,
            'title': data.get('name'),
            'description': data.get('description'),
        }
