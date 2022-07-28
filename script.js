'use strict';

const images = [
    { 'id': '1', 'url':'chrono.jpg'},
    { 'id': '2', 'url':'inuyasha.jpg'},
    { 'id': '3', 'url':'tenchi.jpg'},
    { 'id': '4', 'url':'tenjhotenge.jpg'},
    { 'id': '5', 'url':'yuyuhakusho.jpg'},
    { 'id': '6', 'url':'ippo.png'},
]

const containerItems = document.querySelector('#container-items');
const loadImages = (images, container) =>{
    images.forEach (image => {
        container.innerHTML += `
        <div class='item'>
        <img src='${image.url}'
        </div>
        `
    })
}

loadImages(images, containerItems)

let items = document.querySelectorAll('.item'); //seleciona todas as imagens

const previous = () => {
    containerItems.appendChild(items[0]);
    items = document.querySelectorAll('.item');
}

const next = () => {
    const lastItem = items[items.length - 1];
    containerItems.insertBefore(lastItem, items[0])
    items = document.querySelectorAll('.item');
}

const btnNext = document.querySelector('#next').addEventListener('click', next);
const btnPrevious = document.querySelector('#previous').addEventListener('click', previous);
