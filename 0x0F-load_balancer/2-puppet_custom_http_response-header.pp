# Installs a Nginx server with custome HTTP header

class { 'nginx':
    ensure => installed,
}

$file_path = '/etc/nginx/sites-available/default'
$target_line = 'listen [::]:80 default_server;'
$line_to_insert = 'add_header X-Served-By $hostname;'

file { $file_path:
    ensure => present
}

exec { 'insert_line_after_target':
    command => "sed -i '/${target_line}/a ${line_to_insert}' ${file_path}",
    unless  => "grep -q '${line_to_insert}' ${file_path}",
    require => File[$file_path],
}
