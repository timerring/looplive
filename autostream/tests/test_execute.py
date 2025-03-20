# Copyright (c) 2025 autostream

import unittest
from unittest.mock import patch, MagicMock
from autostream.execute.scan_and_execute import scan_folder_and_execute

class TestScanAndExecute(unittest.TestCase):

    def test_scan_folder_and_execute(self):
        folder_to_scan = "/home/jh/Downloads/autostream/videos"
        command_to_execute = "ffmpeg -re -i {file_path} -c copy -f flv {stream_url}"
        scan_folder_and_execute(folder_to_scan, command_to_execute)