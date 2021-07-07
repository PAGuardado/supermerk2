<?php 

//url aquispe
define('URL_SITIO', 'http://127.0.0.1:5500/paypal/');

require 'paypal/autoload.php';

$apiContext = new \PayPal\Rest\ApiContext(
    new \PayPal\Auth\OAuthTokenCredential(
        'Abv2RPgee4qO6MqNGJ1QXvPIODh-TzztVwWvkysOYpJNUZwBe_n60HLoTJYy52jRwPm8DlNkoZKo3MzR',     // ClientID
        'EKdnBpyX97S3I1vIzTRzHjnY7k2p2rgdizVjrUG70Lk77IYufIiRso9ez2hXAEJnbTJS8ASDx1kqh_tj'      // ClientSecret
    )
);

