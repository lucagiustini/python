import subprocess

def test_ssh_connection(ip_address, username, password):
    ssh_command = f'ssh {username}@{ip_address} "echo successful"'
    try:
        subprocess.check_output(ssh_command, shell=True, timeout=10)
    except subprocess.CalledProcessError:
        print("SSH connection failed. Test successful!")
    except subprocess.TimeoutExpired:
        print("SSH connection timed out. Test successful!")
    else:
        print("SSH connection successful. Test failed!")
# Example usage
test_ssh_connection('192.168.32.134', 'user', 'user')
