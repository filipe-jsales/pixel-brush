'use strict';

const images = [
    { 'id': '1', 'url':'1.png'},
    { 'id': '2', 'url':'2.png'},
    { 'id': '3', 'url':'3.png'},
    { 'id': '4', 'url':'4.png'},
]

const container = document.querySelector('#container-items');

const loadImages = (images, container) =>{
    images.forEach (image => {
        container.innerHTML += `
            <div class='item'>
                <img src='${image.url}'
            </div>
        `
    })
}

loadImages(images, container)

