from click.testing import CliRunner
import glci


def test_search():
    runner = CliRunner()
    result = runner.invoke(glci.search, ["--path", ".", "--ftype", "py"])
    assert result.exit_code == 0
    assert "test_glci" in result.output
