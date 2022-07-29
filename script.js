'use strict';

const images = [
    { 'id': 'Chrono', 'url':'chrono.jpg'},
    { 'id': 'Inuyasha', 'url':'inuyasha.jpg'},
    { 'id': 'Tenchi', 'url':'tenchi.jpg'},
    { 'id': 'Tenjhotenge', 'url':'tenjhotenge.jpg'},
    { 'id': 'Yuyuhakusho', 'url':'yuyuhakusho.jpg'},
    { 'id': 'Ippo', 'url':'ippo.png'},
]

const containerItems = document.querySelector('#container-items');
const loadImages = (images, container) =>{
    images.forEach (image => {
        container.innerHTML += `
        <div class='item'>
        <img src='${image.url}'>

        <div class='item-overlay'>
            <h1>${image.id}</h1>
            <p>teste</p>
        </div>


        
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

const auto = () => {
    setInterval(previous, 3000);
}

auto()

const btnNext = document.querySelector('#next').addEventListener('click', next);
const btnPrevious = document.querySelector('#previous').addEventListener('click', previous);
