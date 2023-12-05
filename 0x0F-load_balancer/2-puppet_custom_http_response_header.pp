# A puppet script to auto-configure new server with new header
include stdlib

exec { 'update_server':
    command  => 'apt-get -y update',
    user     => 'root',
    provider => 'shell'
}

-> package { 'nginx':
    ensure   => present,
    provider => 'apt'
}

-> file_line { 'custom_header':
    ensure =>
    path   => '/etc/nginx/sites-enabled/defaul',
    after  => 'listen [::]:80 default_server;',
    line   => 'add_header X-Served-By $hostname;'
}

-> exec { 'restart_nginx':
    path    => '/usr/bin',
    command => 'sudo service nginx restart',
    require => [Package'nginx'], File_line['custom_header']]
}
