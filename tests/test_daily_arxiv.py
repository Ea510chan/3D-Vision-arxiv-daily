import tempfile
import unittest
from pathlib import Path

import daily_arxiv as da

SAMPLE_ROW_1 = "|**2025-01-02**|**Title A**|Author A et.al.|[1234.5678](http://arxiv.org/abs/1234.5678)|null|\n"
SAMPLE_ROW_2 = "|**2025-03-04**|**Title B**|Author B et.al.|[2345.6789](http://arxiv.org/abs/2345.6789)|null|\n"


class DailyArxivTest(unittest.TestCase):
    def test_slugify_topic(self):
        self.assertEqual(da.slugify_topic("3D Reconstruction"), "3d-reconstruction")
        self.assertEqual(da.slugify_topic("Point Cloud Registration"), "point-cloud-registration")

    def test_normalize_topics_merges_and_drops(self):
        data = {
            "3D Registration": {"id1": SAMPLE_ROW_1},
            "SFM": {"id2": SAMPLE_ROW_2},
            "Keypoint Detection": {"id3": SAMPLE_ROW_1},
            "SLAM": {"id4": SAMPLE_ROW_1},
        }
        topic_merge = {
            "3D Registration": "Point Cloud Registration",
            "SFM": "3D Reconstruction",
        }
        topic_drop = ["Keypoint Detection"]
        allowed = ["Point Cloud Registration", "3D Reconstruction", "SLAM"]

        normalized = da.normalize_topics(data, topic_merge, topic_drop, allowed)

        self.assertIn("Point Cloud Registration", normalized)
        self.assertIn("3D Reconstruction", normalized)
        self.assertIn("SLAM", normalized)
        self.assertNotIn("Keypoint Detection", normalized)
        self.assertEqual(len(normalized["Point Cloud Registration"]), 1)
        self.assertEqual(len(normalized["3D Reconstruction"]), 1)

    def test_paper_to_dict_from_row(self):
        data = da.paper_to_dict("1234.5678", SAMPLE_ROW_1)
        self.assertEqual(data["title"], "Title A")
        self.assertEqual(data["arxiv_id"], "1234.5678")
        self.assertTrue(data["arxiv_url"].startswith("http://arxiv.org/abs/"))
        self.assertTrue(data["pdf_url"].endswith(".pdf"))

    def test_write_index_and_topic_pages(self):
        data = {
            "Topic A": {"id1": SAMPLE_ROW_1},
            "Topic B": {"id2": SAMPLE_ROW_2},
        }
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            index_path = tmp_path / "README.md"
            topics_dir = tmp_path / "topics"

            da.write_index_page(
                data,
                str(index_path),
                "topics",
                link_ext=".md",
                usage_link="./docs/README.md#usage",
                show_badge=False,
                to_web=False,
                pages_url="https://example.com/pages",
                repo_url="https://example.com/repo",
            )
            da.write_topic_pages(data, str(topics_dir), to_web=False)

            index_contents = index_path.read_text()
            self.assertIn("# 3D Vision arXiv Daily", index_contents)
            self.assertIn("Topics: 2", index_contents)
            self.assertIn("[Topic A](topics/topic-a.md)", index_contents)

            topic_a_path = topics_dir / "topic-a.md"
            self.assertTrue(topic_a_path.exists())
            topic_contents = topic_a_path.read_text()
            self.assertIn("# Topic A", topic_contents)
            self.assertIn("| Publish Date | Title | Authors | PDF | Code |", topic_contents)


if __name__ == "__main__":
    unittest.main()
