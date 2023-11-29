# File: 7-puppet_install_nginx_web_server.pp
# Author: Mc Ak Yerima
# Description: Puppet manifest to install and configure Nginx web server

class web_server {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure => file,
    content => template('web_server/nginx.conf.erb'),
    notify => Service['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }
}

class { 'web_server': }

# Redirect configuration
nginx::resource::vhost { 'redirect_me':
  ensure  => present,
  www_root => '/var/www/html',
  port    => '80',
  rewrite_rules => [
    'location /redirect_me {',
    '  return 301 /;',
    '}',
  ],
}
