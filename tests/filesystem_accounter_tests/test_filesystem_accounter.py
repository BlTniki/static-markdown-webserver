from app.filesystem_accounter import FilesystemAccounter
from configs import ConfigHandler, TestConfig

import unittest


class TestFilesystemAccounterImpl(unittest.TestCase):

    def setUp(self) -> None:
        print("setting up TestFilesystemAccounter")

        # Setting specific test config
        ConfigHandler.set_config(TestConfig())

        self.accounter = FilesystemAccounter(ConfigHandler.get_config())
        self.accounter._wd.observer.stop()

        self.accounter._file_tree = [
            {
                'text': 'foo',
                'children': [
                    {
                        'text': 'testfoo.png',
                        'a_attr':
                         {
                             'href': '/md_static/foo/testfoo.png'
                         }
                    },
                    {
                        'text': 'bar',
                        'children': [
                            {
                                'text': 'testbar.png',
                                'a_attr':
                                    {
                                        'href': '/md_static/foo/bar/testbar.png'
                                    }
                            }
                        ]
                    }
                ]
            },
            {
                'text': 'test.png',
                'a_attr':
                    {
                        'href': '/md_static/attach/test.png'
                    }
            }
        ]

    def test_get_file_tree_for_dir_valid(self):
        urls = ["/foo/bar", "foo/bar", "/foo/bar/"]
        model_result = [
                            {
                                'text': 'testbar.png',
                                'a_attr':
                                    {
                                        'href': '/md_static/foo/bar/testbar.png'
                                    }
                            }
                        ]

        for url in urls:
            self.assertEqual(self.accounter.get_file_tree_for_dir(url), model_result, f"for {url}")

    def test_get_file_tree_for_dir_non_exist(self):
        urls = ["/foo/kek", "/foo/test.png", "/foo/attach/testbar.png"]

        for url in urls:
            self.assertRaises(ValueError, self.accounter.get_file_tree_for_dir, url)

    def test_get_file_tree_for_dir_non_dir(self):
        urls = ["/test.png", "/foo/bar/testbar.png"]

        for url in urls:
            self.assertRaises(ValueError, self.accounter.get_file_tree_for_dir, url)
