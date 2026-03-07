import pytest
from unittest.mock import Mock, patch

class CIPipeline:
    def __init__(self, test_runner, notifier):
        self.test_runner = test_runner
        self.notifier = notifier
        self.results = []

    def run(self, branch):
        result = self.test_runner.run_tests()
        self.results.append({"branch": branch, "passed": result["passed"], "failed": result["failed"]})
        if result["failed"] > 0:
            self.notifier.alert(f"Tests failed on branch {branch}: {result['failed']} failures")
            return False
        self.notifier.notify(f"All tests passed on branch {branch}")
        return True
    
@pytest.fixture
def runner():
    m = Mock()
    m.run_tests.return_value = {"passed": 10, "failed": 0}
    return m

@pytest.fixture
def notifier():
    return Mock()

@pytest.fixture
def pipeline(runner, notifier):
    return CIPipeline(runner, notifier)

def test_pipeline_success(pipeline, notifier):
    result = pipeline.run("main")
    assert result == True
    notifier.notify.assert_called_once_with("All tests passed on branch main")

def test_pipeline_failure(pipeline, runner, notifier):
    runner.run_tests.return_value = {"passed": 8, "failed": 2}
    result = pipeline.run("feature")
    assert result == False
    notifier.alert.assert_called_once_with("Tests failed on branch feature: 2 failures")

def test_pipeline_history(pipeline, runner):
    pipeline.run("main")
    runner.run_tests.return_value = {"passed": 5, "failed": 1}
    pipeline.run("dev")
    assert len(pipeline.results) == 2
    assert pipeline.results[0]["branch"] == "main"

