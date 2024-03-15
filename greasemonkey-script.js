// ==UserScript==
// @name         Generate PR description
// @namespace    http://tampermonkey.net/
// @version      2024-03-14
// @description  Add button in Github to generate a description using AI
// @author       vincbeck
// @match        https://github.com/*
// @grant        GM_xmlhttpRequest
// ==/UserScript==

const generate_description = (button, url, callback) => {
    button.disabled = "disabled"

    GM_xmlhttpRequest({
        url: `https://gl2z6xs4lsw5aylaloez2ysedy0myviu.lambda-url.us-east-1.on.aws/example?url=${url}`,
        method: 'GET',
        onload: (response) => {
            button.disabled = ''
            callback(response.response)
        },
        onerror: (error) => {
            button.disabled = ''
            console.error(error)
            alert("Error while generating the description")
        }
    })
}

const generateButton = (url, callback) => {
    const button = document.createElement('button')
    button.type = 'button'
    button.innerHTML = 'Generate an alternative description'
    button.addEventListener('click', () => {
        generate_description(button, url, callback)
    })
    return button
}

(function() {
    'use strict';

    const path = window.location.href
    const prPageRegex = /(https\:\/\/github\.com\/.+\/pull\/[0-9]+).*/
    const matchCompareRegex = /(https:\/\/github\.com\/.+\/compare\/[^?]+).*/
    const isPrPage = prPageRegex.test(path)
    const isComparePage = matchCompareRegex.test(path)

    const url = isPrPage ? path.match(prPageRegex)[1] : isComparePage ? path.match(matchCompareRegex)[1] : null

    if (url) {
        if (isPrPage) {
            const discussionElement = document.getElementById('discussion_bucket')
            const mainElement = discussionElement.getElementsByClassName("Layout-main")[0]
            const descriptionElement = mainElement.getElementsByClassName("timeline-comment-group")[1]

            const callback = (response) => {
                document.getElementById('generate-pr-description-wrapper').innerHTML = `<p style="padding: 5px;">
${response.replace(new RegExp('\r?\n','g'), '<br />')}</p>`
            }
            const button = generateButton(url, callback)
            const wrapper = document.createElement('div')
            wrapper.id = 'generate-pr-description-wrapper'

            descriptionElement.appendChild(button)
            descriptionElement.appendChild(wrapper)
        } else {
            const callback = (response) => {
                document.getElementById('pull_request_body').value = response
            }
            const button = generateButton(url, callback)

            const sideBar = document.getElementsByClassName("Layout-sidebar")[0]
            sideBar.insertBefore(button, sideBar.firstChild);
        }
    }
})()