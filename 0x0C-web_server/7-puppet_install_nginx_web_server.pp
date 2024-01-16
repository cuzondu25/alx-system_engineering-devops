# Install and configure nginx server

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file { 'index.html':
  ensure  => 'present',
  content => 'Hello World!',
  path    => '/var/www/html/index.html',
}

file { '404.html':
  ensure  => 'present',
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page",
}

file { 'sites-available/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => @(CONFIG),
    server {
      listen 80;
      server_name localhost;

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }

      location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
      }

      error_page 404 /404.html;
      location = /404.html {
        root /var/www/html;
	internal;
      }
    }
  CONFIG
}

service { 'nginx':
  ensure  => 'true',
  restart => '/usr/sbin/service nginx restart',
}
