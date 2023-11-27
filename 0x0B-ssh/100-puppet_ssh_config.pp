
# 100-puppet_ssh_config.pp

file { '/home/your_username/.ssh/config':
  ensure => 'present',
  mode   => '0600',
  owner  => 'mcakyerima',
  group  => 'mcakyerima',
}

include stdlib

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/mcakyerima/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
