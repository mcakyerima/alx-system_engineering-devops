# Puppet manifest to configure Nginx with a custom HTTP header
# The name of the custom HTTP header is X-Served-By
# The value of the custom HTTP header is the hostname of the server Nginx is running on

# Install Nginx package

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Define the custom HTTP header content
$custom_header_content = "location / {\n\tadd_header X-Served-By $hostname;\n}"

# Add the custom HTTP header content to the Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => inline_template("<%= content() %>\n$custom_header_content"),
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/sites-available/default']],
}
