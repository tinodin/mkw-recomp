"""Tests for tools/build/release.py."""

import importlib.util
from pathlib import Path
import unittest


def _release_module():
    path = Path(__file__).with_name("release.py")
    spec = importlib.util.spec_from_file_location("build_release", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReleaseTest(unittest.TestCase):
    def test_safe_version_keeps_release_tags(self) -> None:
        release = _release_module()
        self.assertEqual(release.safe_version("1.2.3-rc.1+meta"), "1.2.3-rc.1+meta")

    def test_safe_version_sanitizes_workflow_dispatch_branch_name(self) -> None:
        release = _release_module()
        self.assertEqual(release.safe_version("feat/framegen"), "feat-framegen")


if __name__ == "__main__":
    unittest.main()
