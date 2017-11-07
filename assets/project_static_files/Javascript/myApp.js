"use strict"

$(document).ready(function(){


var pictureList = [
    "static/Specs_images/CornSpecs.png",
    "static/Specs_images/SoybeanSpecs.png",//% static 'Specs_images/SoybeanSpecs.png' %
    "static/Specs_images/WheatSpecs.png",
    "static/Specs_images/SoybeanMealSpecs.png",
    "static/Specs_images/SoybeanOilSpecs.png",
    "static/Specs_images/OatsSpecs.png",
    "static/Specs_images/RiceSpecs.png",
    "static/Specs_images/CattleSpecs.png",
    "static/Specs_images/HogSpecs.png",
    "static/Specs_images/MilkSpecs.png",
    "static/Specs_images/CoffeeSpecs.png",
    "static/Specs_images/CocoaSpecs.png",
    "static/Specs_images/CottonSpecs.png",
    "static/Specs_images/OJ-Specs.png",
    "static/Specs_images/SugarSpecs.png",
  ];

$('#picDD').change(function () {
    var val = parseInt($('#picDD').val());
    $('#specpics').attr("src",pictureList[val]);
});


});
