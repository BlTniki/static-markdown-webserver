from app import FilesystemAccounter
from configs import Config

import unittest


class TestFilesystemAccounterImpl(unittest.TestCase):

    def setUp(self) -> None:
        print("setting up TestFilesystemAccounterImpl")
        config = Config()
        config.PATH_TO_VAULT = ""
        self.accounter = FilesystemAccounter(config)
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
