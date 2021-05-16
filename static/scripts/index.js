
const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// icones
const BOT_IMG = "static/artur.png";
const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";
const BOT_NAME = "A.R.T.U.R.";
const PERSON_NAME = "Você";

msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";
    botResponse(msgText);
});

function appendMessage(name, img, side, text) {
    //   Simple solution for small apps
    const msgHTML = `
        <div class="msg ${side}-msg">
            <div class="msg-img" style="background-image: url(${img})"></div>
                <div class="msg-bubble">
                    <div class="msg-info">
                    <div class="msg-info-name">${name}</div>
                    <div class="msg-info-time">${formatDate(new Date())}</div>
                </div>
                <div class="msg-text">${text}</div>
            </div>
        </div>
        `;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botResponse(rawText) {

    // Bot Response
    $.get("/get", { msg: rawText }).done(function (data) {
        resObj = JSON.parse(data)
        const msgText = resObj.text;
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
    });
}

// Utils
function get(selector, root = document) {
    return root.querySelector(selector);
}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}
