"use strict";

(function() {
    window.addEventListener("load", () => {
        const row_urls = document.querySelectorAll('tr[data-url]')
        row_urls.forEach(item => {
            item.addEventListener('click', event => {
                const url = item.getAttribute('data-url')
                if (url) {
                    window.location.href = url
                }
            })
        })
        const tabs = document.querySelectorAll('ul.logged-tabs li')
        tabs.forEach(item => {
            item.addEventListener('click', event => {
                const link = item.querySelector('a')
                const url = link.getAttribute('href')
                if (url) {
                    window.location.href = url
                }
            })
        })
    })
})()