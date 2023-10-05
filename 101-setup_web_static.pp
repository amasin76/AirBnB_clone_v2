class web_static_setup {
  $nginx_package_name = 'nginx'
  $web_static_path = '/data/web_static'
  $fake_html_content = '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>'
  
  package { $nginx_package_name:
    ensure => installed,
  }

  file { $web_static_path:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    recurse => true,
  }

  file { "${web_static_path}/releases/test/index.html":
    ensure  => file,
    content => $fake_html_content,
    require => File[$web_static_path],
  }

  file { "${web_static_path}/current":
    ensure => link,
    target => "${web_static_path}/releases/test",
    force  => true,
    require => File["${web_static_path}/releases/test/index.html"],
  }

  file_line { 'nginx_config':
    path   => '/etc/nginx/sites-available/default',
    line   => '        location /hbnb_static {\n            alias /data/web_static/current/;\n        }',
    match  => '^        location /hbnb_static',
    after  => '^    server {',
    require => Package[$nginx_package_name],
    notify  => Service[$nginx_package_name],
  }

  service { $nginx_package_name:
    ensure     => running,
    enable     => true,
    hasrestart => true,
    hasstatus  => true,
    subscribe  => File_line['nginx_config'],
  }
}
