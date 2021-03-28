import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_update_motd_dir(host):
    f = host.file('/etc/update-motd.d')

    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'


def test_alteo_motd_file(host):
    f = host.file('/etc/update-motd.d/00-alteo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_motd_file(host):
    f = host.file('/etc/motd')

    assert f.is_symlink
    assert f.linked_to
    '/run/motd.dynamic'
    assert f.user == 'root'
    assert f.group == 'root'
