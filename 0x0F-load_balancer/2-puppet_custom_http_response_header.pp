# A puppet script to auto-configure new server with new header
include stdlib

package { "nginx":
    ensure => 'installed',
}

file_line { "custom_header":
    path  => '/etc/nginx/sites-enabled/defaul',
    line  => 'add_header X-Served-By $hostname;',
    after => 'listen [::]:80 default_server;',
}

exec { "restart_nginx":
    path    => '/usr/bin',
    command => 'sudo service nginx restart',
    require => [Package["nginx"], File_line["custom_header"]]
}
