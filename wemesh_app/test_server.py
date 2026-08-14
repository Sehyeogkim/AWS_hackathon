import unittest

import server


class WemeshDemoTests(unittest.TestCase):
    def test_team_fixture_totals(self):
        team = server.team_payload()
        self.assertEqual(len(team["members"]), 6)
        self.assertEqual(team["totals"], {"nodes": 135, "edges": 123, "evidence": 50})
        self.assertEqual(len(team["gaps"]), 6)
        self.assertEqual([(member["node_count"], member["edge_count"]) for member in team["members"]], [(28, 28), (38, 36), (18, 15), (23, 22), (12, 10), (16, 12)])
        self.assertTrue(all(len(member["nodes"]) == member["node_count"] for member in team["members"]))
        self.assertTrue(all(len(member["edges"]) == member["edge_count"] for member in team["members"]))

    def test_authorized_linkedin_url(self):
        self.assertEqual(
            server.validate_linkedin_url(server.AUTHORIZED_PROFILE_URL),
            server.AUTHORIZED_PROFILE_URL,
        )
        with self.assertRaises(ValueError):
            server.validate_linkedin_url("https://example.com/profile")

    def test_scoring_is_traceable_and_not_short_token_biased(self):
        candidate = server.load_json(server.DATA_DIR / "sehyeog-kim-kg.json")
        result = server.score_candidate(candidate)
        self.assertEqual(len(result["fit"]["rubric"]), 5)
        self.assertEqual(len(result["fit"]["gap_results"]), 6)
        self.assertEqual(len(result["questions"]), 6)
        self.assertEqual(result["fit"]["overall"], 46)
        self.assertEqual(result["fit"]["potential_fit"], "2/6")
        self.assertEqual(result["fit"]["rubric"][0]["score"], 0)
        self.assertEqual([gap["status"] for gap in result["fit"]["gap_results"]], ["Transferable only", "Transferable only", "No explicit evidence", "No explicit evidence", "No explicit evidence", "No explicit evidence"])
        self.assertIn("does not show direct Bedrock & AgentCore experience", result["questions"][2]["question"])
        self.assertEqual(len(result["candidate"]["nodes"]), 38)
        self.assertEqual(len(result["candidate"]["edges"]), 32)
        self.assertEqual(len(result["evidence_samples"]), 38)
        self.assertTrue(all(result["evidence_samples"].values()))
        top_labels = [gap["matches"][0]["label"] for gap in result["fit"]["gap_results"] if gap["matches"]]
        self.assertNotIn("C++", top_labels)
        for gap in result["fit"]["gap_results"]:
            for match in gap["matches"]:
                self.assertTrue(match["evidence_ids"])


if __name__ == "__main__":
    unittest.main()
