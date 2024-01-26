# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['reload_pam'],
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['reload_pam'],
}

# Reload PAM to apply the changes immediately.
exec { 'reload_pam':
  command => 'pkill -HUP -x -u holberton sshd',
  path    => '/usr/local/bin/:/bin/',
  refreshonly => true,
}
