<?php
error_reporting(E_ALL & ~E_DEPRECATED & ~E_NOTICE);

require_once __DIR__ . '/vendor/autoload.php';

use Graby\Graby;

$article = 'https://www.kdnuggets.com/sql-simplified-crafting-modular-and-understandable-queries-with-ctes';
$graby = new Graby();
$result = $graby->fetchContent($article);
echo($result->getHtml());