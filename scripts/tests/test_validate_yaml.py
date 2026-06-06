import subprocess
import tempfile
import pathlib

def test_validate_yaml():
    # Write a valid yaml file
    with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w", delete=False) as f:
        f.write("key: value\n")
        valid_yaml_path = f.name

    # Write an invalid yaml file
    with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w", delete=False) as f:
        f.write("key: : value\n")
        invalid_yaml_path = f.name

    try:
        # Check valid YAML passes
        res = subprocess.run(["python3", "skills/agent-job-app-tailor/scripts/validate_yaml.py", valid_yaml_path], capture_output=True)
        assert res.returncode == 0

        # Check invalid YAML fails
        res2 = subprocess.run(["python3", "skills/agent-job-app-tailor/scripts/validate_yaml.py", invalid_yaml_path], capture_output=True)
        assert res2.returncode == 1
    finally:
        pathlib.Path(valid_yaml_path).unlink()
        pathlib.Path(invalid_yaml_path).unlink()
