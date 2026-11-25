<?php
defined( 'ABSPATH' ) || exit;
add_action( 'wp_enqueue_scripts', static function () {
    wp_enqueue_style( 'garden-leaf', get_theme_file_uri( 'garden.css' ), array(), '1.0' );
} );
